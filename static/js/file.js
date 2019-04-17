function showName() {
  var path = document.getElementById("imageName").value;
  var filename = path.replace("C:\\fakepath\\", "");
  document.getElementById("nombre").innerHTML = filename;
}