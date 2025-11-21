from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    # Renderiza o arquivo index.html dentro da pasta templates
    return render_template('index.html')

if __name__ == '__main__':
    # Roda o servidor de desenvolvimento
    app.run(debug=True)