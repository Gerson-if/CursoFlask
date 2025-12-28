# ESTE DOCUMENTO INCLUI ALTERAÇÕES E INCLUSÕES, EXPLICAÇÕES, DEFINIÇÕES DO CURSO FLASK
## Conforme o curso avança as informações do documento seram modificadas, dada a interpretação obtida.
- Na linha 1 do nosso programa principal, importamos o modulo flask e depois no import, importamos a classe Flask, os demais como url_for ou render_template são as funções da classe flask que invocamos em dado momento nas rotas que vamos criar.
- No diretorio static estamos usando o bootstrap para estilização, nas paginas html linkamos ele com o url_for
- No html passamos comandos e variaveis atraves de {% bloco de comando %} ou {{ nome da variavel}}, podemos tambem criar uma lista dentro das funcoes de devolver isso no return atraves das variaveis para o html.
- Sobre o diretorio static, nos temos nele as pastas: bootstrap-icons, css, img, js ; aqui estas mesmas sao do bootstrap ferrementa esta que ajuda na estilização das paginas html, usando as url dinanmicas no caso url_for, assim dizemos ao html onde estao estes arquivos: 

```
<link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap-icons/bootstrap-icons.css') }}">
<script src="{{ url_for('static', filename='js/bootstrap.min.js') }}"></script>

```

 - Sobre clases e objetos, podemos criar uma nova classe e retorna este mesmo em uma rota para devolver o mesmo para uma template html, a classe em si pode ser estanciada e usada em uma lista a mesma lista e devolvida para o html, onde acessamos o atributo da classe em questao cujo sera percorrido ou consultado dependendo da estrutura de dados:
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
- Template Cadastrar_musica.html é resposavel pelo cadastro das novas musicas, na mesma pagina usamos um formulario, com nomes dos dados que seram enseridos, alem disso o botao é do tipo submit pois os dados seram enviados em dado momento.

- incialmente apos a criação do form, vamos assimilar o uso dos metodos GET E POST, para o envio e recuperação de dados, no formulario, no metodo Get incialmente o padrao este passa os dados pela ulr, ja no POst os dados sao passados para outra pagina ou template.

- Na rota de criação de uma nova musica, utilizamos uma função, que usa o request, que importamos no começo do codigo, ou seja nessa função vamos pegar os dados do formulario, recuperar os dados e depois devolver usar estes dados em outra template, alem disso usamos estes dados para prencher uma lista, ou seja acrecentamos estes mesmo dados ao final de uma lista. No formulario html precisamos tambem indicar no html que ele usara o metodo POST e nao get, e tambem nomear os inputs do html, ou seja temos como se fosse indentificadores para armazenar e trasmitir os dados, e depois recuperar e gravar e exibir os mesmos. Alem disso para que isso tudo ocorra bem precisamos indicar na Rota que trata de tudo isso, o tipo de metodo que sera usado na pagina de destino que evoca esta rota em questao, alem disso dentro do form precisamos definir sua action quando precionamos o botao cadastrar desta forma: 

```
 <form  action="/adicionar" method="post"> 
 
``` 
- Na pagina de Cadastrar musica e lista_musicas incialmente ja começãmos a usar as clases do bootstrap para estilização no entanto o uso por enquanto e limitado ja que o foco central é o entendimento sistemico de como o flask, a consulta de dados exibição e criação de dados fucionam, essa visão sistemica possibilitara novas criaçãoes de novos sistemas a parti deste.






