"use strict";
// No localStorage, cookies, external services, logging of keys or raw request bodies.
const el = id => document.getElementById(id);
const names = {"demo-bank-a":"Banque A","demo-psp-b":"PSP B","demo-mobile-c":"Mobile Money C"};
let active = false;
function message(text, ok=false){el("message").textContent=text;el("message").className="status "+(ok?"good":"bad");}
function empty(){el("signals").replaceChildren();el("count").textContent="—";}
function td(text){const item=document.createElement("td");item.textContent=String(text);return item;}
function render(signals){
  const body=el("signals");body.replaceChildren();el("count").textContent=String(signals.length);
  if(!signals.length){const row=document.createElement("tr");const cell=td("Aucun signal actif");cell.colSpan=5;row.append(cell);body.append(row);return;}
  for(const s of signals){const row=document.createElement("tr");
    for(const col of ["signal_id","category","severity","scenario_ref","expires_at"])row.append(td(s[col]));
    body.append(row);}
}
async function api(method,path,key,body){
  const headers={"Accept":"application/json"};
  if(key)headers["X-Lab-Key"]=key;
  if(body)headers["Content-Type"]="application/json";
  const res=await fetch(path,{method,headers,body:body?JSON.stringify(body):undefined,cache:"no-store",credentials:"omit"});
  let data=null;try{data=await res.json();}catch{}
  return {status:res.status,data};
}
function getKey(){const key=el("lab-key").value; if(!key){message("Saisir la clé fictive de cette institution.");return null;}return key;}
async function refresh(){
  const key=getKey();if(!key)return;
  const chosen=el("institution").value;
  try{
    const res=await api("GET","/signals",key);
    if(res.status!==200||res.data?.institution!==chosen){
      empty();message("Consultation refusée ou clé appartenant à une autre institution (HTTP "+res.status+").");return;
    }
    render(res.data.signals);message(names[chosen]+" : signaux chargés.",true);
  }catch{empty();message("Service indisponible ou erreur réseau.");}
}
async function run(){
  const key=getKey();if(!key)return;
  if(active)return;active=true;el("run").disabled=true;el("load").disabled=true;
  const institution=el("institution").value;
  const list=el("results");list.replaceChildren();const outcomes=[];
  async function check(label,fn){
    let ok=false;try{ok=await fn();}catch{}
    outcomes.push(ok);
    const item=document.createElement("li");item.textContent=(ok?"PASS — ":"FAIL — ")+label;item.className=ok?"good":"bad";list.append(item);
  }
  const suffix=Date.now().toString(36)+"-"+Math.random().toString(36).slice(2,10);
  const signal="demo-web-"+suffix;
  const payload={signal_id:signal,category:"suspicious-transfer",severity:"medium",
    scenario_ref:"demo-scenario-web-"+suffix,expires_in_hours:1};
  try{
    await check("Service disponible (200)",async()=>(await api("GET","/health")).status===200);
    // Do not write a signal unless the supplied key authenticates the selected institution.
    const own=await api("GET","/signals",key);
    const valid=own.status===200&&own.data?.institution===institution;
    await check("Clé correspondant à l'institution sélectionnée (200)",async()=>valid);
    if(valid){
      await check("Création d'un signal fictif (201)",async()=>(await api("POST","/signals",key,payload)).status===201);
      await check("Lecture du signal créé (200)",async()=>(await api("GET","/signals/"+encodeURIComponent(signal),key)).status===200);
      await check("Rejeu rejeté comme doublon (409)",async()=>(await api("POST","/signals",key,payload)).status===409);
      await check("Champ interdit rejeté (422)",async()=>(await api("POST","/signals",key,{...payload,pan:"demo-sensitive-field"})).status===422);
      await check("Identifiant inexistant (404)",async()=>(await api("GET","/signals/demo-not-found-12345678",key)).status===404);
    }
    await check("Lecture sans clé refusée (401)",async()=>(await api("GET","/signals")).status===401);
    const passed=outcomes.filter(Boolean).length;
    el("test-summary").textContent=passed+"/"+outcomes.length+" tests PASS (session navigateur)";
    el("test-summary").className="status "+(passed===outcomes.length?"good":"bad");
    if(valid)await refresh();
  }finally{active=false;el("run").disabled=false;el("load").disabled=false;}
}
el("load").addEventListener("click",refresh);
el("run").addEventListener("click",run);
el("institution").addEventListener("change",()=>{empty();el("lab-key").value="";message("Institution changée : saisir sa propre clé.");el("results").replaceChildren();el("test-summary").textContent="Aucun test exécuté dans cette session";});
el("clear").addEventListener("click",()=>{el("lab-key").value="";empty();el("results").replaceChildren();el("test-summary").textContent="Aucun test exécuté dans cette session";message("Clé et résultats effacés.",true);});
api("GET","/health").then(r=>{el("health").textContent=r.status===200?"Service : disponible":"Service : indisponible";}).catch(()=>{el("health").textContent="Service : indisponible";});
