# ESTE DOCUMENTO INCLUI ALTERAÇÕES E INCLUSÕES, EXPLICAÇÕES, DEFINIÇÕES DO CURSO FLASK
- Na linha 1 do nosso programa principal, importamos o modulo flask e depois no import, importamos a classe Flask, os demais como url_for ou render_template são as funções da classe flask que invocamos em dado momento nas rotas que vamos criar.
- No diretorio static estamos usando o bootstrap para estilização, nas paginas html linkamos ele com o url_for
- No html passamos comandos e variaveis atraves de {% bloco de comando %} ou {{ nome da variavel}}, podemos tambem criar uma lista dentro das funcoes de devolver isso no return atraves das variaveis para o html.
- Sobre o diretorio static, nos temos nele as pastas: bootstrap-icons, css, img, js ; aqui estas mesmas sao do bootstrap ferremente esta que ajuda na estilização das paginas html, e usando as url dinamicas no caso url_for dizemos ao html onde estao estes arquivos: 

```
<link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap-icons/bootstrap-icons.css') }}">
<script src="{{ url_for('static', filename='js/bootstrap.min.js') }}"></script>

```