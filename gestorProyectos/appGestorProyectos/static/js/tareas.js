function cargarDatos() {
    let url = "http://127.0.0.1:8000/tareasAPI/"
    fetch(url)
        .then((respuesta) => respuesta.json())
        .then((datos) => {
            console.log(datos)
            crearTablaTareas(datos)
        })
}

cargarDatos();

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

function crearTabla(array) {
    let cabecera = '<thead>' + crearCabezera(array) + '</thead>';
    let tabla = cabecera + '<tbody>';
    for (const objeto of array) {
        tabla += crearFila(objeto);
    }
    tabla += '</tbody>';
    return tabla;
}

function crearTablaTareas(tareas) {
    let tablaINSERT = crearTabla(tareas);
    document.getElementById('tabla').innerHTML = tablaINSERT;
}

//crearTablaTareas(tareas);
