const result = document.querySelector("#result");

const userInput = prompt("Введите вещественное число:");

const userNumber = Number(userInput);

const smallerNumber = userNumber - 1;
const biggerNumber = userNumber + 1;

result.innerHTML =
    "Вы ввели число: " +
    userNumber +
    "<br>" +
    "Число на 1 меньше: " +
    smallerNumber +
    "<br>" +
    "Число на 1 больше: " +
    biggerNumber;