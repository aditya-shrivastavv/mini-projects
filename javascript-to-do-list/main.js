const inputBox = document.querySelector("#input-box");
const submitButton = document.querySelector("#submit-btn");
const toDoList = document.querySelector(".to-do-items");

const addOnSubmit = () => {
    const todo = document.createElement("li");
    todo.textContent = inputBox.value;
    inputBox.value = "";
    toDoList.appendChild(todo);
}

submitButton.addEventListener("click", addOnSubmit)