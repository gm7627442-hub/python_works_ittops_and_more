const input = document.querySelector("#input");
const addButton = document.querySelector("#addButton");
const container = document.querySelector("#container");

addButton.addEventListener("click", function () {

    const text = input.value;

    const paragraph = document.createElement("p");

    paragraph.innerText = text + " ";

    const deleteButton = document.createElement("button");

    deleteButton.innerText = "X";

    deleteButton.addEventListener("click", function () {

        paragraph.remove();

    });

    paragraph.append(deleteButton);

    container.append(paragraph);

});