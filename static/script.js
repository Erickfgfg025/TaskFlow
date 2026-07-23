function addTask() {
    const input = document.getElementById("input");
    const texto = input.value.trim();

    if (!texto) return;

    const lista = document.querySelector(".lista");

    const label = document.createElement("label");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";

    const span = document.createElement("span");
    span.textContent = texto;

    label.appendChild(checkbox);
    label.appendChild(span);

    lista.appendChild(label);

    input.value = "";
}
