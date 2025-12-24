from flask import Flask, url_for, render_template, session, redirect


secretkey = "minhasenhamuitodificil"
app = Flask(__name__)


@app.route('/musicas')
def listarMusicas():
    lista = ['Terror da Previdencia', 'Lobo Guara', 'Vai e chora']

    return render_template('lista_musicas.html', 
                           titulo = 'conteudo da variavel',
                           musicas = lista)


app.run(debug=True)
