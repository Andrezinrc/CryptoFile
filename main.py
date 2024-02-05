from cryptography.fernet import Fernet
from colorama import Fore, Back, Style

# Função para gerar ou carregar a chave
def obter_chave():
    try:
        # Tenta ler a chave do arquivo
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
    except FileNotFoundError:
        # Se o arquivo não existir, gera uma nova chave
        key = Fernet.generate_key()
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)
    
    return Fernet(key)

# Função para criptografar um arquivo
def criptografar_arquivo(caminho_arquivo, fernet):
    try:
        with open(caminho_arquivo, 'rb') as file:
            original = file.read()
        
        #criptografar arquivo
        encrypted = fernet.encrypt(original)

        with open(caminho_arquivo, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        
        print(f"{Fore.GREEN}Arquivo {caminho_arquivo} criptografado com sucesso!{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}Arquivo {caminho_arquivo} não encontrado.{Style.RESET_ALL}")

# Função para descriptografar um arquivo
def descriptografar_arquivo(caminho_arquivo, fernet):
    try:

        with open(caminho_arquivo, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        
        # Descriptografar o arquivo
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(caminho_arquivo, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
        
        print(f"{Fore.GREEN}Arquivo {caminho_arquivo} descriptografado com sucesso!{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}Arquivo {caminho_arquivo} não encontrado.{Style.RESET_ALL}")

if __name__ == "__main__":
    from colorama import init
    init(autoreset=True)

    diretorio = input(f"{Fore.CYAN}Digite o diretório do arquivo: {Style.RESET_ALL}")

    nome_arquivo = input(f"{Fore.CYAN}Digite o nome do arquivo: {Style.RESET_ALL}")

    caminho_arquivo = f"{diretorio}/{nome_arquivo}"

    # Obter a chave Fernet
    fernet = obter_chave()

    opcao = input(f"{Fore.CYAN}Escolha uma opção (1 para Criptografar, 2 para Descriptografar): {Style.RESET_ALL}")

    if opcao == '1':
        criptografar_arquivo(caminho_arquivo, fernet)
    elif opcao == '2':
        descriptografar_arquivo(caminho_arquivo, fernet)
    else:
        print(f"{Fore.RED}Opção inválida.{Style.RESET_ALL}")
