/*Funcion para eliminar valores*/
function eliminarValores(){
  let id;
  let formulario = document.forms['eliminar'];
  for(let element of formulario){
      id = element.value;
      console.log(id)
  }
  //enviar(id)
}

function enviar(id){
const url = 'http://127.0.0.1:5000/eliminar';
const HTMLResponse = document.querySelector("#main");
const tpl = document.createDocumentFragment();
fetch(`${url}`,{
    method:"DELETE",
    body: JSON.stringify({
    "id":`${4}`
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
