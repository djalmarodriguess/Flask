from flask import Flask, redirect, request, url_for, abort

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['pass'] == 'admin':
            return redirect(url_for('sucesso'))
        else:
            return abort(401)
    else:
        abort(404)


@app.route('/sucesso')
def sucesso():
    return 'Sucesso'

if __name__== "__main__":
    app.run(debug=True)