const numberInput = document.querySelector("#numberInput");
const showButton = document.querySelector("#showButton");

const whileResult = document.querySelector("#whileResult");
const forResult = document.querySelector("#forResult");
const doWhileResult = document.querySelector("#doWhileResult");
showButton.addEventListener("click", function () {

    const userNumber = Number(numberInput.value);

    if (Number.isNaN(userNumber)) {
        whileResult.innerHTML = "Введено не число.";
        forResult.innerHTML = "Введено не число.";
        doWhileResult.innerHTML = "Введено не число.";
        return;
    }

    let whileText = "";
    let whileCounter = 0;

    if (userNumber >= 0) {

        while (whileCounter <= userNumber) {
            whileText += whileCounter + " ";
            whileCounter++;
        }

    } else {

        while (whileCounter >= userNumber) {
            whileText += whileCounter + " ";
            whileCounter--;
        }

    }

    whileResult.innerHTML = whileText;


    let forText = "";

    if (userNumber >= 0) {

        for (let i = 0; i <= userNumber; i++) {
            forText += i + " ";
        }

    } else {

        for (let i = 0; i >= userNumber; i--) {
            forText += i + " ";
        }

    }

    forResult.innerHTML = forText;


    let doWhileText = "";
    let doWhileCounter = 0;

    if (userNumber >= 0) {

        do {
            doWhileText += doWhileCounter + " ";
            doWhileCounter++;
        } while (doWhileCounter <= userNumber);

    } else {

        do {
            doWhileText += doWhileCounter + " ";
            doWhileCounter--;
        } while (doWhileCounter >= userNumber);

    }

    doWhileResult.innerHTML = doWhileText;

});