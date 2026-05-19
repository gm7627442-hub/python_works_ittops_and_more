const xInput = document.querySelector("#xInput");
const yInput = document.querySelector("#yInput");

const showButton = document.querySelector("#showButton");

const result = document.querySelector("#result");

showButton.addEventListener("click", function () {

    const xCoordinate = Number(xInput.value);
    const yCoordinate = Number(yInput.value);

    if (
        Number.isNaN(xCoordinate) ||
        Number.isNaN(yCoordinate)
    ) {

        result.innerHTML = "Введено не число.";

    } else if (
        xCoordinate === 0 &&
        yCoordinate === 0
    ) {

        result.innerHTML =
            "Точка находится в центре координат.";

    } else if (xCoordinate === 0) {

        result.innerHTML =
            "Точка находится на оси Y.";

    } else if (yCoordinate === 0) {

        result.innerHTML =
            "Точка находится на оси X.";

    } else if (
        xCoordinate > 0 &&
        yCoordinate > 0
    ) {

        result.innerHTML =
            "Точка находится в 1 четверти.";

    } else if (
        xCoordinate < 0 &&
        yCoordinate > 0
    ) {

        result.innerHTML =
            "Точка находится во 2 четверти.";

    } else if (
        xCoordinate < 0 &&
        yCoordinate < 0
    ) {

        result.innerHTML =
            "Точка находится в 3 четверти.";

    } else {

        result.innerHTML =
            "Точка находится в 4 четверти.";

    }

});