def carro1(velocidade):
    trajeto = 0

    while trajeto <= 100:
        print('Carro 1: ', trajeto)
        trajeto += velocidade


def carro2(velocidade):
    trajeto = 0

    while trajeto <= 100:
        print('Carro 2: ', trajeto)
        trajeto += velocidade

carro1(10)
carro2(20)