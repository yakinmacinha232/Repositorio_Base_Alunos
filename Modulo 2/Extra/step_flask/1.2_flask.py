# EXERCICIO 1.2: Rota personalizada
# Adicione uma nova rota '/sobre' que retorna uma mensagem
# com seu nome e uma frase sobre você.

from flask import Flask

app = Flask(__name__)  # representa o nome do arquivo
# o código deve ser escrito entre o app e o app.run

@app.route('/')  # @decorador de função
def home():
    return 'Olá Mundo!'

@app.route('/sobre')
def sobre():
    return "Olá, meu nome é Alexsandra e sou uma desenvolvedora Python."

if __name__ == '__main__':
    app.run(debug=True)