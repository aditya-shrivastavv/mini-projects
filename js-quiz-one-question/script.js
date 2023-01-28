const statement = document.querySelector("#statement");
const optionButtons = document.querySelectorAll("#options button");
const explanation = document.querySelector("#explanation");

const fact = {
    statement: "'1' + '1' === '2'",
    answer: false,
    explanation: "The plus operator concatenates (joins together) strings, so '1'+'1'==='11'."
};

statement.textContent = fact.statement;
    
const disable = function (button) {
    // button.setAttribute("disabled",""); both works just fine but i like the second one.
    button.disabled = true;
}
const enable = (button) => button.disabled = false;
// button.removeAttribute("disabled"); 

function isCorrect(guess) {
    return guess === fact.answer.toString();
}

for (let button of optionButtons) {
    button.addEventListener("click", () => {
        explanation.textContent = fact.explanation;
        for (let button of optionButtons) {
            disable(button);
        }

        // button.getAttribute("value") will also work just fine
        if (isCorrect(button.value)) {
            button.classList.add("correct");
        } else {
            button.classList.add("incorrect");
        }
    });
}
