from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_password(key, password):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(password.encode('utf-8'))
    return cipher_text

def decrypt_password(key, cipher_text):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text).decode('utf-8')
    return plain_text

# Exemplo de como usar:
# Passo 1: Gerar uma chave
key = generate_key()

# Passo 2: Criptografar a senha
senha_original = "minha_senha_secreta"
senha_cifrada = encrypt_password(key, senha_original)
print("Senha criptografada:", senha_cifrada)

# Agora, você pode armazenar 'key' e 'senha_cifrada' no seu arquivo de configuração
# ...

# Passo 3: Descriptografar a senha quando necessário
senha_recuperada = decrypt_password(key, senha_cifrada)
print("Senha descriptografada:", senha_recuperada)
