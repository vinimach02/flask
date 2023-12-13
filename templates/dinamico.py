from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    opcoes_dropdown = ["Opção 1", "Opção 2", "Opção 3"]
    return render_template('index_dynamic_list.html', opcoes_dropdown=opcoes_dropdown)

if __name__ == '__main__':
    app.run(debug=True)
