from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    opcoes_dropdown = ["Opção 1", "Opção 2", "Opção 3"]
    return render_template('index.html', opcoes_dropdown=opcoes_dropdown)

@app.route('/atualizar_dropdown2', methods=['POST'])
def atualizar_dropdown2():
    valor_dropdown1 = request.form.get('valor_dropdown1')
    opcoes_dropdown2 = obter_opcoes_dropdown2(valor_dropdown1)
    return jsonify(opcoes_dropdown2=opcoes_dropdown2)

def obter_opcoes_dropdown2(valor_dropdown1):
    if valor_dropdown1 == "Opção 1":
        return ["Subopção 1.1", "Subopção 1.2"]
    elif valor_dropdown1 == "Opção 2":
        return ["Subopção 2.1", "Subopção 2.2"]
    elif valor_dropdown1 == "Opção 3":
        return ["Subopção 3.1", "Subopção 3.2"]
    else:
        return []

if __name__ == '__main__':
    app.run(debug=True)
