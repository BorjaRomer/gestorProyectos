function cargarDatos(filtro) {
    let url = "http://127.0.0.1:8000/tareasAPI/"
    fetch(url)
        .then((respuesta) => respuesta.json())
        .then((datos) => {
            crearTablaTareas(datos, filtro)
        })
}

cargarDatos("");

document.getElementById('select').addEventListener('change', function(event) {
    cargarDatos(event.target.value);
});

function crearCabezera(array2) {
    let cabezera = '<tr>'
    for (const iterator of array2) {
        for (const key in iterator) {
            cabezera += '<th>' + key + '</th>';
        }
        break;
    }
    cabezera += '</tr>'
    return cabezera;
}

function crearFila(objeto) {
    let fila = '<tr>';
    for (const clave in objeto) {
        fila += '<td>' + objeto[clave] + '</td>';
    }
    fila += '</tr>';
    return fila;
}

function crearTabla(array, filtro) {
    let cabecera = '<thead>' + crearCabezera(array) + '</thead>';
    let tabla = cabecera + '<tbody>';
    for (const objeto of array) {
        if(objeto.estado_tarea == filtro) {
            tabla += crearFila(objeto);
        }else if(filtro === "") {
            tabla += crearFila(objeto);
        }
    }
    tabla += '</tbody>';
    return tabla;
}

function crearTablaTareas(tareas, filtro) {
    let tablaINSERT = crearTabla(tareas, filtro);
    document.getElementById('tabla').innerHTML = tablaINSERT;
}

