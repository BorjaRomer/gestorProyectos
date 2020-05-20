function retornarDatos(data) {
    let url = "http://127.0.0.1:8000/tareasAPI/"
    fetch(url, {
        method: 'POST',
        body : JSON.stringify(data),
        headers: {
            'Content-Type' : 'application/json',
        }
    })
//    .then(response => response.json())
//    .then(json => console.log(json))
    .then(response => {
        if (response.ok) {
            return response.json()
        } else {
            console.log(response.statusCode)
            return Promise.reject('Error en la respuesta del server')
        }
    })
    .then(data => console.log(data))
    .catch(error => console.log('Error: ', error));
}


document.getElementById('btn_enviar').addEventListener('click', function(event){
    event.preventDefault();

    let nuevaTarea = {
        nombre: document.getElementById("id_nombre").value,
        descripcion: document.getElementsByName("descripcion")[0].value,
        descripcion: document.getElementsByName("descripcion")[0].value,
        responsable: document.getElementById('id_responsable').value,
        nivel_prioridad: document.getElementById('id_nivel_prioridad').value,
        estado_tarea: document.getElementById('id_estado_tarea').value,
        fecha_inicio: document.getElementsByName("fecha_inicio")[0].value,
        fecha_fin: document.getElementsByName("fecha_fin")[0].value,
        notas: document.getElementsByName("notas")[0].value,
    }

    console.log(nuevaTarea);
    retornarDatos(nuevaTarea);

});

