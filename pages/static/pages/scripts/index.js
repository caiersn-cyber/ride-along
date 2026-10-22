// 导航栏
let myTopnav = document.querySelector("#myTopnav");

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    myTopnav.classList.add("border-bottom", "shadow-lg");
  } else {
    myTopnav.classList.remove("border-bottom", "shadow-lg");
  }
};

window.addEventListener('scroll', scrollFunction);

// 手风琴
// 获取所有.item元素
let cityItems=document.querySelectorAll('.city .item');
let storyItems=document.querySelectorAll('.story .item');

// 设置选中态样式
function setActiveCity(){
    // 遍历所有.item元素，移出active样式
    cityItems.forEach((item)=>{
      item.classList.remove('active');
    })
    // 为当前选中项添加active样式
    this.classList.add('active');
}

function setActiveStory(){
  // 遍历所有.item元素，移出active样式
  storyItems.forEach((item)=>{
    item.classList.remove('active');
  })
  // 为当前选中项添加active样式
  this.classList.add('active');
}

// 遍历所有.item元素，分别为其设置点击事件
cityItems.forEach((item)=>{
    item.addEventListener('click',setActiveCity);
})

storyItems.forEach((item)=>{
  item.addEventListener('click',setActiveStory);
});