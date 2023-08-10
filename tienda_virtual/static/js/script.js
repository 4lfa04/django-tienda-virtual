let input = document.querySelector('.demostration-input')

'Cerveza Fresca'
let articulo = ['Cerveza Fresca', 'Gafas de Sol', 'Sombrero Vaquero']
let lista = []
for (art of articulo) {
    let palabra = art.split('')
    let palabraDeletreada = ''
    for (const deletreo of palabra) {
        palabraDeletreada = palabraDeletreada + deletreo
        lista.push(palabraDeletreada)
    }
    for (let i = 0; i < 10; i++) {
        lista.push(palabraDeletreada)
    }
    lista.push(palabraDeletreada)
}
i = 0
setInterval(()=>{
    if (i <= lista.length-1){
        input.value = lista[i]
        i++
    } else {
        i = 0
    }
},300)

// alert(input.value)