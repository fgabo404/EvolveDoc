"""Check category identity, retired-ID aliases and preserved regional provenance."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT/path).read_text())


def require(value,message):
    if not value:
        raise ValueError(message)


def validate_categories():
    aliases={};entities={};scientific_ids=set()
    for folder in ['plants','animals']:
        d=read(f'data/{folder}/{folder}.catalog.guide.json')
        for r in read(f'data/{folder}/{folder}.biological.catalog.json')['taxa']:
            scientific_ids.add(r['id'])
        local={e['id']:e for e in d['speciesCandidates']}
        require(len(local)==len(d['speciesCandidates']),'Duplicate gameplay identity')
        require(not entities.keys() & local.keys(),'Duplicate cross-catalog identity')
        entities.update(local)
        for a in d['entityAliases']:
            require(a['previousId'] not in aliases and a['previousId'] not in local,'Reused retired identity')
            require(a['entityId'] in local,'Unresolved alias target')
            aliases[a['previousId']]=a['entityId']
        for e in local.values():
            if 'sourceVariants' not in e:continue
            require(e['id'] not in scientific_ids,'Gameplay category reuses a scientific definition ID')
            variants=e['sourceVariants']
            require(len(variants)>=2,'Generalized category without source variants')
            require(all(aliases.get(v['id'])==e['id'] for v in variants),'Source variant/alias mismatch')
            require(set(e['biomeVariantIds'])=={b for v in variants for b in v['biomeVariantIds']},'Grouped habitat references changed')
            require(e['taxonomy']['scientificName'] is None,'General category requires exact species')
            require(e['taxonResolution']['selectionMode']=='optional_scientific_reference','Science is mandatory for category')
    require(not aliases.keys() & entities.keys(),'Retired ID still active')
    seen=set()
    for o in read('data/world/world.catalog.guide.json')['resourceOccurrences']:
        require(o['definitionId'] not in aliases,'World still references retired ID')
        if 'sourceDefinitionId' in o:
            require(aliases.get(o['sourceDefinitionId'])==o['definitionId'],'Occurrence lost source provenance')
            seen.add(o['sourceDefinitionId'])
    require(seen==aliases.keys(),'Retired source lost all world occurrences')
    fox=next(e for e in entities.values() if e.get('tag')=='foxes')
    require(fox['name']=={'en':'Foxes','es':'Zorros'},'Fox category label changed')
    require([p['resourceId'] for p in fox['potentialProducts']]==['RES#000031'],'Fox output must remain hide only')
    bindings=read('data/resources/resources.catalog.guide.json')['sourceBindings']
    require(all(b['sourceId'] not in aliases for b in bindings),'Resource binding still references retired source')
    require(sum(b['sourceId']==fox['id'] for b in bindings)==1,'Fox output binding duplicated')
    return {'entityCount':len(entities),'generalizedCategoryCount':sum('sourceVariants' in e for e in entities.values()),'retiredIdCount':len(aliases)}


if __name__=='__main__':
    print('Validated gameplay categories: '+json.dumps(validate_categories()))
