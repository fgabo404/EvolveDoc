"""Check animal material/acquisition contracts; not a biological or simulation proof."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT/path).read_text())


def require(value,message):
    if not value:
        raise ValueError(message)


def validate_animal_products():
    a=read('data/animals/animals.catalog.guide.json');r=read('data/resources/resources.catalog.guide.json')
    resources={x['id']:x for x in r['resources']};processes={x['processTag']:x for x in r['processingLinks']}
    evidence={x['sourceKey'] for x in a['productEvidenceSources']};methods={x['tag']:x for x in a['acquisitionMethods']}
    require(len(methods)==len(a['acquisitionMethods']),'Duplicate acquisition method')
    require(len(evidence)==len(a['productEvidenceSources']),'Duplicate product evidence key')
    outcomes={'requires_dead_animal','consumes_animal','preserves_animal','collects_discarded_material','removes_egg_without_killing_adult'}
    for method in methods.values():
        require(method['sourceOutcome'] in outcomes and method['runtimeEnabled'] is False,'Invalid/executable method')
        for field in ['name','description']:
            require(set(method[field])=={'en','es'} and all(method[field].values()),'Missing method localization')
    bindings={(b['sourceId'],b['resourceId']):b for b in r['sourceBindings'] if b['sourceCollection']=='animalSpeciesCandidates'}
    associations=set()
    for animal in a['speciesCandidates']:
        products=animal['potentialProducts'];tags={p['resourceTag'] for p in products}
        require(products and len(tags)==len(products),'Missing/duplicate animal product')
        require(animal['anatomicalGroup'] in ['mammal','bird','fish','reptile','shellfish'],'Unknown anatomy group')
        require(not {'horns','antlers'}<=tags,'Both horns and antlers granted')
        require('antlers_or_horns' not in tags and not any(t.endswith('_service') for t in tags),'Unresolved anatomy/service in material outputs')
        if animal['anatomicalGroup']=='shellfish':require(not {'bones','hide','milk','antlers','horns'}&tags,'Vertebrate material assigned to shellfish')
        if animal['anatomicalGroup']!='mammal':require('milk' not in tags,'Nonmammal dairy output')
        if animal['anatomicalGroup']=='bird':require({'meat','bones','feathers','eggs'}<=tags,'Incomplete bird material coverage')
        for p in products:
            rid=p['resourceId'];require(rid in resources and resources[rid]['tag']==p['resourceTag'],'Material tag/ID mismatch')
            require(p['acquisitionMethodTags'] and set(p['acquisitionMethodTags'])<=methods.keys(),'Unresolved acquisition method')
            require(p['evidenceSourceKeys'] and set(p['evidenceSourceKeys'])<=evidence,'Unresolved material evidence')
            require(set(p['notes'])=={'en','es'} and all(p['notes'].values()),'Missing product localization')
            require(p['yield'] is None and p['requiredTechnologyIds'] is None,'Unapproved yield/technology assigned')
            key=(animal['id'],rid);require(key not in associations,'Duplicate animal/resource association');associations.add(key)
            require(key in bindings,'Missing material binding')
            binding=bindings[key];process=p['processingTag']
            require(binding['processingTag']==process,'Product/binding process mismatch')
            if resources[rid]['stage']!='raw':
                require(process in processes and rid in processes[process]['outputResourceIds'],'Processed output lacks matching process guide')
                require('input_from_same_animal' in p['availabilityConstraints'],'Processed output lost animal provenance')
                require(processes[process].get('inputProvenancePolicy'),'Missing input provenance restriction')
            else:require(process is None,'Raw resource has processed-output tag')
            selected=[methods[t] for t in p['acquisitionMethodTags']]
            if p['resourceTag'] in ['meat','fish_meat','bones','animal_fat','hide','raw_tendons','horns','tusks','baleen']:
                require(all(m['sourceOutcome'] in ['requires_dead_animal','consumes_animal'] for m in selected),'Living animal loses body tissue')
            if p['resourceTag']=='horns':require('collect_shed_antlers' not in p['acquisitionMethodTags'],'Horns treated as shed antlers')
            if p['resourceTag']=='milk':require('managed_lactating_female' in p['availabilityConstraints'] and p['acquisitionMethodTags']==['milking'],'Unconditional milk output')
            if p['resourceTag']=='pearls':require({'pearl_bearing_individual','pearl_actually_present'}<=set(p['availabilityConstraints']),'Guaranteed pearl assigned')
            if p['resourceTag']=='baleen':require('baleen_whale_member' in p['availabilityConstraints'],'Baleen granted to all whales')
            if p['resourceTag']=='eggs' and animal['anatomicalGroup']=='mammal':require('egg_laying_female' in p['availabilityConstraints'],'Ordinary mammal granted eggs')
    require(associations==bindings.keys(),'Orphan animal source binding')
    entities={x['id'] for x in a['speciesCandidates']}
    for service in a['serviceUseCandidates']:
        require(service['entityId'] in entities and service['runtimeEnabled'] is False,'Invalid/executable animal service')
        require(service['serviceTag'].endswith('_service'),'Material incorrectly separated as service')
    expected={'animalEntityCount':len(entities),'materialLinkCount':len(associations),'acquisitionMethodCount':len(methods),'serviceCandidateCount':len(a['serviceUseCandidates'])}
    require(expected==a['productCoverage'],'Animal product coverage mismatch')
    return expected


if __name__=='__main__':
    print('Validated animal material/acquisition reference: '+json.dumps(validate_animal_products()))
