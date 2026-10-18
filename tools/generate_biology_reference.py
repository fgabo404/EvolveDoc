"""Generate bilingual full taxon mappings, form tables and compact lineage references."""
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT/path).read_text())


def cell(value):
    return str(value).replace('|',r'\|').replace('\n',' ')


def documents():
    out={}
    for folder in ['plants','animals']:
        data=read(f'data/{folder}/{folder}.biological.catalog.json')
        guide=read(f'data/{folder}/{folder}.catalog.guide.json')
        taxa={x['id']:x for x in data['taxa']};forms={x['id']:x for x in data['biologicalForms']}
        for lang in ['en','es']:
            es=lang=='es';filename='BIOLOGY.es.md' if es else 'BIOLOGY.md'
            text=('# Referencia científica opcional' if es else '# Optional scientific reference')+'\n\n'
            text+=('**Las entidades del juego son categorías generales. Esta referencia científica no exige separar zorros, osos o robles en especies.**\n\n' if es else '**Gameplay entities are general categories. This scientific reference does not require splitting foxes, bears or oaks into species.**\n\n')
            text+=f'[JSON]({folder}.biological.catalog.json) · '+('[Modelo y límites]' if es else '[Model and boundaries]')+f'(../../lang/{lang}/biology.md)\n\n'
            text+=('Nombres científicos cotejados con el proveedor; las selecciones representativas, regiones nativas, hábitat y productos siguen pendientes de revisión. Los IDs retirados conservan su procedencia mediante alias explícitos. Ninguna tabla autoriza apariciones iniciales ni transformaciones del juego. Las formas de referencia relacionadas no son una lista de aparición silvestre.\n\n' if es else 'Scientific names matched to the provider; representative choices, native ranges, habitats and outputs still need review. Retired source IDs are preserved through explicit aliases. No table authorizes initial spawning or gameplay transformations. Related reference forms are not a wild-spawn list.\n\n')
            text+=('## Cobertura\n\n' if es else '## Coverage\n\n')
            text+='| Metric | Count |\n| --- | --- |\n'+''.join(f'| `{k}` | {v} |\n' for k,v in data['summary'].items())
            text+=('\n## Etiquetas originales y selección concreta\n\n' if es else '\n## Original labels and concrete selection\n\n')
            text+=('| Candidato | Nombre de referencia | Taxones elegidos | Selección | Formas relacionadas |\n' if es else '| Candidate | Reference name | Selected taxa | Selection | Related forms |\n')+'| --- | --- | --- | --- | --- |\n'
            for c in guide['speciesCandidates']+guide.get('agriculturalCropCandidates',[]):
                res=c['taxonResolution'];names='; '.join(f"`{i}` {taxa[i]['name'][lang]}" for i in res['taxonIds'])
                text+=f"| `{c['id']}` | {cell(c['name'][lang])} | {cell(names)} | `{res['selectionMode']}` | "+', '.join(f'`{f}`' for f in res['formIds'])+' |\n'
            text+=('\n## Registro completo de taxones\n\nLos nombres latinos son los mismos en ambos idiomas. `SUBSPECIES` no se presenta como especie nueva. El nombre con autor y la evidencia de sinónimos se conservan completos en JSON.\n\n' if es else '\n## Complete taxon registry\n\nLatin names are identical across languages. A `SUBSPECIES` is not presented as a new species. Full names with authority and synonym evidence remain in JSON.\n\n')
            text+='| ID | Tag | Scientific name | Rank | Group | Provider |\n| --- | --- | --- | --- | --- | --- |\n'
            for t in taxa.values():
                tax=t['taxonomy'];text+=f"| `{t['id']}` | `{t['tag']}` | {cell(t['scientificName'])} | `{t['taxonRank']}` | `{t['organismGroup']}` | [{tax['provider']} {tax['providerTaxonKey']}]({tax['referenceUrl']}) |\n"
            text+=('\n## Formas biológicas\n\nUna forma cultivada de referencia no afirma por sí sola una domesticación histórica demostrada, ni equivale a un cultivar o raza con nombre.\n\n' if es else '\n## Biological forms\n\nA cultivated reference form does not by itself assert a proven historical domestication event or identify a named cultivar or breed.\n\n')
            text+='| ID | Name | Taxon | Kind | Literature name | Evidence |\n| --- | --- | --- | --- | --- | --- |\n'
            for f in forms.values():
                text+=f"| `{f['id']}` | {cell(f['name'][lang])} | `{f['taxonId']}` | `{f['formKind']}` | {cell(f['literatureName'])} | "+', '.join(f['evidenceSourceKeys'])+' |\n'
            text+=('\n## Relaciones documentadas\n\nLas relaciones describen historia biológica, no niveles obligatorios ni recetas. En `hybrid_origin`, todos los padres indicados aportan conjuntamente. La introgresión es flujo génico, distinto de domesticación. No se resuelven poblaciones fundadoras exactas.\n\n' if es else '\n## Documented relationships\n\nRelations describe biological history, not mandatory levels or recipes. In `hybrid_origin`, all listed parents jointly contribute. Introgression is gene flow, distinct from domestication. Exact founding populations are not resolved.\n\n')
            text+='| Type | Parent forms | Child forms | Interpretation | Evidence |\n| --- | --- | --- | --- | --- |\n'
            for r in data['lineageRelations']:
                def labels(ids):return '; '.join(f"`{i}` {forms[i]['name'][lang]}" for i in ids)
                text+=f"| `{r['relationType']}` | {cell(labels(r['parentFormIds']))} | {cell(labels(r['childFormIds']))} | {cell(r['description'][lang])} | "+', '.join(r['evidenceSourceKeys'])+' |\n'
            # Connected components combine branches; two-node relations remain in the exact table above.
            neighbors={f:set() for f in forms}
            for r in data['lineageRelations']:
                endpoints=r['parentFormIds']+r['childFormIds']
                for f in endpoints:neighbors[f].update(set(endpoints)-{f})
            seen=set();groups=[]
            for start in neighbors:
                if start in seen:continue
                stack=[start];component=set()
                while stack:
                    f=stack.pop()
                    if f in component:continue
                    component.add(f);stack.extend(neighbors[f]-component)
                seen.update(component)
                if len(component)>=3:groups.append(component)
            for n,component in enumerate(groups,1):
                text+=('\n### Rama relacionada ' if es else '\n### Related branch ')+str(n)+'\n\n```mermaid\nflowchart TD\n'
                node={i:'f'+i.split('#')[1] for i in sorted(component)}
                for i,name in node.items():
                    label=forms[i]['name'][lang].replace('"',"'")
                    text+=f'  {name}["{label}"]\n'
                for r in data['lineageRelations']:
                    if not set(r['parentFormIds']+r['childFormIds'])<=component:continue
                    for p in r['parentFormIds']:
                        for c in r['childFormIds']:
                            text+=f"  {node[p]} -->|{r['relationType']}| {node[c]}\n"
                text+='```\n'
            if data['excludedLineageRelations']:
                text+=('\n## Relaciones directas descartadas\n\n' if es else '\n## Excluded direct relationships\n\n')
                for e in data['excludedLineageRelations']:
                    text+=f"- **{forms[e['parentFormId']]['name'][lang]} → {forms[e['childFormId']]['name'][lang]}:** {e['reason'][lang]} (`"+'`, `'.join(e['evidenceSourceKeys'])+'`).\n'
            used={k for r in data['lineageRelations']+data['excludedLineageRelations']+data['biologicalForms'] for k in r.get('evidenceSourceKeys',[])}
            child_forms={i for r in data['lineageRelations'] for i in r['childFormIds']}
            pending=[f for f in forms.values() if f['formKind'] in ['cultivated_population','domesticated_form'] and f['id'] not in child_forms]
            if pending:
                text+=('\n## Ascendencia sin relación fundadora registrada\n\nEstas formas tienen identidad concreta; su relación fundadora no se ha incorporado. Esto no significa que carezcan de ancestros. Las exclusiones anteriores impiden sustituirlos por un pariente actual sin evidencia.\n\n' if es else '\n## Ancestry without a recorded founding relation\n\nThese forms have concrete identities; their founding relation has not been incorporated. This does not mean they lack ancestors. Exclusions above prevent substituting an extant relative without evidence.\n\n')
                for f in pending:text+=f"- `{f['id']}` — {f['name'][lang]}.\n"
            text+=('\n## Fuentes de las relaciones\n\n' if es else '\n## Relationship sources\n\n')
            for source in data['evidenceSources']:
                if source['sourceKey'] in used:text+=f"- `{source['sourceKey']}` — [{source['title']}]({source['url']}).\n"
            text+=('\nActualizar con `python tools/generate_biology_reference.py`.\n' if es else '\nUpdate with `python tools/generate_biology_reference.py`.\n')
            out[f'data/{folder}/{filename}']=text
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    for name,text in documents().items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_text()!=text:raise SystemExit('Outdated biology reference: '+name)
        else:path.write_text(text)
    print(('Checked' if args.check else 'Generated')+' 4 bilingual biology references.')


if __name__=='__main__':main()
