//function retornarDatos() {
//    let url = "http://127.0.0.1:8000/tareasAPI/"
//    fetch(url, {
//        method : 'POST',
//        headers : {
//            'Content-Type' : 'application/json'
//        },
//        body : JSON.stringify({
//            nombre : 'nombre'
//        })
//    })
//        .then(response => response.json())
//        .then(json => console.log(json))
//}

document.getElementById('btn_enviar').addEventListener('click', function(event){
    event.preventDefault();

    let nuevaTarea = {
        nombre: document.getElementsByName("nombre")[0].value,
        descripcion: document.getElementsByName("descripcion")[0].value,
        responsable: document.getElementsByName("responsable")[0].value,
        nivel_prioridad: document.getElementsByName("nivel_prioridad")[0].value,
        estado_tarea: document.getElementsByName("estado_tarea")[0].value,
        fecha_inicio: document.getElementsByName("fecha_inicio")[0].value,
        fecha_fin: document.getElementsByName("fecha_fin")[0].value,
        notas: document.getElementsByName("notas")[0].value,
    }

    console.log(nuevaTarea);

});

