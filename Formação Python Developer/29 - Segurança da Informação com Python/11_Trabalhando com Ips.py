import ipaddress

ip = '192.168.0.1'

endereco_ip = ipaddress.ip_address(ip)

print(endereco_ip)
print(type(endereco_ip))
# Se eu quiser saber o próximo IP posso somar valores
print(endereco_ip + 254)
print(endereco_ip + 511)

ip_rede = '192.168.0.0/24'

rede = ipaddress.ip_network(ip_rede, strict=False)

print(rede)
print(type(rede))

for ip in rede:
    print(ip)
