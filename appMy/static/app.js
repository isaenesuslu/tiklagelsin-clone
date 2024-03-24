let bar = document.querySelector(".bar-1");
let header = document.querySelector(".header");
let search = document.querySelector(".search-m");
let input = document.querySelector(".input-hero");
let headerSec = document.querySelector(".header-sec");
let removeClass = document.querySelector(".remove-class");

let barsFunc = ()=> {
    if (bar.classList.contains("fa-bars")){
        header.style.height="fit-content";
        bar.classList.remove("fa-bars");
        bar.classList.add("fa-x");
    }
    else {
        header.style.height="90px";
        bar.classList.remove("fa-x");
        bar.classList.add("fa-bars");
    };
}

let searchFunc = ()=>{
    input.style.display="block";
    if (bar.classList.contains("fa-x")){
        header.style.height="90px"
        bar.classList.remove("fa-x")
        bar.classList.add("fa-bars")
    }
}

let inputExit = () =>{
    input.style.display="none"
}

//* BİLGİSAYARDAN KONTROL ETTİĞİMİZ ZAMAN SONRADAN MOBIL GORUNUME GEÇTİĞİMİZ İÇİN ÇALIŞMAYACAKTIR (SAYFAYI YENİLEYİNCE NORMALE DÖNÜYOR) AMA MOBIL BİR KULLANICI İÇİN SORUNSUZ ÇALIŞACAKTIR.

if (screen.width <= 768 ) {
    headerSec.classList.remove("container")
}

if (screen.width <= 1399) {
    removeClass.classList.remove("px-5")
}

//* MOBİLDE CAROUSEL KAYDIRMAK İÇİN
var startX;

function handleTouchStart(event) {
  startX = event.touches[0].clientX;
}

function handleTouchMove(event) {
  var currentX = event.touches[0].clientX;
  var diffX = startX - currentX;

  if (Math.abs(diffX) > 20) {
    if (diffX > 0) {
      $('#carouselExample').carousel('next');
    } else {
      $('#carouselExample').carousel('prev');
    }
  }
}

var carousel = document.getElementById('carouselExample');

carousel.addEventListener('touchstart', handleTouchStart);
carousel.addEventListener('touchmove', handleTouchMove);
