from flask import Flask, render_template
import os

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    # Renderiza o arquivo index.html dentro da pasta templates
    return render_template('index.html')

if __name__ == '__main__':
    # O modo de depuração é ativado se a variável de ambiente FLASK_DEBUG for '1'
    debug_mode = os.environ.get('FLASK_DEBUG') == '1'
    app.run(debug=debug_mode)