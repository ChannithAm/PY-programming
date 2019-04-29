import binascii
import ipaddress

ADDRESS = [
    '192.168.0.120',
    '2001:db8:2:1::2',
]

for ip in ADDRESS:
    addr = ipaddress.ip_address(ip)
    print("{!r}".format(addr))
    print("\tIP version: ", addr.version)
    print("\tIs private: ", addr.is_private)
    print("\tPacked form: ", binascii.hexlify(addr.packed))
    print("\t\tInteger: ", int(addr))