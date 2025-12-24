from flask import Flask, url_for, render_template, session, redirect


secretkey = "minhasenhamuitodificil"
app = Flask(__name__)


@app.route('/musicas')
def listaMusicas():
    return render_template('lista_musicas.html', 
                           titulo = 'conteudo da variavel')



app.run(debug=True)
