from threading import Thread
import time


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 30:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Piloto: {piloto} KM: {trajeto}')


t_carro1 = Thread(target=carro, args=[1, 'Alex'])
t_carro2 = Thread(target=carro, args=[1.5, 'Pamela'])

t_carro1.start()
t_carro2.start()
