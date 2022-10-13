let body = document.querySelector('body');
body.addEventListener('dblclick', giveAlert);

function giveAlert() {
    alert('this is an alert');
}

const bttn = document.getElementById('bttn');
bttn.addEventListener('click', colorChange);

function colorChange() {
    this.style.backgroundColor = "red";
}

document.getElementById("demo").addEventListener("keypress", myFunction);

function myFunction() {
  document.getElementById("demo").style.backgroundColor = "blue";
}