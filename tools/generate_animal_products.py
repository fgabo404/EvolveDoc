"""Generate complete bilingual animal/material acquisition tables from current definitions."""
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT/path).read_text())


def cell(value):
    return str(value).replace('|',r'\|').replace('\n',' ')


def documents():
    a=read('data/animals/animals.catalog.guide.json');r=read('data/resources/resources.catalog.guide.json')
    resources={x['id']:x for x in r['resources']};methods={x['tag']:x for x in a['acquisitionMethods']}
    out={}
    for lang in ['en','es']:
        es=lang=='es'
        text=('# Animales: materiales y obtención' if es else '# Animals: materials and acquisition')+'\n\n'
        text+=('[Modelo y límites]' if es else '[Model and boundaries]')+f'(../../lang/{lang}/animal-products.md) · [JSON](animals.catalog.guide.json)\n\n'
        text+=('Las 101 entidades se mantienen generales. Se registran materiales útiles según anatomía, no una promesa de igual rendimiento, alimento apto o aprovechamiento histórico habitual de cada animal. Cantidades, tiempos, regeneración, costes y reglas ejecutables siguen pendientes. No se requieren especies científicas nuevas.\n\n' if es else 'All 101 entities retain their gameplay identity. Materials reflect useful anatomy, not equal yields, food suitability or routine historical harvesting of every animal. Quantities, durations, regeneration, costs and executable rules remain pending. No additional scientific species are required.\n\n')
        text+=('La misma materia puede aparecer en dos columnas si tiene métodos alternativos: no duplica el material. Las columnas muestran posibilidades de obtención; la disponibilidad real respeta las condiciones del JSON.\n\n' if es else 'The same material may appear in two columns when alternative methods exist; this does not duplicate it. Columns show acquisition possibilities, while actual availability follows JSON constraints.\n\n')
        text+=('| Entidad | ID | Del cuerpo muerto o consumido | En vida o material desprendido | Derivados que requieren proceso |\n' if es else '| Entity | ID | Dead/consumed source | Living/shed collection | Derivatives requiring processing |\n')+'| --- | --- | --- | --- | --- |\n'
        for animal in a['speciesCandidates']:
            dead=[];live=[];processed=[]
            for p in animal['potentialProducts']:
                label=resources[p['resourceId']]['name'][lang]
                if p['processingTag']:processed.append(label);continue
                outcomes={methods[t]['sourceOutcome'] for t in p['acquisitionMethodTags']}
                if outcomes & {'requires_dead_animal','consumes_animal'}:dead.append(label)
                if outcomes - {'requires_dead_animal','consumes_animal'}:live.append(label)
            text+=f"| {cell(animal['name'][lang])} | `{animal['id']}` | {cell(', '.join(dead))} | {cell(', '.join(live)) or '—'} | {cell(', '.join(processed)) or '—'} |\n"
        text+=('\n## Métodos de obtención\n\nSon operaciones materiales de referencia, no una decisión sobre cuántos clics/acciones tendrá la interfaz ni recetas implementadas.\n\n' if es else '\n## Acquisition methods\n\nThese describe material handling, not the future number of UI actions or implemented recipes.\n\n')
        text+='| Tag | '+('Método | Efecto sobre la fuente | Detalle' if es else 'Method | Source outcome | Detail')+' |\n| --- | --- | --- | --- |\n'
        for m in methods.values():text+=f"| `{m['tag']}` | {cell(m['name'][lang])} | `{m['sourceOutcome']}` | {cell(m['description'][lang])} |\n"
        text+=('\n## Condiciones por producto\n\nEstas etiquetas en inglés expresan restricciones del diseño; todavía no son condiciones ejecutables del motor. Una fila es una asociación de entidad y recurso, no una cantidad concedida.\n\n' if es else '\n## Per-product conditions\n\nEnglish tags express design constraints, not implemented engine conditions. A row is an entity/resource association, not an awarded quantity.\n\n')
        text+='| '+('Entidad | Material | Métodos | Condiciones | Proceso | Nota' if es else 'Entity | Material | Methods | Constraints | Process | Note')+' |\n| --- | --- | --- | --- | --- | --- |\n'
        for animal in a['speciesCandidates']:
            for p in animal['potentialProducts']:
                text+=f"| {cell(animal['name'][lang])} | {cell(resources[p['resourceId']]['name'][lang])} | {cell(', '.join(p['acquisitionMethodTags']))} | {cell(', '.join(p['availabilityConstraints'])) or '—'} | `{p['processingTag'] or 'none'}` | {cell(p['notes'][lang])} |\n"
        text+=('\n## Servicios separados de materiales\n\nSon candidatos históricos/de manejo pendientes, no habilidades concedidas por encontrar al animal. No son materiales de inventario.\n\n' if es else '\n## Services separate from materials\n\nThese are historical/husbandry candidates still under review, not abilities granted by finding the animal. They are not inventory materials.\n\n')
        text+='| entityId | serviceTag | status |\n| --- | --- | --- |\n'
        for service in a['serviceUseCandidates']:text+=f"| `{service['entityId']}` | `{service['serviceTag']}` | `{service['status']}` |\n"
        text+=('\n## Referencias consultadas\n\nLas fuentes respaldan anatomía o usos materiales generales. La selección de productos útiles para cada categoría es una decisión de diseño, sin afirmar prácticas industriales o ganaderas para todas las especies representadas.\n\n' if es else '\n## Consulted references\n\nSources support anatomy or general material uses. Useful output selections for gameplay categories are design decisions, not claims of industrial or husbandry practices across every represented species.\n\n')
        for source in a['productEvidenceSources']:text+=f"- `{source['sourceKey']}` — [{source['title']}]({source['url']}).\n"
        text+='\n`python tools/generate_animal_products.py` / `--check`\n'
        out['data/animals/PRODUCTS'+('.es' if es else '')+'.md']=text
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    for relative,text in documents().items():
        path=ROOT/relative
        if args.check:
            if not path.exists() or path.read_text()!=text:raise SystemExit('Outdated animal products reference: '+relative)
        else:path.write_text(text)
    print(('Checked' if args.check else 'Generated')+' 2 animal material/acquisition references.')


if __name__=='__main__':main()
