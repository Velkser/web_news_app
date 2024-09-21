function incrementCount() {
    var countElement = document.getElementById('count');
    var currentCount = parseInt(countElement.innerText);
    countElement.innerText = currentCount + 1;
}

