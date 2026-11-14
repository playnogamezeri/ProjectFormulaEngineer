(function(){
const id=document.body.dataset.department,all=window.FOE_DEPARTMENTS||[],m=all.find(function(x){return x.id===id;});
const $=function(x){return document.getElementById(x);};
if(!m){$("pageTitle").textContent="Department not found";return;}
document.title=m.name+" | Formula of Everything";
$("pageTitle").textContent=m.name;$("pageDesc").textContent=m.desc;
$("pageTool").textContent=m.tool;$("pageEquation").textContent=m.eq;
$("pageWhat").textContent=m.what;$("pageELI5").textContent=m.eli5;$("pageNote").textContent=m.note;
$("departmentBreadcrumb").textContent=m.name;
$("inputFields").innerHTML=m.f.map(function(f){return '<label>'+f[1]+'<input name="'+f[0]+'" type="'+(typeof f[2]==="string"?"text":"number")+'" step="any" value="'+String(f[2]).replace(/&/g,"&amp;").replace(/"/g,"&quot;")+'" required></label>';}).join("");
const key="foe-department-history-v6";
function history(){try{return JSON.parse(localStorage.getItem(key)||"[]").filter(function(x){return x&&x.department===m.name;});}catch(e){return[];}}
function draw(){const a=history();$("historyList").innerHTML=a.length?a.slice(0,10).map(function(r){return '<article><b>'+r.tool+'</b><p>'+r.result+'</p><small>'+new Date(r.created).toLocaleString()+'</small></article>';}).join(""):"<p class='muted'>No saved calculations for this department yet.</p>";}
let last=null;
$("calculate").addEventListener("click",function(){
 const v={};for(const f of m.f){const el=$("inputFields").querySelector('[name="'+f[0]+'"]'),raw=el.value;if(typeof f[2]==="string"){if(!raw.trim()){$("calcResult").textContent="Enter observations before calculating.";return;}v[f[0]]=raw.trim();}else{if(raw.trim()===""||!Number.isFinite(Number(raw))){$("calcResult").textContent="Every field must contain a valid number.";return;}v[f[0]]=Number(raw);}}
 try{last={department:m.name,tool:m.tool,equation:m.eq,result:m.run(v),created:new Date().toISOString()};$("calcResult").textContent=last.result;$("saveCalculation").disabled=false;}catch(e){last=null;$("calcResult").textContent=e.message;$("saveCalculation").disabled=true;}
});
$("saveCalculation").addEventListener("click",function(){if(!last)return;let a;try{a=JSON.parse(localStorage.getItem(key)||"[]");if(!Array.isArray(a))a=[];}catch(e){a=[];}a.unshift(last);localStorage.setItem(key,JSON.stringify(a.slice(0,500)));$("saveCalculation").disabled=true;draw();});
$("clearInputs").addEventListener("click",function(){$("inputFields").querySelectorAll("input").forEach(function(el){const f=m.f.find(function(x){return x[0]===el.name;});el.value=f[2];});$("calcResult").textContent="Inputs reset. Calculate when ready.";last=null;$("saveCalculation").disabled=true;});
const index=all.findIndex(function(x){return x.id===id;}),prev=all[(index+all.length-1)%all.length],next=all[(index+1)%all.length];
$("prevDept").href=prev.slug+".html";$("prevDept").textContent="← "+prev.name;
$("nextDept").href=next.slug+".html";$("nextDept").textContent=next.name+" →";
$("deptDirectory").innerHTML=all.map(function(x){return '<a class="linkcard" href="'+x.slug+'.html">'+x.name+'<small>'+x.tool+'</small></a>';}).join("");
draw();
})();