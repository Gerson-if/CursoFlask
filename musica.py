from flask import Flask, url_for, render_template, redirect, request



#declaração inicial de criação da aplicação, app recebe a classe Flask
app = Flask(__name__) 


#criação de classe 
class Musica:
    #o self referencia a propia classe
    def __init__(self, nome, cantorBandaGrupo, genero): 
        self.nome = nome # classe ponto nome recebe nome, quando evocamos a classe passamos o nome para variavel responsavel.
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero
        

# aqui criamos instancias da classe Musica 
musica01 = Musica('Temporal', 'Hungria', 'Rap')
musica02 = Musica('Papai banca', 'Mc Ryan Sp', 'Funk')
musica03 = Musica('Camissa 10', 'Turma do Pagode', 'Pagode')

lista = [musica01, musica02, musica03]
#aqui criamos uma lista dos nosso objetos instanciados acima



#nossa rota incial
@app.route('/')  
def listarMusicas():
    return render_template('lista_musicas.html', 
                           titulo = 'conteudo da variavel',
                           musicas = lista)


#aqui temos a rota de cadastro de musica
# essa  rota devolve pra gente a template cadastrar_musica.htmls
@app.route('/cadastrar')
def cadastrarMusica():
    return render_template('cadastrar_musica.html')



#essa rota é responsavel pelo cadastro da nova musica
#passamos como parametro também o tipo de metodo que ela vai usar.
#note que essa rota ela e respoavel por salvar e trasferir dados.
#nesta classe tambem usamos o metodo post e nao metodo get, ou seja os dados nao sao passados por url e 
# e sim sao passados de uma maneira mais segura.
@app.route('/adicionar', methods=['POST', ])
def adicionar_musica():
    nome = request.form['txtNome'] 
    #passa o valor de txtNome da pagina cadastrar_musica.html para a variavel nome
    #esse passo de repete nas outras
    cantor = request.form['txtCantor']
    genero = request.form['txtGenero']

    #cria nova musica ou seja uma nova classe.
    novaMusica = Musica(nome, cantor, genero)

    #adiciona no fim da lista uma nova musica
    lista.append(novaMusica) 

    return redirect('/')
    #retorna a pagina inicial

#rota de login inicial reponsavel por devolver a tela de login.
@app.route('/login')
def login():
    return render_template('login.html')


#rota de autenticação responsavel pela validação de dados da tela de login.
@app.route('/autenticar', methods=['POST', ])
def autenticar():
    #se verdadeiro retorne para inicio '/'
    if request.form['txtSenha'] == 'admin':
        return redirect('/')
    else:
        # se falso retorne para login 
        return redirect('/login')

#declaração de execução da aplicação, com debug true sem necessidade de renicio para teste.
app.run(debug=True)
