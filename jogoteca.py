from flask import Flask, render_template, request, redirect, session, flash, url_for
# render_template Para trabalhar com os templates do HTML automaticamente
# Requests para pegar as informnações enviadas
# redirect para redirecionar páginas 
# session permite reter informação por mais de um ciclo de request, armazenando nos cookies do navegador
# flash permite enviar mensagem na tela
# url_for - Dinamisar as urls de rediret chamando a funçao

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atarai')
jogo2 = Jogo('Street Fighter','Luta', 'Super Nintendo')
jogo3 = Jogo('Fifa', 'Esportes', 'PS3')
lista = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

# Valores Usuarios
ususario1 = Usuario("Vinicius Machado", "VM", "senhamestre")
ususario2 = Usuario("Mariana Monteiro", "Mari", "familia")
ususario3 = Usuario("Rafael Monteiro Machado", "Rafa", "papainoel")

#Dictionary
usuarios = { ususario1.nickname : ususario1,
             ususario2.nickname : ususario2,
             ususario3.nickname : ususario3 }

app = Flask(__name__) #__name__ faz uma referência ao próprio arquivo e garante que irá rodar a aplicação
app.secret_key = 'mach'


# Criar uma rota
@app.route('/')
#Quando criamos uma rota, precisamos de uma função
def index():
    #lista = ['Tetris', 'Street Fighters', 'Crash'] # Criando lista
    return render_template('lista.html', titulo='Jogos', jogos=lista) # O render template passa o valor da variável para o HTML

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None: #se nao houver nenhuma chave chamado usuario_logado na sessão entao redireciona para pg de login
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + " Usuario logado com sucesso")
            proxima_pagina = request.form
    else:
        flash('Usuario não logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))

app.run() # Para rodar a aplicaçao Para alterar a porta podemos colocar dentro do run app.run(host0'0.0.0.0', port=8080)