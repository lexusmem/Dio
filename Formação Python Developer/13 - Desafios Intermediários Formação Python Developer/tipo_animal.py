a = input()
b = input()
c = input()

if a == 'vertebrado':
    if b == 'mamifero':
        if c == 'onivoro':
            print('homem')
        else:
            print('vaca')
    else:
        if c == 'carnivoro':
            print('aguia')
        else:
            print('pomba')

elif a == 'invertebrado':
    if b == 'inseto':
        if c == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if c == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
