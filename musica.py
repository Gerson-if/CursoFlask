from flask import Flask, url_for, render_template, redirect, request




secretkey = "minhasenhamuitodificil"
app = Flask(__name__)



class Musica: # criação de classe 
    def __init__(self, nome, cantorBandaGrupo, genero): # o self referencia a propia classe 
        self.nome = nome
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero
        

# aqui criamos instancias da classe Musica 
musica01 = Musica('Temporal', 'Hungria', 'Rap')
musica02 = Musica('Papai banca', 'Mc Ryan Sp', 'Funk')
musica03 = Musica('Camissa 10', 'Turma do Pagode', 'Pagode')

lista = [musica01, musica02, musica03] # aqui criamos uma lista dos nosso obejtos estanciados acima




@app.route('/') # nossa rota incial 
def listarMusicas():
    return render_template('lista_musicas.html', 
                           titulo = 'conteudo da variavel',
                           musicas = lista)


@app.route('/cadastrar')
def cadastrarMusica():
    return render_template('cadastrar_musica.html')


@app.route('/adicionar', methods=['POST', ])
def adicionar_musica():
    nome = request.form['txtNome'] # passa o valor de txtNome da pagina cadastrar_musica.html para a var nome
    cantor = request.form['txtCantor']
    genero = request.form['txtGenero']

    novaMusica = Musica(nome, cantor, genero) #cria nova musica
    lista.append(novaMusica) #adiciona no fim da lista

    return redirect('/')

app.run(debug=True)
