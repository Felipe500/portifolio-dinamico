
function escrevendoLetra(){
    function ativaLetra(elemento){
        const arrTexto = elemento.innerHTML.split('');
        elemento.innerHTML  = '';
        arrTexto.forEach((letra, i)=>{
            setTimeout(()=>{
                elemento.innerHTML += letra;
            }, 75 * i);
        });
    }

    const titulo = document.querySelector('.digitando');
    ativaLetra(titulo);
}

function ativacaoMenu(){
    const ativaMenu = document.querySelector('.fa-bars');
    const navMenu = document.querySelector('header .navegacao-primaria')


    ativaMenu.addEventListener('click', ()=>{
        ativaMenu.classList.toggle('fa-x')
        navMenu.classList.toggle('ativado')
    })
}

ativacaoMenu()


const listaALL = document.querySelectorAll('.projects_armazenamento ul li');
const buttonGeral = document.querySelectorAll('.project_navegacao li');
const buttonALL = document.querySelector('.project_models .all');

listaALL.forEach((item)=>{
    item.classList.add('ativo');
})

function removeClick(index){
    buttonGeral.forEach((item)=>{
        item.classList.remove('ativo');
    })
    buttonGeral[index].classList.add('ativo')
}

buttonGeral.forEach((event,index)=>{
    event.addEventListener('click', ()=>{
        removeClick(index)
    })
})


function ScrollHomeFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

function ScrollHomeFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
