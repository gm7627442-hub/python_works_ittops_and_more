const numberInput = document.querySelector("#numberInput");
const showButton = document.querySelector("#showButton");
const result = document.querySelector("#result");

showButton.addEventListener("click", function () {

    const userNumber = Number(numberInput.value);

    let resultText = "";

    for (let multiplier = 0; multiplier <= 9; multiplier++) {

        resultText =
            resultText +
            userNumber +
            " * " +
            multiplier +
            " = " +
            (userNumber * multiplier) +
            "<br>";

    }

    result.innerHTML = resultText;

});
