let password1 = document.querySelector('.password1')
let password2 = document.querySelector('.password2')
let button = document.querySelector('.checkButton')


function revisarContraseña() {
    let clave = password1.value
    if (password1.value == password2.value && clave.length >= 8) {
        button.removeAttribute('disabled')
    } else {
        button.setAttribute('disabled','True')
    }

    
}

password1.addEventListener('input',revisarContraseña)
password2.addEventListener('input',revisarContraseña)