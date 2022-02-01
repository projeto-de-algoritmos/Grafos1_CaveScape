
from flask import Flask, render_template, request


app = Flask(__name__)  # sempre ao iniciar um site

# criar a primeira página do site
# route -> caminho que vem depois do dominio

# funcao -> o que quero exibir naquela página
# template


@app.route('/', methods=["GET", "POST"])
def homepage():
    variavel = "Game: Cave Scape"
    if request.method == "GET":

        return render_template("homepage.html", variavel=variavel)
    else:
        no = 0
        palpite = int(request.form.get("name"))
        if no == palpite:
            return '<h1>Você Ganhou!!!<h1>'
        else:
            return '<h1>Você Perdeu!!!<h1>'


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
