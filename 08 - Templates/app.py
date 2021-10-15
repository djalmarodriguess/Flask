from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    x = 50
    y = 10
    return render_template('modelo.html', x= x, z= y)


if __name__=='__main__':
    app.run(debug= True)