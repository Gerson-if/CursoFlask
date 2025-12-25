from flask import Flask, url_for, render_template, session, redirect


secretkey = "minhasenhamuitodificil"
app = Flask(__name__)

class Musica:
    def __init__(self, nome, cantorBandaGrupo, genero):
        self.nome = nome
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero
        





@app.route('/musicas')
def listarMusicas():
    musica01 = Musica('Temporal', 'Hungria', 'Rap')
    musica02 = Musica('Papai banca', 'Mc Ryan Sp', 'Funk')
    musica03 = Musica('Camissa 10', 'Turma do Pagode', 'Pagode')

    lista = [musica01, musica02, musica03]

    return render_template('lista_musicas.html', 
                           titulo = 'conteudo da variavel',
                           musicas = lista)


app.run(debug=True)
