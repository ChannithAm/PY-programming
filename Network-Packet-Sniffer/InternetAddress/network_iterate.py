import ipaddress

NETWORKS = [
    '192.168.0.0/24',
    '2001:db8:1:2::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print("{!r}".format(net))
    for i, ip in zip(range(5), net):
        print(ip)

    print()