const slider = document.getElementById("myRange");
const output = document.getElementById("bottles");
output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = this.value;
}