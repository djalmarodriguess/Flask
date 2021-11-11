from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/<nome>')
def usuarios(nome):
    return render_template('usuarios.html',  nome = nome)
    
app.route('/<int:num>/<int:num>')
def soma(num1,num2):
    return render_template('soma.html', num1= num1, num2= num2)

if __name__ == '__main__':
    app.run(debug=True)