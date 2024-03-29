const slideList = document.querySelector('.slide_list'); // Slide parent dom
const slideContents = document.querySelectorAll('.slide_content'); // each slide dom
const slideBtnNext = document.querySelector('.slide_btn_next'); // next button
const slideBtnPrev = document.querySelector('.slide_btn_prev'); // prev button
const slideLen = slideContents.length; // slide length
const slideWidth = 400; // slide width
const slideSpeed = 300; // slide speed
const startNum = 0;


slideList.style.width = slideWidth * (slideLen + 2) + "px";


let firstChild = slideList.firstElementChild;
let lastChild = slideList.lastElementChild; 
let clonedFirst = firstChild.cloneNode(true);
let clonedLast = lastChild.cloneNode(true);

slideList.appendChild(clonedFirst)
slideList.insertBefore(clonedLast, slideList.firstElementChild);
// curIndex와 curSlide
slideList.style.transform = "translate3d(-" + (slideWidth * (startNum +1)) + "px, 0px, 0px";

let curIndex = startNum;
let curSlide = slideContents[curIndex];
curSlide.classList.add('slide_activate')


/** 다음 버튼 기능 구현 */
slideBtnNext.addEventListener('click', function() {
    if (curIndex <= slideLen - 1) {
        slideList.style.transition = slideSpeed + "ms";
        slideList.style.transform = "translate3d(-" + (slideWidth * (curIndex + 2)) + "px, 0px, 0px)";
    }
    /*if (curIndex === slideLen -1){
        setTimeout(function(){
            slideList.style.transition = "0ms";
            slideList.style.transform = "translate3d(-" + slideWidth + "px, 0px, 0px)";
        }, slideSpeed);
        curIndex = -1;
    }*/
    /*--curSlide.classList.remove('slide_active');*/
    curSlide = slideContents[++curIndex];
    /*curSlide.classList.add('slide_active');*/
});



