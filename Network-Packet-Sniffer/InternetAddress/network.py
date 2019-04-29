import ipaddress

NETWORKS = [
    '192.168.0.0/24',
    '2001:db8:1:3::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print("{!r}".format(net))
    print("\tis private: ", net.is_private)
    print("\tbroadcast: ", net.broadcast_address)
    print("\tcompressed: ", net.compressed)
    print("\twith netmask: ", net.with_netmask)
    print("\twith hostmask: ", net.with_hostmask)
    print("\tnum addresses: ", net.num_addresses)
    print()