import os
import pyaes 



def decrypt(file_txt='teste.txt'):
    #Arquivo criptografado
    file_name = file_txt
    file = open(file_name,'rb')
    file_data = file.read()
    file.close()


    #chave para descriptografar
    key = b'testeransomwares'
    aes = pyaes.AESModeOfOperationCTR(key)
    decript_data = aes.decrypt(file_data)

    os.remove(file_name)


    #criando o arquivo descriptografado
    new_file = 'teste.txt'
    new_file = open(f'{new_file}','wb')
    new_file.write(decript_data)
    new_file.close()