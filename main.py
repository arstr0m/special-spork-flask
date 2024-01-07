from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '¡Hola, mundo! Esta es mi primera página web con Flask.'

if __name__ == '__main__':
    app.run(debug=True)
