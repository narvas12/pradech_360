function display(){
    document.querySelector('.form-choice').style.display = 'flex'
}

function display_partnership(){
    document.querySelector('#form1').style.display = 'block'
    document.querySelector('#form2').style.display = 'none'
}

function display_creatives(){
    document.querySelector('#form2').style.display = 'block'
    document.querySelector('#form1').style.display = 'none'
}

document.querySelector('.close-form1').addEventListener('click', () => {
    document.querySelector('#form1').style.display = 'none'
})

document.querySelector('.close-form2').addEventListener('click', () => {
    document.querySelector('#form2').style.display = 'none'
})