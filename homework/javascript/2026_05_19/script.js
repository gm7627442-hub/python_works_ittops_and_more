const setInput = document.getElementById("setInput");
const addSetBtn = document.getElementById("addSetBtn");

const commonDocInput = document.getElementById("commonDocInput");
const addCommonBtn = document.getElementById("addCommonBtn");

const cards = document.getElementById("cards");



// Добавление карточки

addSetBtn.addEventListener("click", () => {

    const title = setInput.value.trim();

    if(title === ""){
        return;
    }

    createCard(title);

    setInput.value = "";

});



// Создание карточки

function createCard(title){

    const card = document.createElement("div");
    card.className = "card";



    const cardTitle = document.createElement("h3");
    cardTitle.textContent = title;



    const deleteCardBtn = document.createElement("button");
    deleteCardBtn.textContent = "Удалить комплект";

    deleteCardBtn.addEventListener("click", () => {
        card.remove();
    });



    const docInput = document.createElement("input");
    docInput.type = "text";
    docInput.placeholder = "Название документа";



    const addDocBtn = document.createElement("button");
    addDocBtn.textContent = "Добавить документ";



    const docsList = document.createElement("div");



    addDocBtn.addEventListener("click", () => {

        const docName = docInput.value.trim();

        if(docName === ""){
            return;
        }

        addDocument(docsList, docName);

        docInput.value = "";

    });



    card.appendChild(cardTitle);
    card.appendChild(deleteCardBtn);

    card.appendChild(document.createElement("br"));
    card.appendChild(document.createElement("br"));

    card.appendChild(docInput);
    card.appendChild(addDocBtn);

    card.appendChild(document.createElement("br"));
    card.appendChild(document.createElement("br"));

    card.appendChild(docsList);

    cards.appendChild(card);

}



// Добавление документа

function addDocument(container, name){

    const doc = document.createElement("div");
    doc.className = "doc";



    const text = document.createElement("span");
    text.textContent = name + " ";



    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "X";



    deleteBtn.addEventListener("click", () => {
        doc.remove();
    });



    doc.appendChild(text);
    doc.appendChild(deleteBtn);

    container.appendChild(doc);

}



// Добавление общего документа

addCommonBtn.addEventListener("click", () => {

    const commonName = commonDocInput.value.trim();

    if(commonName === ""){
        return;
    }



    const allDocsLists = document.querySelectorAll(".card > div:last-child");



    allDocsLists.forEach(list => {
        addDocument(list, commonName);
    });



    commonDocInput.value = "";

});