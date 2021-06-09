/*!
* Start Bootstrap - Business Casual v6.0.0 (https://startbootstrap.com/theme/business-casual)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-casual/blob/master/LICENSE)
*/
// Highlights current date on contact page
$('.list-hours li').eq(new Date().getDay()).addClass('today');


// code emprunté sur :  https://jsfiddle.net/ourcodeworld/rce6nn3z/2/
function dl(filename, text) {
    let element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

function download(id) {
    const text = document.getElementById(id).innerHTML;
    const fileName = "Rapport.html"

    dl(fileName, text)
}