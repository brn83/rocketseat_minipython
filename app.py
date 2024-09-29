# Importação da classe Flask
from flask import Flask


# Instanciar a classe Flask
app = Flask(__name__)


# Definição de rota raiz e função a ser executada
@app.route('/')
def hello_world():
    return 'Hello World'


# Ativar a aplicação em modo debug
if __name__ == "__main__":
    app.run(debug=True)
