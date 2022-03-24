/*Funcion para recuperar los datos de creacion de Avistamiento
y enviarlo en formato JSON*/

lista = [];
function insertarValores(){
  let formulario = document.forms['creacion'];
  for(let element of formulario){
    lista.push(element.value);
  }
  enviar()
}

function enviar(){
const url = 'http://127.0.0.1:5000/insertar';
const HTMLResponse = document.querySelector("#main");
const tpl = document.createDocumentFragment();
fetch(`${url}`,{
    method:"POST",
    body: JSON.stringify({
    "lugar":`${lista[0]}`,
    "especie":`${lista[1]}`,
    "avistamiento":`${lista[2]}`,
    "pais": `${lista[3]}`,
    "departamento": `${lista[4]}`,
    "ciudad": `${lista[5]}`,
    "nombrecientifico": `${lista[6]}`,
    "latitub": `${lista[7]}`,
    "longitub": `${lista[8]}`,
    "autor": `${lista[9]}`,
    "nota": `${lista[10]}`,
    "reino": `${lista[11]}`,
    "filo":`${lista[12]}`,
    "clase": `${lista[13]}`,
    "orden":`${lista[14]}`,
    "familia":`${lista[15]}`,
    "genero":`${lista[16]}`,
    "nombre_comun":`${lista[17]}`

    }),
    headers:{
        'Content-Type': 'application/json'
        //'Accept':'	text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    }
})
.then((response) => response.json())
.then((users) =>{
    console.log(users);
});
}
console.log(lista)
