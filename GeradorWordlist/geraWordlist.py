import itertools

string = input('Digite a string a ser permutada: ')

resultado = itertools.permutations(string, len(string))     # Gera uma palavra de len(string) caracteres com essa string

for i in resultado:
    print(''.join(i))
