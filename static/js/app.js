const navSlide = ()=>{
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav_links');
    burger.addEventListener('click',()=>{
      nav.classList.toggle('nav-active');
    });
  }
  navSlide();
  
  function mySignin() {
    document.getElementById("screen").style.height = "100%";
    document.getElementById("signin").style.height = "80%";
    document.getElementById("signup").style.height = "0";
  }
  function mySignup() {
    document.getElementById("screen").style.height = "100%";
    document.getElementById("signup").style.height = "80%";
    document.getElementById("signin").style.height = "0";
  }
  function myFunction1() {
    document.getElementById("screen").style.height = "0";
    document.getElementById("signup").style.height = "0";
    document.getElementById("signin").style.height = "0";
  }
  
  var errors = document.querySelectorAll('.errors')
  var errors1 = document.querySelectorAll('.errors1')
  function init(){
    notify();
    notify1();
  }
  function removeTags(str) {
    if ((str===null) || (str===''))
    return false;
    else
    str = str.toString();
    return str.replace( /(<([^>]+)>)/ig, '');
  }
  function notify() {
    
    console.log(errors)
    for(index = 0; index < errors.length; index++) { 
      var note = errors[index].innerHTML;
      note = note.trim();

      console.log(note)
      if(note!="")
      {
        mySignin();
        alert(removeTags(note));
        break;
      }
    } 
  }
  function notify1() {
    for(index = 0; index < errors1.length; index++) { 
      var note = errors1[index].innerHTML;
      note = note.trim();
      if(note!="")
      {
        mySignup();
        alert(removeTags(note));
        break;
      }
    } 
  }
  document.body.onload = init;
  