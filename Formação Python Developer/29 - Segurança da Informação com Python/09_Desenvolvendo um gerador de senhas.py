import random
import string

tamanho = int(input('Informe o tamanho da senha a ser gerada: '))

chars = string.ascii_letters + string.digits + '!@#$%¨&*()-=+'

rnd = random.SystemRandom()  # os.urandom

print(''.join(rnd.choice(chars) for i in range(tamanho)))

print(chars)
