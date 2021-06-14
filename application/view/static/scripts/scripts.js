function mostraImagem(img) {
		var imagem = document.getElementById("img_selected");
		imagem.src = img;
}

var btn = document.querySelector("#botao_menu");
btn.addEventListener("click", function() {
    var div = document.querySelector("#dropdown-content");

  if(div.style.display === "none") {
        div.style.display = "block";
    } else {
      div.style.display = "none";
  }

});