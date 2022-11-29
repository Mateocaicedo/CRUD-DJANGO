let flash = document.getElementsByClassName('message-success')[0];
console.log(flash);
if (flash) {
    setTimeout(function () {
        flash.style.display = 'none';
    }, 3000);
}