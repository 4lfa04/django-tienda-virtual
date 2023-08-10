let menosButton = document.querySelector('.menos');
let masButton = document.querySelector('.mas');
let conteo = document.querySelector('.conteo');
let dataInput = document.querySelector('.data');
let zonaprecio = document.querySelector('.precio');
let zonaPrecioTotal = document.querySelector('.precio-total');

function contMenos() {
    data = conteo.innerHTML
    data = parseInt(data)
    if (data > 0) {
        data = data - 1
        conteo.innerHTML = data
        dataInput.value = data
    }
    ponerPrecio(zonaprecio,data)
}
function contMas() {
    data = conteo.innerHTML
    data = parseInt(data)
    data = data + 1
    conteo.innerHTML = data
    dataInput.value = data
    ponerPrecio(zonaprecio,data)
}

function ponerPrecio(precio, cantidad) {
    precio = precio.innerHTML
    precio = precio.split('$')
    precio = precio[1]
    precio = parseInt(precio)*cantidad
    console.log(precio)
    zonaPrecioTotal.innerHTML = '$' + precio
}
let cuenta = parseInt(conteo.innerHTML)
ponerPrecio(zonaprecio,cuenta)

menosButton.addEventListener('click',contMenos)
masButton.addEventListener('click',contMas)