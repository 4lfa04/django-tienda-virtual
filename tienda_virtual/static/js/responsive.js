let boton = document.querySelector('.menu-navegacion')
let botonera = document.querySelector('.botonera-right')

boton.addEventListener('click',()=>{
    if ('botonera-right botonera-right-desplegada' == botonera.classList) {
        botonera.classList = 'botonera-right'
    } else {
        botonera.classList = 'botonera-right botonera-right-desplegada'
    }
})