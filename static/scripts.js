
let ingredientForm = document.querySelectorAll(".ingredient")
let addButton = document.querySelector("#add-form")
let parentDiv =  document.querySelector("#form-container");
let totalForms = document.querySelector("#id_form-TOTAL_FORMS")


let formNum = ingredientForm.length-1 

addButton.addEventListener('click', addForm)
   
function addForm(e){
    e.preventDefault()

    let newForm = ingredientForm[0].cloneNode(true) 

    let formRegex = RegExp(`form-(\\d){1}-`,'g')
    formNum++ 
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
    parentDiv.insertBefore(newForm, addButton)
    totalForms.setAttribute('value', `${formNum+1}`) 
   
}

