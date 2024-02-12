const no = document.getElementById('no')
no.addEventListener('mouseover', moveHover);
no.addEventListener('click', moveHover);

function moveHover(){
    const i=Math.floor(Math.random() * 100)+1 ;
    const j=Math.floor(Math.random() * 100)+1 ;

    no.style.left = i+"px"
    no.style.top = j+"px"
}   