import ipaddress

ip = '192.168.0.1'
enderco_ip = ipaddress.ip_address(ip)
print(enderco_ip + 2000)

rede_ip = '192.168.0.0/24'
endereco_rede_ip = ipaddress.ip_network(rede_ip, strict=False)

print(endereco_rede_ip)

for ip in endereco_rede_ip:
    print(ip)
