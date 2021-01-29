from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0

    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} km: {} \n'.format(piloto, trajeto))

tdCarro1 = Thread(target=carro, args=[5, 'Bruno'])      # args => argumentos da função carro
tdCarro2 = Thread(target=carro, args=[5.5, 'Python'])

tdCarro1.start()
tdCarro2.start()
