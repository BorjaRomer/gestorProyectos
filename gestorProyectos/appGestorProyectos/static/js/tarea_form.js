function retornarDatos() {
    let url = "http://127.0.0.1:8000/tareasAPI/"
    fetch(url, {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({
            nombre : 'nombre'
        })
    })
        .then(response => response.json())
        .then(json => console.log(json))
}
