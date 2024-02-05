## Uso

Antes de executar o código, é necessário gerar uma chave de criptografia.

1. Execute o seguinte código Python para gerar uma chave:

    '''
    from cryptography.fernet import Fernet

    key = Fernet.generate_key()

    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    '''

2. Agora você está pronto para usar o script de criptografia.
