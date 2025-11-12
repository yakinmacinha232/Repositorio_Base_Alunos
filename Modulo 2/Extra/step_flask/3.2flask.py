# Exercício 3.2: Templates com estrutura de controle
# Passe uma lista de nomes para o template e use um for em Jinja
# para listar todos os nomes em um <ul> (lista não ordenada)

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')  # primeira página (home ou index)
def index():
    return 'Hello Flask'

@app.route('/sobre')  # segunda página
def sobre():
    return 'Olá, eu sou aluno do projeto Fábrica de Programadores.'

@app.route('/lista')  # terceira página
def lista():
    alunos = ['Abed', 'Rafael', 'Helena', 'Renan', 'Felipe', 'Enzo', 'Guilherme', 'Jorge', 'Igor', 'Emanuel', 'Caio']
    return render_template('ex_3-2.html', lista=alunos)

if __name__ == '__main__':
    app.run(debug=True)
