# EXERCICIO 1.3: Parâmetros na URL (rotas dinâmicas)
# Crie uma rota /saudacao/<nome> que retorna "Olá, <nome>! Seja bem-vindo!".

from flask import Flask

app = Flask(__name__)  # representa o nome do arquivo
# o código deve ser escrito entre o app e o app.run

@app.route('/')  # @decorador de função
def home():
    return 'Olá Mundo!'

@app.route('/sobre')
def sobre():
    return "Olá, meu nome é Alexsandra e sou uma desenvolvedora Python."

@app.route('/saudacao/<nome>')  # para abrir a página precisamos adicionar o nome
def saudacao(nome):
    return f'Olá {nome}! Tudo bem?'

if __name__ == '__main__':
    app.run(debug=True)