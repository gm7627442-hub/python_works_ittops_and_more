const startInput = document.querySelector("#startInput");
const finishInput = document.querySelector("#finishInput");
const thresholdInput = document.querySelector("#thresholdInput");

const showButton = document.querySelector("#showButton");
const result = document.querySelector("#result");

showButton.addEventListener("click", function () {

    const startNumber = Number(startInput.value);
    const finishNumber = Number(finishInput.value);
    const thresholdNumber = Number(thresholdInput.value);

    if (
        Number.isNaN(startNumber) ||
        Number.isNaN(finishNumber) ||
        Number.isNaN(thresholdNumber)
    ) {
        result.innerHTML = "Введено не число.";
        return;
    }

    let resultText = "";

    for (
        let currentNumber = startNumber;
        currentNumber <= finishNumber;
        currentNumber++
    ) {

        if (currentNumber < thresholdNumber) {

            resultText =
                resultText +
                "&lt;&lt;" +
                currentNumber +
                "&gt;&gt;<br>";

        } else if (currentNumber > thresholdNumber) {

            resultText =
                resultText +
                "**" +
                currentNumber +
                "**<br>";

        } else {

            resultText =
                resultText +
                currentNumber +
                "<br>";

        }

    }

    result.innerHTML = resultText;

});