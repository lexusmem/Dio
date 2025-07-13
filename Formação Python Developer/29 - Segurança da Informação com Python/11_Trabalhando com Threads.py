from threading import Thread
import time


def carro(velocidade, piloto):
    trajeto = 0

    while trajeto < 100:
        trajeto_futuro = trajeto + velocidade

        if trajeto_futuro >= 100:
            trajeto_para_imprimir = 100
        else:
            trajeto_para_imprimir = trajeto_futuro

        print(f'Piloto: {piloto} Km: {trajeto_para_imprimir}')

        trajeto = trajeto_para_imprimir

        if trajeto_para_imprimir >= 100:
            break

        time.sleep(0.5)


t_carro1 = Thread(target=carro, args=[15, 'Alex'])
t_carro2 = Thread(target=carro, args=[20, 'Laura'])

t_carro1.start()
t_carro2.start()
