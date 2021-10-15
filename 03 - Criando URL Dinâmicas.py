from os import write
from flask import Flask

app = Flask(__name__)

@app.route('/')
def escreve():
    return 'Escreve alguma coisa ai!!'


@app.route('/hello/')
@app.route('/hello/<nome>')
def hello(nome=''):
    return f'<h1>Hello {nome}</h1>'


@app.route('/conta/')
def conta1():
    return f'<h1>Escreva um número na frente da URL para fazer a comparação</h1>'

@app.route('/conta/<int:num>')
def conta(num= 5):
    if num > 5:
        return f'<h1>O número é maior</h1>'
    elif num == 5:
        return f'<h1>O número igual</h1>'
    else:
        return f'<h1>O numero é menor</h1>'

if __name__ == '__main__':
    app.run(debug= True, port='3000')
