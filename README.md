# ESTE DOCUMENTO INCLUI ALTERAÇÕES E INCLUSÕES, EXPLICAÇÕES, DEFINIÇÕES DO CURSO FLASK
- Na linha 1 do nosso programa principal, importamos o modulo flask e depois no import, importamos a classe Flask, os demais como url_for ou render_template são as funções da classe flask que invocamos em dado momento nas rotas que vamos criar.
- No diretorio static estamos usando o bootstrap para estilização, nas paginas html linkamos ele com o url_for
- No html passamos comandos e variaveis atraves de {% bloco de comando %} ou {{ nome da variavel}}, podemos tambem criar uma lista dentro das funcoes de devolver isso no return atraves das variaveis para o html.
- Sobre o diretorio static, nos temos nele as pastas: bootstrap-icons, css, img, js ; aqui estas mesmas sao do bootstrap ferrementa esta que ajuda na estilização das paginas html, usando as url dinanmicas no caso url_for, assim dizemos ao html onde estao estes arquivos: 

```
<link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap-icons/bootstrap-icons.css') }}">
<script src="{{ url_for('static', filename='js/bootstrap.min.js') }}"></script>

```

 - Sobre clases e obejetos, podemos criar uma nova classe e retorna este mesmo em uma rota para devolver o mesmo para uma template html, a classe em si pode ser estanciada e usada em uma lista a mesma lista e devolvida para o html, onde acessamos o atributo da classe em questao cujo sera percorrido ou consultado dependendo da estrutura de dados:
 exemplo:

 ```
 class Musica:
    def __init__(self, nome, cantorBandaGrupo, genero):
        self.nome = nome
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero
        

musica01 = Musica('Temporal', 'Hungria', 'Rap')
musica02 = Musica('Papai banca', 'Mc Ryan Sp', 'Funk')
musica03 = Musica('Camissa 10', 'Turma do Pagode', 'Pagode')
```
- Observamos aqui a criação de uma nova classe, e novos obejetos sendo criados a parti de uma estancia.
- posterior a isso temos a funcao e o trexo que faz uso dessas informações:


```
@app.route('/musicas')
def listarMusicas():
    lista = [musica01, musica02, musica03]

    return render_template('lista_musicas.html', 
                           titulo = 'conteudo da variavel',
                           musicas = lista)
                           ```
```
- E no html: 

```
 {% for music in musicas %}
        <tr><!-- segunda linha-->
            <td>{{ music.nome }}</td> <!-- variavel music sendo percorrido pelo laço for-->
            <!-- alem disso acessamos o atributo do objeto music, pois este mesmo é que esta sendo percorrido-->
            <td>{{ music.cantorBanda }}</td>
            <td>{{ music.genero }}</td>
        </tr>
        {% endfor %}

``` 
