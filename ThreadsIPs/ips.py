import ipaddress

ip1 = '192.168.0.1'
ip2 = '192.168.0.0/24'

endereco = ipaddress.ip_address(ip1)
rede = ipaddress.ip_network(ip2, strict=False)

print(endereco)

for ip in rede:
    print(rede)