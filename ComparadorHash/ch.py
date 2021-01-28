import hashlib

arquivo1 = 'primeiro.txt'
arquivo2 = 'segundo.txt'

hash1 = hashlib.new('SHA1')
hash1.update(open(arquivo1, 'rb').read())     # Leitura em Modo Binário

hash2 = hashlib.new('SHA1')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():       # digest: resumido
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print('O hash do aquivo primeiro.txt é: ', hash1.hexdigest())
    print('O hash do aquivo segundo.txt é: ', hash2.hexdigest())
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo {arquivo2}')
    print('O hash do aquivo primeiro.txt é: ', hash1.hexdigest())
    print('O hash do aquivo segundo.txt é: ', hash2.hexdigest())