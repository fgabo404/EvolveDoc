"""Validate biological reference identities, evidence and cross-catalog boundaries offline.

This checks the stored name-match evidence, not a live taxonomic service or historical truth.
"""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read(path):
    return json.loads((ROOT / path).read_text())


def validate_biology():
    all_ids, all_tags, provider_keys = set(), set(), set()
    totals = dict(taxonCount=0, biologicalFormCount=0, lineageRelationCount=0)
    for folder in ['plants','animals']:
        data = read(f'data/{folder}/{folder}.biological.catalog.json')
        guide = read(f'data/{folder}/{folder}.catalog.guide.json')
        require(guide['biologicalCatalogFile'] == f'{folder}.biological.catalog.json', 'Wrong biological catalog link')
        require(data['runtimePolicy']['loadAsGameDefinitions'] is False, 'Biology reference enabled for runtime')
        taxa = {t['id']:t for t in data['taxa']}
        forms = {f['id']:f for f in data['biologicalForms']}
        sources = {s['sourceKey'] for s in data['evidenceSources']}
        require(len(sources)==len(data['evidenceSources']), 'Duplicate bibliography keys')
        require(len(taxa)==len(data['taxa']) and len(forms)==len(data['biologicalForms']), 'Duplicate biology IDs')
        for record in data['taxa']+data['biologicalForms']:
            require(record['id'] not in all_ids, 'Duplicate global biology ID')
            require(record['tag'] not in all_tags, 'Duplicate biology tag')
            all_ids.add(record['id']);all_tags.add(record['tag'])
            require(re.fullmatch(r'[a-z][a-z0-9]*(?:_[a-z0-9]+)*',record['tag']), 'Invalid biology tag')
            require(record['runtimeEnabled'] is False, 'Biology record enabled')
            require(set(record['name'])=={'en','es'} and all(record['name'].values()), 'Missing localized biology name')
        for taxon in taxa.values():
            prefix={'plant':'PLT','animal':'ANM','alga':'ALG','lichenized_fungus':'FNG'}[taxon['organismGroup']]
            require(re.fullmatch(prefix+r'#(?!000000)\d{6}',taxon['id']), 'Wrong taxon prefix')
            require((folder=='animals')==(prefix=='ANM'), 'Misfiled taxon')
            tax = taxon['taxonomy']
            require(taxon['taxonRank'] in ['SPECIES','SUBSPECIES','VARIETY'], 'Unsupported taxon rank')
            require(tax['taxonomicStatus']=='ACCEPTED', 'Nonaccepted taxon')
            if prefix in ['PLT','ANM','FNG']:
                require(tax['kingdom']=={'PLT':'Plantae','ANM':'Animalia','FNG':'Fungi'}[prefix], 'Wrong scientific kingdom')
            key=(tax['provider'],tax['providerTaxonKey'])
            require(key not in provider_keys, 'Duplicate accepted provider taxon');provider_keys.add(key)
            require(tax['matchEvidence'], 'Taxon without match evidence')
            for match in tax['matchEvidence']:
                require(match['matchType']=='EXACT' and match['confidence']>=95, 'Unsafe taxonomy match')
                require(match['matchStatus'] in ['ACCEPTED','SYNONYM'] and match['requestUrl'].startswith('https://'), 'Invalid match evidence')
        for form in forms.values():
            require(re.fullmatch(r'FRM#(?!000000)\d{6}',form['id']), 'Invalid form ID')
            require(form['taxonId'] in taxa, 'Unknown form taxon')
            require(set(form['evidenceSourceKeys'])<=sources, 'Unresolved form bibliography')
        edges={f:set() for f in forms}
        for relation in data['lineageRelations']:
            parents,children=set(relation['parentFormIds']),set(relation['childFormIds'])
            require(parents and children and not parents&children, 'Empty/self ancestry')
            require(parents|children<=forms.keys(), 'Unknown lineage form')
            require(len(parents)==len(relation['parentFormIds']) and len(children)==len(relation['childFormIds']), 'Duplicate lineage endpoint')
            require(relation['evidenceSourceKeys'] and set(relation['evidenceSourceKeys'])<=sources, 'Missing lineage bibliography')
            require(relation['runtimeEnabled'] is False and relation['exactAncestralPopulationResolved'] is False, 'Unreviewed executable lineage')
            require(set(relation['description'])=={'en','es'}, 'Missing lineage localization')
            if relation['relationType']=='hybrid_origin':require(len(parents)>=2, 'Hybrid origin requires joint parents')
            # Introgression may legitimately be bidirectional. Only founding/selection edges form a DAG.
            if relation['relationType']!='introgression':
                for parent in parents:edges[parent].update(children)
        active,visited=set(),set()
        def visit(node):
            require(node not in active, 'Founding/selection lineage cycle')
            if node in visited:return
            active.add(node)
            for child in edges[node]:visit(child)
            active.remove(node);visited.add(node)
        for node in edges:visit(node)
        for excluded in data['excludedLineageRelations']:
            require(excluded['parentFormId'] in forms and excluded['childFormId'] in forms, 'Unknown excluded endpoint')
            require(excluded['evidenceSourceKeys'] and set(excluded['evidenceSourceKeys'])<=sources, 'Missing exclusion evidence')
            require(excluded['runtimeEnabled'] is False, 'Executable excluded lineage')
            require(excluded['childFormId'] not in edges[excluded['parentFormId']], 'Excluded ancestry was also included')
        for candidate in guide['speciesCandidates']+guide.get('agriculturalCropCandidates',[]):
            resolution=candidate['taxonResolution']
            require(resolution['taxonIds'] and set(resolution['taxonIds'])<=taxa.keys(), 'Unresolved candidate taxon')
            require(set(resolution['formIds'])<=forms.keys(), 'Unresolved candidate form')
            require(all(forms[f]['taxonId'] in resolution['taxonIds'] for f in resolution['formIds']), 'Form not in selected taxa')
            require(resolution['inheritResourceBindings'] is False, 'Implicit species resource inheritance')
        expected={'taxonCount':len(taxa),'biologicalFormCount':len(forms),'lineageRelationCount':len(data['lineageRelations']),'excludedLineageRelationCount':len(data['excludedLineageRelations']),'sourceCandidateCount':len(guide['speciesCandidates']),'cropCandidateCount':len(guide.get('agriculturalCropCandidates',[]))}
        require(expected==data['summary'], 'Biology summary mismatch')
        require(data['status']=='optional_scientific_background_not_gameplay_entity_catalog', 'Scientific reference must remain optional')
        for key in totals:totals[key]+=expected[key]
    return totals


if __name__=='__main__':
    print('Validated stored biology references: '+json.dumps(validate_biology()))
