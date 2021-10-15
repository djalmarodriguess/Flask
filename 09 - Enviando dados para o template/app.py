from flask import *

app = Flask(__name__,template_folder = 'templates')

@app.route('/')
def notas():
    return render_template('notas.html')


@app.route('/notas', methods=['POST'])
def soma():
    total = sum([int(v) for v in request.form.to_dict().values()])
    return render_template('soma.html', total=total)

if __name__=='__main__':
    app.run(debug=True)