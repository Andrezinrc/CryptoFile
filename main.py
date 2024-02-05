from cryptography.fernet import Fernet
from colorama import Fore, Style
import os

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

        # Criptografar arquivo
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

# Função para processar arquivos em um diretório
def processar_arquivos_no_diretorio(diretorio, fernet, funcao_processamento):
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_arquivo):
            funcao_processamento(caminho_arquivo, fernet)

if __name__ == "__main__":
    from colorama import init
    init(autoreset=True)

    print(f"{Fore.YELLOW}Bem-vindo ao CryptoFile!{Style.RESET_ALL}")

    diretorio = input(f"{Fore.CYAN}Digite o diretório do arquivo ou pasta (exemplo: /caminho/para/pasta): {Style.RESET_ALL}")

    nome_arquivo = input(f"{Fore.CYAN}Digite o nome do arquivo (se for um arquivo) ou pressione Enter se for uma pasta: {Style.RESET_ALL}")

    caminho_arquivo = os.path.join(diretorio, nome_arquivo) if nome_arquivo else diretorio

    # Obter a chave Fernet
    fernet = obter_chave()

    opcao = input(f"{Fore.CYAN}Escolha uma opção (1 para Criptografar, 2 para Descriptografar): {Style.RESET_ALL}")

    if opcao == '1':
        if os.path.isdir(caminho_arquivo):
            print(f"{Fore.YELLOW}Criptografando todos os arquivos em {caminho_arquivo}...{Style.RESET_ALL}")
            processar_arquivos_no_diretorio(caminho_arquivo, fernet, criptografar_arquivo)
        else:
            criptografar_arquivo(caminho_arquivo, fernet)
    elif opcao == '2':
        if os.path.isdir(caminho_arquivo):
            print(f"{Fore.YELLOW}Descriptografando todos os arquivos em {caminho_arquivo}...{Style.RESET_ALL}")
            processar_arquivos_no_diretorio(caminho_arquivo, fernet, descriptografar_arquivo)
        else:
            descriptografar_arquivo(caminho_arquivo, fernet)
    else:
        print(f"{Fore.RED}Opção inválida.{Style.RESET_ALL}")
