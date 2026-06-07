# Anotações do Curso Flask

> **Observação:** Este documento representa minha interpretação atual do conteúdo estudado. Conforme eu avançar no curso e adquirir mais conhecimento, algumas informações poderão ser corrigidas, complementadas ou reorganizadas.

---

# Introdução ao Flask

Na primeira linha do programa normalmente importamos elementos do Flask:

```python
from flask import Flask, render_template, url_for, redirect, request
```

## O que cada item faz?

* `Flask`: classe utilizada para criar a aplicação.
* `render_template()`: renderiza páginas HTML.
* `url_for()`: gera URLs dinâmicas.
* `redirect()`: redireciona o usuário para outra rota.
* `request`: permite acessar dados enviados pelo usuário.

---

# Diretório Static

O diretório `static` é utilizado para armazenar arquivos estáticos da aplicação.

Exemplos:

```text
static/
├── bootstrap-icons/
├── css/
├── img/
└── js/
```

Neste projeto estamos utilizando o Bootstrap para auxiliar na estilização das páginas HTML.

Para acessar esses arquivos usamos a função `url_for()`:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap-icons/bootstrap-icons.css') }}">
<script src="{{ url_for('static', filename='js/bootstrap.min.js') }}"></script>
```

Dessa forma o Flask localiza corretamente os arquivos dentro da pasta `static`.

---

# Templates HTML e Jinja

Nas páginas HTML podemos utilizar a sintaxe do mecanismo de templates do Flask (Jinja).

## Exibir variáveis

```html
{{ titulo }}
```

## Executar comandos

```html
{% for item in lista %}
{% endfor %}
```

Através desses recursos podemos exibir informações enviadas pelas rotas Python.

---

# Classes e Objetos

Podemos criar classes para representar entidades do sistema.

Exemplo:

```python
class Musica:
    def __init__(self, nome, cantorBandaGrupo, genero):
        self.nome = nome
        self.cantorBanda = cantorBandaGrupo
        self.genero = genero
```

Criando objetos:

```python
musica01 = Musica('Temporal', 'Hungria', 'Rap')
musica02 = Musica('Papai Banca', 'Mc Ryan SP', 'Funk')
musica03 = Musica('Camisa 10', 'Turma do Pagode', 'Pagode')
```

Neste caso:

* `Musica` é a classe.
* `musica01`, `musica02` e `musica03` são objetos criados a partir da classe.

---

# Enviando Objetos para o HTML

Podemos criar uma lista contendo objetos e enviá-la para uma página HTML.

Exemplo:

```python
@app.route('/musicas')
def listarMusicas():
    lista = [musica01, musica02, musica03]

    return render_template(
        'lista_musicas.html',
        titulo='Conteúdo da variável',
        musicas=lista
    )
```

A variável `musicas` será recebida pelo template HTML.

---

# Percorrendo Objetos no HTML

```html
{% for music in musicas %}
<tr>
    <td>{{ music.nome }}</td>
    <td>{{ music.cantorBanda }}</td>
    <td>{{ music.genero }}</td>
</tr>
{% endfor %}
```

Neste exemplo:

* O laço percorre cada objeto da lista.
* A variável `music` representa o objeto atual.
* Podemos acessar seus atributos utilizando a notação de ponto.

---

# Cadastro de Músicas

A página `cadastrar_musica.html` é responsável pelo cadastro de novas músicas.

Nela utilizamos um formulário HTML:

```html
<form action="/adicionar" method="post">
```

O botão de envio normalmente possui:

```html
<button type="submit">
    Cadastrar
</button>
```

---

# Métodos GET e POST

## GET

* Método padrão dos formulários.
* Os dados aparecem na URL.
* Geralmente utilizado para consultas.

Exemplo:

```text
/site?nome=Gerson
```

## POST

* Utilizado para enviar informações ao servidor.
* Os dados não aparecem na URL.
* Muito utilizado em cadastros e autenticação.

---

# Recuperando Dados do Formulário

Para acessar os dados enviados pelo formulário utilizamos o objeto `request`.

Exemplo:

```python
nome = request.form['nome']
```

Os nomes definidos nos campos HTML servem como identificadores para recuperar as informações.

Exemplo:

```html
<input type="text" name="nome">
```

---

# Redirecionamento

Após adicionar uma música utilizamos:

```python
return redirect('/')
```

Isso evita que o navegador envie novamente os dados ao pressionar F5.

Fluxo simplificado:

```text
Formulário
     ↓
POST
     ↓
Processamento
     ↓
Redirect
     ↓
Nova página
```

---

# Uso Inicial do Bootstrap

Neste momento do curso o Bootstrap está sendo utilizado apenas para introduzir conceitos básicos de estilização.

O foco principal ainda está em compreender:

* Rotas
* Templates
* Formulários
* Classes
* Objetos
* Fluxo de dados

A estilização será aprofundada posteriormente.

---

# Rota Principal

Inicialmente utilizávamos:

```python
@app.route('/musicas')
```

Depois alteramos para:

```python
@app.route('/')
```

Assim, ao iniciar a aplicação, o usuário acessa diretamente a página principal.

---

# Responsabilidade das Rotas

Uma observação importante aprendida durante o curso é que cada rota possui uma responsabilidade específica.

Exemplo:

### Exibir tela de login

```python
@app.route('/login')
def login():
    return render_template('login.html')
```

### Validar usuário e senha

```python
@app.route('/autenticar', methods=['POST'])
def autenticar():
    pass
```

Embora trabalhem juntas, cada rota possui uma função diferente dentro da aplicação.

Esse conceito ajuda na organização e manutenção do sistema.

---

# Conclusão

Até este ponto do curso estou compreendendo principalmente:

* Como criar rotas.
* Como renderizar templates HTML.
* Como enviar dados do Python para o HTML.
* Como receber dados de formulários.
* Como utilizar GET e POST.
* Como utilizar classes e objetos.
* Como organizar melhor as responsabilidades das rotas.

Estas anotações representam meu entendimento atual e serão atualizadas conforme o avanço dos estudos.
