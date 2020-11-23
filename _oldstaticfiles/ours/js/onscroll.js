//
// function scrollFunction() {
//     if (document.getElementById("content").scrollTop > 0) {
//         shrink()
//     } else {
//         if(document.getElementById("content").scrollTop === 0)
//             grow()
//     }
// }
//
// function shrink(){
//     if(document.getElementById("content").scrollTop === 0){
//         return;
//     }
//     document.getElementById("navbar").style.padding = "10px 10px";
//     document.getElementById("content").style.marginTop = "-25vh";
//     document.getElementById("content").style.height = "140%";
//     // setTimeout(function(){shrink_books()}, 1);
//
// }
//
// function grow() {
//     document.getElementById("navbar").style.padding = "30px 10px";
//     document.getElementById("content").style.marginTop = "-20vh";
//     document.getElementById("content").style.height = "130%";
//     // setTimeout(function(){grow_books()}, 1);
//
//
// }
//
// function shrink_books(){
//     document.getElementById("book-1-title").style.top = "-100px";
//     document.getElementById("book-2-title").style.top = "-100px";
//     document.getElementById("book-3-title").style.top = "-100px";
//     document.getElementById("book-1-title").style.position = "relative";
//     document.getElementById("book-2-title").style.position = "relative";
//     document.getElementById("book-3-title").style.position = "relative";
//
//
// }
//
// function grow_books() {
//     document.getElementById("book-1-title").style.top = "0px";
//     document.getElementById("book-2-title").style.top = "0px";
//     document.getElementById("book-3-title").style.top = "0px";
//     document.getElementById("book-1-title").style.position = "intitial";
//     document.getElementById("book-2-title").style.position = "intitial";
//     document.getElementById("book-3-title").style.position = "intitial";
//
// }