//获取按钮：
let scrollToTopbutton = document.querySelector(".scroll-to-top");

// 当用户从文档顶部向下滚动 20px 时，显示按钮
function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollToTopbutton.style.display = "block";
  } else {
    scrollToTopbutton.style.display = "none";
  }
}

// 当用户点击按钮时，滚动到文档顶部
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
};

window.addEventListener('scroll', scrollFunction);
scrollToTopbutton.addEventListener("click", topFunction);