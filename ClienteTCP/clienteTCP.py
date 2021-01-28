import socket   # Fazer a relação entre a placa de rede e o S.O.
import sys      # Fornece o acesso à algumas variáveis que possuem interação com o interpretador

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!")
        print(f"Erro: {e}")
        sys.exit()

    print("Socket criado com sucesso!")

    HostAlvo = input("Digite o Host ou Ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host: " + HostAlvo + " e na Porta: " + PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar no Host: " + HostAlvo + " - Porta: " + PortaAlvo)
        print(f"Erro: {e}")
        sys.exit()

if __name__ == "__main__":
    main()
