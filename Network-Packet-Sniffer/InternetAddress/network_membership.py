import ipaddress

NETWORKS = [
    ipaddress.ip_network('192.168.0.0/24'),
    ipaddress.ip_network('2001:db8:1:2::/64'),
]

ADDRESSES = [
    ipaddress.ip_address('192.168.0.120'),
    ipaddress.ip_address('192.168.2.121'),
    ipaddress.ip_address(
        '2001:db8:1:2::3'
    ),
    ipaddress.ip_address(
        '2001:db8:abc:3:2::4'
    ),
]

for ip in ADDRESSES:
    for net in NETWORKS:
        if ip in net:
            print("{}\nis on {}".format(ip, net))
            break
    else:
        print('{}\nis not a known network'.format(ip))
    print()