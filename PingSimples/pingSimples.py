import os   # Importar o módulo ou biblioteca os (integra os programas e recursos do S.O.)

print("#" * 60)

# Criação da variável que vai receber um ip do usuário
ip_ou_host = input("Digite o IP ou HOST a ser verificado: ")

print("-" * 60)

# Chamando o módulo system da biblioteca os
# Chamando o comando ping com 6 pacotes
os.system(f'ping -c 6 {ip_ou_host}')

print("-" * 60)