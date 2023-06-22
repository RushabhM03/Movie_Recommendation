//console.log("hello world");
const modeToggle = document.getElementById('toggle-mode');

document.addEventListener('DOMContentLoaded', function() {
    var storedMode = localStorage.getItem('mode');
    var body = document.body;

    if (storedMode === 'light-mode') {
        body.classList.remove('dark-mode');
        body.classList.add('light-mode');
        modeToggle.innerHTML = '<svg class="-mr-8 micon" stroke="white" fill="#22c55e" height="36" viewBox="0 0 512 512" width="36" xmlns="http://www.w3.org/2000/svg"><title/><path d="M152.62,126.77c0-33,4.85-66.35,17.23-94.77C87.54,67.83,32,151.89,32,247.38,32,375.85,136.15,480,264.62,480c95.49,0,179.55-55.54,215.38-137.85-28.42,12.38-61.8,17.23-94.77,17.23C256.76,359.38,152.62,255.24,152.62,126.77Z"/></svg>'
    } else {
        body.classList.remove('light-mode');
        body.classList.add('dark-mode');
        modeToggle.innerHTML = '<?xml version="1.0" ?><svg class="-mr-8" id="Layer_1_1_" style="enable-background:new 0 0 16 16;" height="36px" width="36px" fill="white" version="1.1" viewBox="0 0 16 16" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><circle cx="8.5" cy="7.5" r="4.5"/><rect height="2" width="1" x="8"/><rect height="2" width="1" x="8" y="13"/><rect height="1" width="2" x="14" y="7"/><rect height="1" width="2" x="1" y="7"/><rect height="2" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -4.7175 12.8033)" width="1" x="12.596" y="11.096"/><rect height="2" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -0.9099 3.6109)" width="1" x="3.404" y="1.904"/><rect height="1" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -7.4099 6.3033)" width="2" x="2.904" y="11.596"/><rect height="1" transform="matrix(0.7071 -0.7071 0.7071 0.7071 1.7823 10.1107)" width="2" x="12.096" y="2.404"/></svg>'
    }
});

document.addEventListener('DOMContentLoaded', function() {
    
    const body = document.body;
    const navbar = document.getElementsByTagName('nav');
  
    modeToggle.addEventListener('click', function() {
      //body.classList.toggle('dark-mode');
      if(body.classList.contains('light-mode')){
        body.classList.remove('light-mode')
        body.classList.add('dark-mode')
        //sessionStorage.setItem('mode', 'dark-mode')
        localStorage.setItem('mode', 'dark-mode');
        
      }else if(body.classList.contains('dark-mode')){
        body.classList.remove('dark-mode')
        body.classList.add('light-mode')
        //sessionStorage.setItem('mode', 'light-mode')
        localStorage.setItem('mode', 'light-mode');
      }
    });
  });

modeToggle.addEventListener('click', function() {
    var bodyClass = document.body.className;
    //const modeToggle = document.getElementById('toggle-mode');
    if (bodyClass.includes('dark-mode')) {
        modeToggle.innerHTML = '<svg class="-mr-8 micon" stroke="white" fill="#22c55e" height="36" viewBox="0 0 512 512" width="36" xmlns="http://www.w3.org/2000/svg"><title/><path d="M152.62,126.77c0-33,4.85-66.35,17.23-94.77C87.54,67.83,32,151.89,32,247.38,32,375.85,136.15,480,264.62,480c95.49,0,179.55-55.54,215.38-137.85-28.42,12.38-61.8,17.23-94.77,17.23C256.76,359.38,152.62,255.24,152.62,126.77Z"/></svg>'
    }

    if (bodyClass.includes('light-mode')) {
      modeToggle.innerHTML = '<?xml version="1.0" ?><svg class="-mr-8" id="Layer_1_1_" style="enable-background:new 0 0 16 16;" height="36px" width="36px" fill="white" version="1.1" viewBox="0 0 16 16" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><circle cx="8.5" cy="7.5" r="4.5"/><rect height="2" width="1" x="8"/><rect height="2" width="1" x="8" y="13"/><rect height="1" width="2" x="14" y="7"/><rect height="1" width="2" x="1" y="7"/><rect height="2" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -4.7175 12.8033)" width="1" x="12.596" y="11.096"/><rect height="2" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -0.9099 3.6109)" width="1" x="3.404" y="1.904"/><rect height="1" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -7.4099 6.3033)" width="2" x="2.904" y="11.596"/><rect height="1" transform="matrix(0.7071 -0.7071 0.7071 0.7071 1.7823 10.1107)" width="2" x="12.096" y="2.404"/></svg>'
    }
  });
