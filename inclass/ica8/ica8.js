let body = document.querySelector('body');
body.addEventListener('click', giveAlert);

function giveAlert() {
    alert('this is an alert');
}

body.addEventListener('hover', colorChange);

function colorChange() {
    this.style.backgroundColor = "red";
}