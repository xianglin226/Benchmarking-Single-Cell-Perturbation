from pathlib import Path
import sys, json, csv, math, re, itertools, hashlib, os, tempfile
ROOT=Path(__file__).resolve().parent
TASK=ROOT.parents[1]
os.environ.setdefault('MPLCONFIGDIR',str(Path(tempfile.gettempdir())/'pertogether-matplotlib'))
if (TASK/'work/graph_libs').exists():sys.path.insert(0,str(TASK/'work/graph_libs'))
import numpy as np
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

BACKBONES={
 'vae':('VAE',3), 'autoencoder':('Autoencoder',1),
 'gnn':('Graph neural network',3), 'transformer':('Transformer',3),
 'denoising_diffusion':('Denoising diffusion',3), 'masked_diffusion':('Masked diffusion',3),
 'diffusion_family':('Generative diffusion family',1),
 'flow_matching':('Flow matching',3), 'normalizing_flow':('Normalizing flow',3),
 'optimal_transport':('Optimal transport',3),'gaussian_process':('Gaussian process',3),
 'gan':('Adversarial generator / GAN',3),'ode_network':('ODE network',3),
 'regulatory_network':('Explicit regulatory-network model',2),
 'factorization':('Low-rank matrix / tensor method',2), 'llm_agent':('LLM agent',3),
 'cnn':('Convolutional neural network',3),'causal_sde':('Causal stochastic dynamics',3),
 'gaussian_copula':('Gaussian copula',3), 'attention':('Attention module',1),
 'compositional_latent':('Additive compositional latent structure',1),
}
MODULES={'attention','compositional_latent'}
GROUPS=[('latent','Autoencoder / latent models','#197c85'),('diffusion','Diffusion / flow models','#8364bc'),('graph','Graph neural networks','#448849'),('transformer','Transformer / attention','#cc7924'),('statistical','Statistical / mechanistic','#4d76ad'),('other','Other models / frameworks','#9d6172')]
COLORS={g:c for g,_,c in GROUPS}
LABELS={g:l for g,l,_ in GROUPS}
raw=json.loads((ROOT/'input_snapshot.json').read_text())
annotations=json.loads((ROOT/'annotations.json').read_text())
assert set(annotations)=={r['name'] for r in raw['models']}
G=nx.Graph();nodes=[]
extra_evidence={
 'PerturbLDM':'https://github.com/davidroad/PerturbLDM',
 'X-Cell':'https://www.cdn.xaira.com/papers/X_CELL_V1_0316_final.pdf',
 'PopPert':'https://arxiv.org/pdf/2609.01357',
 'scDFM':'https://proceedings.iclr.cc/paper_files/paper/2026/file/75f029a1289a47aa99c86588239f0c12-Paper-Conference.pdf'
}
NOTES={
 'Pertpy':'Modular analysis toolkit; no single fixed architecture is assigned.',
 'LCD':'Mechanistic latent causal SDE; not assigned to the denoising/masked generative diffusion family.',
 'biolord':'Disentangled latent-code generator; no VAE posterior is inferred from the name or decoder alone.',
 'PerturbNet':'Normalizing flow is annotated separately from flow-matching training.',
 'MultiPert':'Includes a transcriptomic VAE and a proteomic autoencoder, plus dual attention.',
 'PertAdapt':'Adapter module is annotated; no one backbone is assumed for every supported foundation model.',
 'AlphaCell':'Multi-paradigm world-model framework; alternatives in the conceptual overview are not assigned as one fixed backbone.',
 'PopPert':'Transformer predictor and Gaussian-copula population model (source paper, Fig. 2 and model overview).',
 'scDFM':'Flow matching with a differential Transformer backbone (source paper, Fig. 1).',
 'scBalFlow':'Staged flow matching with Transformer generation (source architecture Fig. 2).',
 'X-Cell':'Masked/remasking diffusion LM with a scGPT-initialized attention backbone; kept distinct from continuous denoising diffusion.',
}
for r in raw['models']:
 name=r['name'];tags=set(annotations[name]);inherited=[]
 for child,parent in [('vae','autoencoder'),('transformer','attention'),('denoising_diffusion','diffusion_family'),('masked_diffusion','diffusion_family')]:
  if child in tags and parent not in tags:tags.add(parent);inherited.append(parent)
 if tags & {'vae','autoencoder','disentangled_latent_generator','conditional_encoder_decoder'}:group='latent'
 elif tags & {'denoising_diffusion','masked_diffusion','flow_matching','normalizing_flow','causal_sde'}:group='diffusion'
 elif 'gnn' in tags:group='graph'
 elif tags & {'transformer','attention'}:group='transformer'
 elif tags & {'factorization','regulatory_network','structural_causal_model','causal_spatial_graph','gaussian_process','optimal_transport','glm','constrained_regression','effect_distribution_model','signature_enrichment'}:group='statistical'
 else:group='other'
 # Main display category for mixed systems, recorded explicitly rather than inferred by community detection.
 if name in ['PerturbLDM','scLDM']:group='diffusion'
 ev=list(dict.fromkeys(r.get('evidence_urls',[r['paper_url']])+([extra_evidence[name]] if name in extra_evidence else [])))
 figure='https://github.com/xianglin226/Benchmarking-Single-Cell-Perturbation/blob/master/model_figures/'+r['figure_file'] if r['figure_file'] else ''
 n={'id':name,'name':name,'year':r['year'],'section':r['section'],'structure_label':r['model_structure'],'tags':sorted(tags),'explicit_tags':annotations[name],'inherited_tags':inherited,'group':group,'paper_url':r['paper_url'],'figure_url':figure,'evidence_urls':ev,'notes':NOTES.get(name,''),'features':r['features']}
 nodes.append(n);G.add_node(name,**{k:(json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v) for k,v in n.items() if k!='id'})

def weight(tag):return BACKBONES.get(tag,('',1))[1]
for a,b in itertools.combinations(nodes,2):
 sa,sb=set(a['tags']),set(b['tags']);shared=sa&sb;eligible=shared&set(BACKBONES)
 if not eligible:continue
 common_backbone=eligible-MODULES
 kind='shared_backbone' if common_backbone else 'shared_module_only'
 score=sum(weight(t) for t in shared)/sum(weight(t) for t in sa|sb)
 reason='; '.join(BACKBONES[t][0] for t in sorted(eligible))
 G.add_edge(a['id'],b['id'],weight=round(score,6),tag_jaccard=round(score,6),shared_weight=sum(weight(t) for t in shared),shared_tags=';'.join(sorted(shared)),shared_core_tags=';'.join(sorted(eligible)),reason=reason,edge_type=kind)
assert G.number_of_nodes()==77
assert not G.has_edge('LCD','scDiff')
assert not G.has_edge('PerturbNet','CellFlow')
assert G.has_edge('scGen','scVIDR') and 'vae' in G['scGen']['scVIDR']['shared_tags']
assert G.has_edge('CellFlow','scDFM') and 'flow_matching' in G['CellFlow']['scDFM']['shared_tags']
assert G.has_edge('GEARS','PDGrapher') and 'gnn' in G['GEARS']['PDGrapher']['shared_tags']
assert not G.has_edge('biolord','scGen')
assert not G.is_directed()
for n in nodes:n['degree']=G.degree(n['id'])
# Fixed seed, weighted spring layout, then deterministic packing of disconnected components.
components=sorted(nx.connected_components(G),key=lambda s:(-len(s),sorted(s)[0]));pos={};others=[]
for ci,comp in enumerate(components):
 if ci==0 and len(comp)>1:
  local=nx.spring_layout(G.subgraph(comp),seed=226,k=1.05/math.sqrt(len(comp)),iterations=1500,weight='weight',scale=1)
  center=np.mean(list(local.values()),axis=0)
  # Radial expansion opens the densely connected center while retaining the spring-layout topology.
  for n in local:
   d=local[n]-center;r=np.linalg.norm(d);local[n]=center+d/max(r,.01)**.32
  ar=np.array(list(local.values()));lo=ar.min(0);hi=ar.max(0)
  for n,p in local.items():pos[n]=np.array([.06+(p[0]-lo[0])/(hi[0]-lo[0])*.88,.10+(p[1]-lo[1])/(hi[1]-lo[1])*.56])
 elif len(comp)>1:others.append(comp)
 else:pass
# Small components and isolated nodes occupy a separate lower strip, with no invented links.
bottom=[]
for comp in others:
 for j,n in enumerate(sorted(comp)):bottom.append((n,ci))
isolates=sorted(nx.isolates(G));bottom_names=[n for n,_ in bottom]+isolates
cols=8;rows=max(1,math.ceil(len(bottom_names)/cols))
for i,n in enumerate(bottom_names):pos[n]=np.array([.07+(i%cols)*.123,.77+(i//cols)*(.19/max(1,rows-1))])
for n in nodes:n['x']=round(float(pos[n['id']][0]),6);n['y']=round(float(pos[n['id']][1]),6)
# Lightweight deterministic label separation in normalized figure coordinates.
labelpos={n:pos[n].copy()+np.array([0,.012]) for n in G}
for _ in range(180):
 moves={n:np.zeros(2) for n in G}
 for a,b in itertools.combinations(G,2):
  p,q=labelpos[a],labelpos[b];wa=(len(a)*.0037+0.014);wb=(len(b)*.0037+.014)
  if abs(p[0]-q[0])<(wa+wb)/2 and abs(p[1]-q[1])<.016:
   dy=.0012 if p[1]>=q[1] else -.0012;moves[a][1]+=dy;moves[b][1]-=dy
 for n in G:
  labelpos[n]+=moves[n]+.025*(pos[n]+np.array([0,.012])-labelpos[n]);labelpos[n]=np.clip(labelpos[n],[.035,.025],[.965,.985])
for n in nodes:n['lx']=round(float(labelpos[n['id']][0]),6);n['ly']=round(float(labelpos[n['id']][1]),6)

def dumpcsv(filename,fieldnames,rows):
 with (ROOT/filename).open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=fieldnames);w.writeheader();w.writerows(rows)
nodefields=['id','year','section','structure_label','group','tags','explicit_tags','inherited_tags','degree','paper_url','figure_url','evidence_urls','notes']
dumpcsv('nodes.csv',nodefields,[{k:(';'.join(n[k]) if isinstance(n[k],list) else n[k]) for k in nodefields} for n in nodes])
lookup={n['id']:n for n in nodes};edges=[]
for a,b,d in G.edges(data=True):
 if a>b:a,b=b,a
 e={'source':a,'target':b,**d,'source_paper':lookup[a]['paper_url'],'target_paper':lookup[b]['paper_url'],'source_figure':lookup[a]['figure_url'],'target_figure':lookup[b]['figure_url']}
 edges.append(e)
edges.sort(key=lambda e:(-e['weight'],e['source'],e['target']))
edgefields=['source','target','weight','tag_jaccard','shared_weight','edge_type','shared_core_tags','shared_tags','reason','source_paper','target_paper','source_figure','target_figure']
dumpcsv('edge_list.csv',edgefields,edges)
dumpcsv('edge_list_backbone.csv',edgefields,[e for e in edges if e['edge_type']=='shared_backbone'])
meta={'created_on':'2026-11-04','input_commit':raw['input_commit'],'nodes':len(nodes),'edges':len(edges),'backbone_edges':sum(e['edge_type']=='shared_backbone' for e in edges),'module_only_edges':sum(e['edge_type']=='shared_module_only' for e in edges),'connected_components':len(components),'isolates':isolates,'scope':'77 methods in root README model tables; scFM and benchmark rows excluded','score':'Weighted Jaccard over curated architecture tags; family weights 3, autoencoder/diffusion parent 1, regulatory/factorization families 2, modules/details 1. Edges require at least one shared eligible family/module.','interpretation':'Annotation-derived structural similarity, not measured functional similarity, performance, inheritance, or publication chronology.'}
(ROOT/'graph.json').write_text(json.dumps({'metadata':meta,'groups':[{'id':g,'label':l,'color':c} for g,l,c in GROUPS],'nodes':nodes,'edges':edges},ensure_ascii=False,indent=2))
(ROOT/'taxonomy.json').write_text(json.dumps({'eligible_tags':{k:{'label':l,'weight':w,'level':'module' if k in MODULES else 'family'} for k,(l,w) in BACKBONES.items()},'parents':{'vae':'autoencoder','transformer':'attention','denoising_diffusion':'diffusion_family','masked_diffusion':'diffusion_family'},'detail_weight':1,'detail_tags':sorted(set(t for n in nodes for t in n['tags'])-set(BACKBONES))},ensure_ascii=False,indent=2))
G.graph.update(created_on='2026-11-04',source_commit=raw['input_commit'],edge_definition=meta['score'])
nx.write_graphml(G,ROOT/'architecture.graphml')
# Standard, editable scientific network figure.
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none','font.size':10})
fig=plt.figure(figsize=(22,17),facecolor='white');ax=fig.add_axes([.025,.055,.95,.82]);ax.set_xlim(0,1);ax.set_ylim(1,0);ax.axis('off')
for a,b,d in G.edges(data=True):
 p,q=pos[a],pos[b];ax.plot([p[0],q[0]],[p[1],q[1]],color='#78909c' if d['edge_type']=='shared_backbone' else '#b5bbc4',alpha=.12+.40*d['weight'] if d['edge_type']=='shared_backbone' else .12,linewidth=.35+1.5*d['weight'],linestyle='-' if d['edge_type']=='shared_backbone' else '--',zorder=1)
for n in nodes:
 x,y=pos[n['id']];ax.scatter([x],[y],s=60+7*math.sqrt(n['degree']),c=COLORS[n['group']],edgecolors='white',linewidths=1,zorder=3)
 lx,ly=labelpos[n['id']]
 if np.linalg.norm(labelpos[n['id']]-pos[n['id']])>.025:ax.plot([x,lx],[y,ly],color='#b8c0c8',linewidth=.45,zorder=2)
 ax.text(lx,ly,n['id'],ha='center',va='top',fontsize=9.5,color='#243447',bbox={'facecolor':'white','alpha':.82,'edgecolor':'none','pad':.8},zorder=4)
ax.axhline(.715,color='#dce1e5',linewidth=.8)
ax.text(.015,.735,'Small components and methods without a matched architecture family',fontsize=11,color='#546675',va='top')
fig.text(.04,.965,'Architecture similarity among perturbation methods',fontsize=23,fontweight='normal',color='#203647')
fig.text(.04,.938,f"77 methods  ·  {len(edges)} shared-structure links  ·  source README {raw['input_commit'][:7]}",fontsize=12,color='#526676')
handles=[Line2D([0],[0],marker='o',color='none',markerfacecolor=c,markersize=8,label=l) for _,l,c in GROUPS]
fig.legend(handles=handles,loc='upper left',bbox_to_anchor=(.034,.922),ncol=3,frameon=False,fontsize=11)
fig.text(.04,.035,'Edges encode shared annotated components. Thickness: weighted tag Jaccard. Dashed: shared modules only. Node color: display group.',fontsize=10,color='#526676')
fig.text(.04,.019,'No direction or model ancestry is implied. Isolated nodes indicate no shared eligible tag in this annotation, not proven structural uniqueness.',fontsize=10,color='#526676')
fig.savefig(ROOT/'architecture_network.svg',facecolor='white');fig.savefig(ROOT/'architecture_network.png',dpi=180,facecolor='white');plt.close(fig)
(ROOT/'summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
print(json.dumps(meta,ensure_ascii=False,indent=2))

order=sorted(nodes,key=lambda n:([g for g,_,_ in GROUPS].index(n['group']),n['id'].lower()))
mat=np.zeros((len(order),len(order)))
for i,a in enumerate(order):
 for j,b in enumerate(order):
  if G.has_edge(a['id'],b['id']):mat[i,j]=G[a['id']][b['id']]['weight']
fig,ax=plt.subplots(figsize=(20,18),facecolor='white')
im=ax.imshow(np.ma.masked_equal(mat,0),cmap='YlGnBu',vmin=0,vmax=1,interpolation='nearest')
ax.set_xticks(range(len(order)),[n['id'] for n in order],rotation=90,fontsize=7.5)
ax.set_yticks(range(len(order)),[n['id'] for n in order],fontsize=7.5)
ax.tick_params(length=0)
for side in ax.spines.values():side.set_visible(False)
ax.set_title('Shared architecture tags · all-pairs weighted Jaccard',loc='left',fontsize=18,pad=18)
prev=0
for g,l,c in GROUPS:
 count=sum(n['group']==g for n in order)
 ax.axhline(prev-.5,color='#c5cbd2',linewidth=.6);ax.axvline(prev-.5,color='#c5cbd2',linewidth=.6)
 for k in range(prev,prev+count):ax.get_yticklabels()[k].set_color(c);ax.get_xticklabels()[k].set_color(c)
 prev+=count
fig.colorbar(im,ax=ax,shrink=.5,pad=.025,label='Weighted tag Jaccard (annotation-derived)')
fig.text(.10,.015,'Blank cells: no edge under the declared tag rule; diagonal omitted. Order follows display families, not learned clusters.',fontsize=10,color='#526676')
fig.tight_layout(rect=[0,.025,1,1])
fig.savefig(ROOT/'architecture_similarity_matrix.png',dpi=160,facecolor='white')
fig.savefig(ROOT/'architecture_similarity_matrix.svg',facecolor='white');plt.close(fig)
