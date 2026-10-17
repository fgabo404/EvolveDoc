"""Check resource-guide identities, source/product links and unresolved-data boundaries.

Standard-library domain checks; this is not a general JSON Schema validator.
"""
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]


def require(condition,message):
    if not condition:raise ValueError(message)


def read(path):return json.loads((ROOT/path).read_text())


def validate_resources():
    data=read('data/resources/resources.catalog.guide.json')
    plants=read('data/plants/plants.catalog.guide.json');animals=read('data/animals/animals.catalog.guide.json');minerals=read('data/minerals/minerals.catalog.guide.json')
    by_id={r['id']:r for r in data['resources']}
    tags={r['tag']:r for r in data['resources']}
    require(len(by_id)==len(data['resources'])==len(tags),'Duplicate resource IDs or tags')
    require(not data['runtimePolicy']['loadAsGameDefinitions'],'Guide must remain runtime-disabled')
    for resource in data['resources']:
        require(re.fullmatch(r'RES#[0-9]{6}',resource['id']) and resource['id']!='RES#000000','Invalid resource ID')
        require(re.fullmatch(r'[a-z][a-z0-9]*(?:_[a-z0-9]+)*',resource['tag']),'Invalid resource tag')
        require(not resource['tag'].endswith('_service'),'Services must not become inventory materials')
        require(resource['inventory']['storable'] is True,'Resource must be a storable material')
        require(resource['inventory']['quantityUnit'] is None,'Inventory units are not approved yet')
        for field in ['name','description']:
            require(all(resource[field].get(lang) for lang in ['en','es']),'Missing resource localization')
    collections={'plantSpeciesCandidates':plants['speciesCandidates'],'animalSpeciesCandidates':animals['speciesCandidates'],'agriculturalCropCandidates':plants['agriculturalCropCandidates'],'geologicalResourceCandidates':minerals['geologicalResourceCandidates']}
    source_maps={key:{r['id']:r for r in values} for key,values in collections.items()}
    binding_keys=set()
    for binding in data['sourceBindings']:
        collection=binding['sourceCollection'];sid=binding['sourceId'];rid=binding['resourceId']
        require(collection in source_maps and sid in source_maps[collection],'Unresolved source binding')
        require(rid in by_id,'Unresolved source output')
        require(not binding['runtimeEnabled'] and binding['quantityPerAction'] is None,'Unreviewed source activated or assigned a yield')
        require(binding['requiresProcessing']==(by_id[rid]['stage']!='raw'),'Processing-stage mismatch')
        key=(collection,sid,rid)
        require(key not in binding_keys,'Duplicate source binding');binding_keys.add(key)
        source=source_maps[collection][sid]
        if collection=='geologicalResourceCandidates':require(source.get('extractedResourceId')==rid,'Geological inverse link missing')
        else:
            products=source.get('products' if collection=='agriculturalCropCandidates' else 'potentialProducts') or []
            require(any(p.get('resourceId')==rid for p in products),'Source inverse product link missing')
    # Every declared forward product must have a matching binding; unbound candidates remain unresolved.
    for collection,sources in collections.items():
        for source in sources:
            if collection=='geologicalResourceCandidates':
                require((collection,source['id'],source['extractedResourceId']) in binding_keys,'Missing geology binding')
            else:
                for product in source.get('products' if collection=='agriculturalCropCandidates' else 'potentialProducts') or []:
                    if product.get('resourceId'):require((collection,source['id'],product['resourceId']) in binding_keys,'Missing product binding')
    mappings={m['sourceTag']:m for m in data['sourceTagMappings']}
    animal_tags={p['resourceTag'] for a in animals['speciesCandidates'] for p in a.get('potentialProducts') or []}
    require(set(mappings)==animal_tags,'Animal source tag coverage mismatch')
    for tag,mapping in mappings.items():
        require(all(r in by_id for r in mapping['resourceIds']),'Unresolved animal tag mapping')
        if mapping['targetKind']!='resource':require(not mapping['resourceIds'],'Services or ambiguous anatomy grant material')
        for animal in animals['speciesCandidates']:
            for product in animal.get('potentialProducts') or []:
                if product['resourceTag']==tag:
                    if mapping['targetKind']=='resource':require(product.get('resourceId') in mapping['resourceIds'],'Animal mapping mismatch')
                    else:require('resourceId' not in product,'Ambiguous product or service incorrectly mapped')
    process_tags=set();graph={rid:set() for rid in by_id}
    for process in data['processingLinks']:
        require(process['processTag'] not in process_tags,'Duplicate processTag');process_tags.add(process['processTag'])
        require(process['inputResourceIds'] and process['outputResourceIds'],'Missing process endpoints')
        require(all(r in by_id for r in process['inputResourceIds']+process['outputResourceIds']),'Unresolved process resource')
        require(not process['runtimeEnabled'] and process['recipeId'] is None,'Guide incorrectly enabled as recipe')
        for field in ['requiredTechnologyIds','inputQuantities','outputQuantities','facilities','byproducts']:
            require(process[field] is None,'Unreviewed recipe parameters populated')
        for source in process['inputResourceIds']:graph[source].update(process['outputResourceIds'])
    visited=set();active=set()
    def visit(rid):
        require(rid not in active,'Unexpected cycle in initial resource process guide')
        if rid in visited:return
        active.add(rid)
        for target in graph[rid]:visit(target)
        active.remove(rid);visited.add(rid)
    for rid in graph:visit(rid)
    for source in data['unresolvedSources']:require(source['resourceId'] in by_id,'Unknown unresolved resource')
    expected={'resourceCount':len(by_id),'sourceBindingCount':len(binding_keys),'processingLinkCount':len(process_tags),'sourceTagMappingCount':len(mappings),'geologicalSourceCount':len(minerals['geologicalResourceCandidates']),'cropSourceCount':len(plants['agriculturalCropCandidates'])}
    require(expected==data['summary'],'Resource summary mismatch')
    return expected


if __name__=='__main__':
    print('Validated resource references and boundaries: '+json.dumps(validate_resources()))
