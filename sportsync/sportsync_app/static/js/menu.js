var menuItem = document.querySelectorAll('.item-menu') //guarda os elementos em um array

function selectLink(){
    menuItem.forEach((item)=>
        item.classList.remove('ativo')
    )
    this.classList.add('ativo')
}

menuItem.forEach((item)=>
    item.addEventListener('click',selectLink)
)