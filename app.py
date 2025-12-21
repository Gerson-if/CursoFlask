from flask import Flask, url_for, render_template, session, redirect


secretkey = "minhasenhamuitodificil"
app = Flask(__name__)

@app.route('/inicio')
def hello():
    return "<h3> Bem vindo a minha Primeira aplicação flask </h3>"

@app.route('/musicas')
def listaMusicas():
    return render_template('lista_musicas.html')


app.run(debug=True)
