from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def admin():
    return '<h1>Admin</h1>'


@app.route('/guest/<guest>')
def guest(guest):
    return f'<h1>Bem vindo {guest}</h1>'


@app.route('/user/<nome>')
def user(nome):
    if nome == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest',guest= nome ))

@app.route('/google')
def google():
    return redirect('http://google.com')


if __name__ == '__main__':
    app.run(debug=True, port='3000')
