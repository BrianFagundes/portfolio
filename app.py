from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Executa a aplicação na porta 8181 e permite acesso externo
    app.run(host='0.0.0.0', port=8181, debug=True)
