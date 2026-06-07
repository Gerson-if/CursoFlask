from flask import Flask, url_for, render_template, redirect, request, flash

# Cria a aplicação Flask
app = Flask(__name__)

app.secret_key = 'minhassenhamuitodificildaplicacao'

# Classe que representa uma música
class Musica:

    # Inicializa os atributos do objeto
    def __init__(self, nome, cantorBandaGrupo, genero):
        self.nome = nome
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero


# Objetos criados a partir da classe Musica
musica01 = Musica('Temporal', 'Hungria', 'Rap')
musica02 = Musica('Papai banca', 'Mc Ryan Sp', 'Funk')
musica03 = Musica('Camissa 10', 'Turma do Pagode', 'Pagode')

# Lista de músicas
lista = [musica01, musica02, musica03]


# Página inicial
@app.route('/')
def listarMusicas():
    return render_template(
        'lista_musicas.html',
        titulo='conteudo da variavel',
        musicas=lista
    )


# Exibe a página de cadastro
@app.route('/cadastrar')
def cadastrarMusica():
    return render_template('cadastrar_musica.html')


# Recebe os dados do formulário e adiciona uma nova música
@app.route('/adicionar', methods=['POST'])
def adicionar_musica():

    # Recupera os dados enviados pelo formulário
    nome = request.form['txtNome']
    cantor = request.form['txtCantor']
    genero = request.form['txtGenero']

    # Cria um novo objeto Musica
    novaMusica = Musica(nome, cantor, genero)

    # Adiciona o objeto à lista
    lista.append(novaMusica)

    # Retorna para a página inicial
    return redirect(url_for('listar_musicas'))


# Exibe a tela de login
@app.route('/login')
def login():
    return render_template('login.html')


# Valida os dados do login
@app.route('/autenticar', methods=['POST'])
def autenticar():

    if request.form['txtSenha'] == 'admin':
        return redirect(url_for('listarMusicas'))

    else:
        return redirect(url_for('login'))


# Inicia a aplicação
app.run(debug=True)
