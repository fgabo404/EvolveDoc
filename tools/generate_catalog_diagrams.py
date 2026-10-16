"""Generate complete catalog reference diagrams without changing game definitions."""
import argparse
from collections import Counter
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'


def read(path):return json.loads((ROOT/path).read_text())


def label(value):
    return str(value).replace('"', "'").replace('\n',' ').replace('`','')


def node(identifier,text):return f'    {identifier}["{label(text)}"]'


def mermaid(lines,direction='TD'):
    return '```mermaid\nflowchart '+direction+'\n'+'\n'.join(lines)+'\n```\n'


def table(headers,rows):
    def cell(value):return str(value).replace('|','\\|').replace('\n',' ')
    return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(cell(v) for v in row)+' |\n' for row in rows)


def name(record,lang):return record.get('name',{}).get(lang,record['id'])


def chunks(values,size=4):
    for i in range(0,len(values),size):yield values[i:i+size]


def header(folder,lang,source):
    es=lang=='es'
    title={'world':('World','Mundo'),'animals':('Animals','Animales'),'plants':('Plants','Plantas'),'minerals':('Minerals','Minerales'),'resources':('Resources','Recursos'),'technologies':('Technologies','Tecnologías')}[folder][es]
    text=f'# {title} — '+('Diagramas completos de referencia' if es else 'Complete reference diagrams')+'\n\n'
    text+=('[Índice gráfico](../../lang/es/catalog-diagrams.md)' if es else '[Diagram index](../../lang/en/catalog-diagrams.md)')+' · [English](DIAGRAMS.md) · [Español](DIAGRAMS.es.md)\n\n'
    if source:text+=f'[JSON]({source}) · '+('[Estructura completa del JSON](../../lang/es/json-structures.md)' if es else '[Complete JSON structure](../../lang/en/json-structures.md)')+'\n\n'
    text+=('Todos los registros del catálogo están incluidos. Se usan varios diagramas pequeños en este mismo archivo para facilitar la consulta. Las flechas representan vínculos documentados, no rendimiento, presencia garantizada ni evolución deducida. Los IDs actuales se conservan.\n\n' if es else 'Every catalog record is included. Several small diagrams in this file keep the reference readable. Arrows represent documented links, not yield, guaranteed presence or inferred evolution. Existing IDs are preserved.\n\n')
    return text


def condition_tree(expression,lang,lines,prefix):
    es=lang=='es';counter=[0]
    def emit(value):
        identifier=prefix+str(counter[0]);counter[0]+=1
        if 'all' in value or 'any' in value:
            operator='all' if 'all' in value else 'any';children=value[operator]
            if not children:
                lines.append(node(identifier, 'none — all: []' if operator=='all' else 'INVALID — any: []'))
            else:
                lines.append(node(identifier,('TODOS' if es else 'ALL') if operator=='all' else ('AL MENOS UNO' if es else 'ANY')))
                for child in children:
                    child_id=emit(child);lines.append(f'    {child_id} --> {identifier}')
        else:
            tech=value.get('technologyId');scope=value.get('scope')
            title=(tech+' / '+scope) if tech else value['type']
            lines.append(node(identifier,title))
        return identifier
    return emit(expression)


def technologies(lang,data):
    es=lang=='es';text=header('technologies',lang,'agriculture.technologies.json')
    techs=data['technologies'];by_id={t['id']:t for t in techs};external=data['externalReferences']['technologyIds']
    text+=('## Índice de las 23 tecnologías\n\n' if es else '## Index of all 23 technologies\n\n')
    text+=table(['order','id','Nombre' if es else 'Name','scope'],[(t['order'],f"[{t['id']}](#technology-{t['id']})",name(t,lang),t['scope']) for t in techs])+'\n'
    text+=('`order` solo ordena la presentación. `ALL` exige todos los requisitos; `ANY` acepta cualquiera. `current_species` se refiere a la misma especie y `any_species` a alguna especie de esa civilización. Los requisitos externos están declarados, todavía no implementados aquí.\n\n' if es else '`order` is display order only. `ALL` requires every input; `ANY` accepts any input. `current_species` refers to the same species and `any_species` to any species of that civilization. External prerequisites are declared but not implemented here.\n\n')
    for tech in techs:
        text+=f"## Technology {tech['id']}\n\n**{name(tech,lang)}** — {tech['description'][lang]}\n\n"
        lines=[]
        # Exact boolean grammar: retaining all/any matters more than an unqualified dependency arrow.
        root=condition_tree(tech['prerequisites'],lang,lines,'p')
        lines.append(node('target',f"{tech['order']}. {name(tech,lang)} / {tech['id']}"));lines.append(f'    {root} --> target')
        text+=mermaid(lines)+'\n'
        text+=table(['Campo' if es else 'Field','Valor' if es else 'Value'],[
            ('scope',tech['scope']),('research.mode',tech['research']['mode']),('research.cost',str(tech['research']['cost'])+' '+tech['research']['pointUnit']),('research.onConditionFailure',tech['research']['onConditionFailure']),('effects',', '.join(f"{e['type']}: {e['capabilityId']} ({e['scope']}; {e['activation']})" for e in tech['effects']))])+'\n'
        # Typed condition leaves retain every parameter in tables, including nested all/any context.
        rows=[]
        def collect(expression,path):
            if 'all' in expression or 'any' in expression:
                op='all' if 'all' in expression else 'any'
                if not expression[op]:rows.append((path+'.'+op,'[]'))
                for i,child in enumerate(expression[op]):collect(child,f'{path}.{op}[{i}]')
            else:rows.append((path,'`'+json.dumps(expression,ensure_ascii=False,separators=(',',':'))+'`'))
        for key in ['startConditions','ongoingConditions']:collect(tech['research'][key],'research.'+key)
        collect(tech['usageConditions'],'usageConditions')
        text+=table(['Condición' if es else 'Condition','Expresión exacta' if es else 'Exact expression'],rows)+'\n'
        if tech['eurekas']:
            text+=('### Eurekas\n\n')
            text+=table(['id','eventType','filters','counter','reward','repeatable'],[(e['id'],e['eventType'],'`'+json.dumps(e['filters'],ensure_ascii=False)+'`','`'+json.dumps(e['counter'])+'`','`'+json.dumps(e['reward'])+'`',str(e['repeatable']).lower()) for e in tech['eurekas']])+'\n'
        else:text+=('**Eurekas:** none.\n\n')
        for note in tech.get('designNotes',[]):text+='> '+note+'\n\n'
    text+=('## Importaciones externas\n\n' if es else '## External imports\n\n')
    text+='\n'.join('- `'+i+'`' for i in external)+'\n\n'
    text+=('La configuración raíz también documenta políticas globales, alternativas de fabricación y manejadores. Consultar su [referencia completa](../../lang/es/json/data--technologies--agriculture.technologies.md). Investigar no produce materiales automáticamente.\n' if es else 'Root configuration also documents global policies, manufacturing alternatives and handlers. See its [complete reference](../../lang/en/json/data--technologies--agriculture.technologies.md). Research does not automatically produce materials.\n')
    return text


def candidate_catalog(folder,lang,data,world):
    es=lang=='es';mineral=folder=='minerals';key='geologicalResourceCandidates' if mineral else 'speciesCandidates';records=data[key]
    source=f'{folder}.catalog.guide.json';text=header(folder,lang,source)
    text+=('Candidatos sin taxonomía, ecología, productos o procesos definitivos. Solo se dibujan relaciones existentes. Las etiquetas de productos potenciales no son IDs de recursos ni cantidades producidas.\n\n' if es else 'Candidates do not have finalized taxonomy, ecology, products or processes. Only existing relationships are drawn. Potential product tags are not resource IDs or confirmed production quantities.\n\n')
    variants={v['id']:v for v in world['regionalVariants']};biomes={b['id']:b for b in world['biomes']}
    occurrences=[o for o in world['resourceOccurrences'] if o['definitionId'] in {r['id'] for r in records}]
    text+=('## Inventario completo\n\n' if es else '## Complete inventory\n\n')
    text+=table(['id','Nombre' if es else 'Name'],[(r['id'],name(r,lang)) for r in records])+'\n'
    text+=('## Relaciones de todos los candidatos\n\n' if es else '## Relationships for every candidate\n\n')
    for group_index,group in enumerate(chunks(records),1):
        text+=f'### '+('Grupo' if es else 'Group')+f' {group_index}\n\n';lines=[];defined=set();edges=set()
        def define(identifier,title):
            if identifier not in defined:lines.append(node(identifier,title));defined.add(identifier)
        for i,record in enumerate(group):
            rid=f'c{i}';define(rid,name(record,lang)+' / '+record['id'])
            relevant=[o for o in occurrences if o['definitionId']==record['id']]
            for occurrence in relevant:
                vid=occurrence['variantId'];variant=variants[vid];bid=variant['biomeId']
                vn='v'+str(list(variants).index(vid));bn='b'+str(list(biomes).index(bid))
                define(vn,name(variant,lang)+' / '+vid);define(bn,name(biomes[bid],lang)+' / '+bid)
                edges.add((rid,vn,'source occurrence'));edges.add((vn,bn,'biomeId'))
            for j,product in enumerate(record.get('potentialProducts') or []):
                pid=f'o{i}_{j}';define(pid,product['resourceTag']+' / potential');edges.add((rid,pid,'potentialProducts'))
        for a,b,k in sorted(edges):lines.append(f'    {a} -->|{k}| {b}')
        text+=mermaid(lines,'LR')+'\n'
    if folder=='plants':
        crops=data['agriculturalCropCandidates'];text+=('## Todos los candidatos agrícolas\n\n' if es else '## All agricultural candidates\n\n')
        text+=('Son grupos agrícolas pendientes de especie exacta y ancestro; no se fusionan automáticamente con candidatos regionales.\n\n' if es else 'These are crop groups awaiting exact species and ancestors; they are not automatically merged with regional candidates.\n\n')
        for number,group in enumerate(chunks(crops),1):
            text+=f'### '+('Cultivos' if es else 'Crops')+f' {number}\n\n';lines=[];tags={}
            lines.append(node('tech','species_cultivation'))
            for i,crop in enumerate(group):
                lines.append(node('c'+str(i),name(crop,lang)+' / '+crop['id']));lines.append(f'    c{i} -->|cultivationResearch.technologyId| tech')
                tag=crop['cropUseTag']
                if tag not in tags:tags[tag]='g'+str(len(tags));lines.append(node(tags[tag],tag))
                lines.append(f'    c{i} -->|cropUseTag| {tags[tag]}')
            text+=mermaid(lines,'LR')+'\n'
        text+=table(['id','Nombre' if es else 'Name','cropUseTag','sourceOriginHint'],[(c['id'],name(c,lang),c['cropUseTag'],c['sourceOriginHint']) for c in crops])+'\n'
    text+=('## Todas las apariciones de la fuente\n\n' if es else '## Every source occurrence\n\n')
    text+=('Esta tabla conserva cada vínculo regional y método de extracción aunque el diagrama agrupe flechas repetidas. La presencia inicial sigue deshabilitada.\n\n' if es else 'This table retains every regional link and extraction method even when diagrams combine repeated arrows. Initial spawning remains disabled.\n\n')
    text+=table(['id','definitionId','biomeId','variantId','extractionMethodId','sourceText'],[(o['id'],o['definitionId'],o['biomeId'],o['variantId'],o.get('extractionMethodId','—'),o['sourceText']) for o in occurrences])+'\n'
    return text


def world_catalog(lang,world):
    es=lang=='es';text=header('world',lang,'world.catalog.guide.json')
    text+=('## Todos los biomas y variantes\n\n' if es else '## All biomes and variants\n\n')
    text+=('Las cantidades son registros del documento, no poblaciones o depósitos ya generados. La distribución regional exacta y la probabilidad siguen pendientes.\n\n' if es else 'Counts describe source listings, not generated populations or deposits. Exact native distribution and spawn probabilities remain unresolved.\n\n')
    for biome in world['biomes']:
        text+=f"### {name(biome,lang)} / `{biome['id']}`\n\n";lines=[node('biome',name(biome,lang)+' / '+biome['id'])]
        for i,variant in enumerate(v for v in world['regionalVariants'] if v['biomeId']==biome['id']):
            lines.append(node(f'v{i}',name(variant,lang)+' / '+variant['id']));lines.append(f'    v{i} -->|biomeId| biome')
            count=Counter(o['kind'] for o in world['resourceOccurrences'] if o['variantId']==variant['id'])
            for j,(kind,amount) in enumerate(sorted(count.items())):
                lines.append(node(f'o{i}_{j}',f'{kind}: {amount} source occurrences'));lines.append(f'    o{i}_{j} -->|variantId| v{i}')
        text+=mermaid(lines,'LR')+'\n'
    for key in ['worldRules','summary']:
        text+=f'## `{key}`\n\n'+table(['Campo' if es else 'Field','Valor' if es else 'Value'],[(k,'`'+json.dumps(v,ensure_ascii=False)+'`') for k,v in world[key].items()])+'\n'
    for key in ['elevationLevels','geographicModifiers']:
        text+=f'## `{key}`\n\n'+table(['id','Nombre' if es else 'Name','Reglas adicionales' if es else 'Additional rules'],[(str(v['id']),name(v,lang),'`'+json.dumps({k:x for k,x in v.items() if k not in ['id','name']},ensure_ascii=False)+'`') for v in world[key]])+'\n'
    text+=('## Orden de generación propuesto\n\n' if es else '## Proposed generation order\n\n')
    text+='\n'.join(f'{i}. `{step}`' for i,step in enumerate(world['generationPipeline'],1))+'\n\n'
    text+=('Las 485 apariciones individuales están completas en los archivos de [plantas](../plants/DIAGRAMS.es.md), [animales](../animals/DIAGRAMS.es.md) y [minerales](../minerals/DIAGRAMS.es.md), sin duplicar todo el inventario aquí. Las políticas de casillas, yacimientos y revisión están en la [estructura completa](../../lang/es/json/data--world--world.catalog.guide.md).\n' if es else 'All 485 individual occurrences are retained in the [plants](../plants/DIAGRAMS.md), [animals](../animals/DIAGRAMS.md) and [minerals](../minerals/DIAGRAMS.md) files without repeating the complete inventory here. Tile/deposit and review policies are in the [complete structure](../../lang/en/json/data--world--world.catalog.guide.md).\n')
    return text


def documents():
    world=read('data/world/world.catalog.guide.json');tech=read('data/technologies/agriculture.technologies.json');output={}
    for lang in ['en','es']:
        es=lang=='es';filename='DIAGRAMS.es.md' if es else 'DIAGRAMS.md'
        output[f'data/technologies/{filename}']=technologies(lang,tech)
        output[f'data/world/{filename}']=world_catalog(lang,world)
        for folder in ['plants','animals','minerals']:
            output[f'data/{folder}/{filename}']=candidate_catalog(folder,lang,read(f'data/{folder}/{folder}.catalog.guide.json'),world)
        output[f'data/resources/{filename}']=header('resources',lang,None)+( 'No existe un JSON de recursos todavía. Madera, piedra y grano son ejemplos de recursos futuros, no definiciones ya implementadas. No se dibujan productos, recetas ni rendimientos inventados. El catálogo tendrá su diagrama completo cuando se definan sus registros.\n' if es else 'No resource JSON exists yet. Wood, stone and grain are examples of future resources, not implemented definitions. No invented outputs, recipes or yields are drawn. A complete catalog diagram will accompany its definitions.\n')
        index=('# Diagramas completos por catálogo\n\n' if es else '# Complete diagrams by catalog\n\n')
        index+=('Un archivo específico junto a cada JSON, dividido en diagramas pequeños. GitHub los representa en la vista normal del Markdown.\n\n' if es else 'One dedicated file beside each catalog JSON, divided into small diagrams. GitHub renders them in the normal Markdown view.\n\n')
        for folder in ['technologies','world','plants','animals','minerals','resources']:
            index+=f'- [{folder}](../../data/{folder}/{filename})\n'
        index+=('\nCobertura actual: 23 tecnologías, 9 importaciones tecnológicas, 7 biomas, 27 variantes regionales, 129 candidatos vegetales, 134 animales, 57 geológicos, 21 candidatos agrícolas y las 485 apariciones de la fuente. Recursos sigue sin catálogo.\n\nLos diagramas muestran relaciones; las tablas que los acompañan conservan parámetros y apariciones repetidas. No inventan evolución biológica, domesticación, productos ni procesamiento. Las estructuras campo por campo siguen en la [referencia de JSON](json-structures.md).\n' if es else '\nCurrent coverage: 23 technologies, 9 external technology imports, 7 biomes, 27 regional variants, 129 plant candidates, 134 animal candidates, 57 geological candidates, 21 crop candidates and all 485 source occurrences. Resources has no catalog yet.\n\nDiagrams show relationships; accompanying tables retain parameters and repeated occurrences. They do not invent biological evolution, domestication, outputs or processing. Field-by-field structures remain in the [JSON reference](json-structures.md).\n')
        index+=('\nActualizar con `python tools/generate_catalog_diagrams.py`; verificar con `--check`.\n' if es else '\nUpdate with `python tools/generate_catalog_diagrams.py`; verify with `--check`.\n')
        output[f'lang/{lang}/catalog-diagrams.md']=index
    return {path: content.rstrip()+'\n' for path,content in output.items()}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();outdated=[]
    for relative,content in documents().items():
        path=ROOT/relative
        if args.check:
            if not path.exists() or path.read_text()!=content:outdated.append(relative)
        else:path.write_text(content,encoding='utf-8')
    if outdated:raise SystemExit('Missing or outdated catalog diagrams: '+', '.join(outdated))
    print(('Checked' if args.check else 'Generated')+' 12 catalog diagram files and 2 bilingual indexes.')


if __name__=='__main__':main()
