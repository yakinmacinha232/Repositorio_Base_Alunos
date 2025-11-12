# Exercício 3.1: Templates com variáveis
# Modifique o template para receber o nome como variável e exibir: "Bem-vindo, {{nome}}"

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou aluno do projeto Fábrica de Programadores.'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return render_template('ex_3-1.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
