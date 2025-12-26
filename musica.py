from flask import Flask, url_for, render_template, session, redirect, request




secretkey = "minhasenhamuitodificil"
app = Flask(__name__)



class Musica:
    def __init__(self, nome, cantorBandaGrupo, genero):
        self.nome = nome
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero
        

musica01 = Musica('Temporal', 'Hungria', 'Rap')
musica02 = Musica('Papai banca', 'Mc Ryan Sp', 'Funk')
musica03 = Musica('Camissa 10', 'Turma do Pagode', 'Pagode')

lista = [musica01, musica02, musica03]




@app.route('/musicas')
def listarMusicas():
    return render_template('lista_musicas.html', 
                           titulo = 'conteudo da variavel',
                           musicas = lista)


@app.route('/cadastrar')
def cadastrarMusica():
    return render_template('cadastrar_musica.html')


@app.route('/adicionar', methods='POST, ')
def adicionar_musica():
    nome = request.form('txtNome')
    cantor = request.form('txtCantor')
    genero = request.form('txtGenero')

    novaMusica = Musica(nome, cantor, genero) #cria nova musica
    lista.append(novaMusica) #adiciona no fim da lista

    return render_template('lista_musicas.html')

app.run(debug=True)
