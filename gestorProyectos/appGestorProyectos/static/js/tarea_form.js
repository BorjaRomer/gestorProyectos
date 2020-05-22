function retornarDatos(datos){
    const data = new FormData();
    for(key in datos){
        data.append(key, datos[key])
    }
    fetch('http://127.0.0.1:8000/tareasAPI/', {
       method: 'POST',
       body: data
    })
    .then(function(response) {
       if(response.ok) {
           return response.text()
       } else {
           throw "Error en la llamada Ajax";
       }

    })
    .then(function(texto) {
       console.log(texto);
    })
    .catch(function(err) {
       console.log(err);
    });
}

document.getElementById('btn_enviar').addEventListener('click', function(event){
    event.preventDefault();

    var datos = {
        nombre: document.getElementById("id_nombre").value,
        descripcion: document.getElementsByName("descripcion")[0].value,
        responsable: document.getElementById('id_responsable').value,
        nivel_prioridad: document.getElementById('id_nivel_prioridad').value,
        estado_tarea: document.getElementById('id_estado_tarea').value,
        fecha_inicio: document.getElementsByName("fecha_inicio")[0].value,
        fecha_fin: document.getElementsByName("fecha_fin")[0].value,
        notas: document.getElementsByName("notas")[0].value,
    }

    console.log(datos);
    retornarDatos(datos);
});


