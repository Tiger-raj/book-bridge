let doneBtn = document.querySelector(".submit-btn");

function editInfo() {
  doneBtn.classList.remove("hidden");
  const nodeList = document.querySelectorAll("input");
  for (let i = 0; i < nodeList.length; i++) {
    nodeList[i].removeAttribute("readonly");
  }
}
function doneInfo() {
  doneBtn.classList.add("hidden");
  const nodeList = document.querySelectorAll("input");
  for (let j = 0; j < nodeList.length; j++) {
    nodeList[j].setAttribute("readonly", "readonly");
  }
  //   nodeList[0].setAttribute("readonly", "readonly");
}
