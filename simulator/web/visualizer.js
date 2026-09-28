"use strict";
let circuit=null, values={};
const $=s=>document.querySelector(s), app=$("#app");
function bit(v){return v?1:0}
function gate(type,a){if(type==="NOT")return 1-a[0];let r;if(type==="AND"||type==="NAND")r=a.every(Boolean)?1:0;else if(type==="OR"||type==="NOR")r=a.some(Boolean)?1:0;else r=a.reduce((x,y)=>x^y,0);return ["NAND","NOR","XNOR"].includes(type)?1-r:r}
function settle(){
 const s={}; circuit.inputs.forEach(n=>s[n]=bit(values[n])); const p=[...circuit.gates];
 while(p.length){let progress=false;for(let i=p.length-1;i>=0;i--){const g=p[i];if(g.inputs.every(n=>n in s)){s[g.output]=gate(g.type,g.inputs.map(n=>s[n]));p.splice(i,1);progress=true}}if(!progress)throw Error("Kretsen kan ikke settle")}
 return s;
}
function render(){
 if(!circuit)return; let s;try{s=settle()}catch(e){app.textContent=e.message;return}
 const teach=circuit.teaching||{}, switches=teach.switches||circuit.inputs.map(signal=>({signal,label:signal})), leds=teach.leds||circuit.outputs.map(signal=>({signal,label:signal}));
 app.innerHTML="<fieldset><legend>Brytere</legend>"+switches.map(x=>`<button data-s="${x.signal}">${x.label}: ${s[x.signal]}</button>`).join("")+"</fieldset>"+
 "<fieldset><legend>LED-er</legend>"+leds.map(x=>`<span class="signal ${s[x.signal]?"on":""}">${x.label}: ${s[x.signal]}</span>`).join("")+"</fieldset>"+
 "<fieldset><legend>Alle signaler</legend>"+Object.entries(s).map(([n,v])=>`<span class="signal ${v?"on":""}">${n}=${v}</span>`).join("")+"</fieldset>";
 app.querySelectorAll("button[data-s]").forEach(b=>b.onclick=()=>{values[b.dataset.s]=1-bit(values[b.dataset.s]);render()});
}
$("#file").onchange=async e=>{circuit=JSON.parse(await e.target.files[0].text());values={};circuit.inputs.forEach(n=>values[n]=0);render()};
