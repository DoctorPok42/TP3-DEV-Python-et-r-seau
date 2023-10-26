from sys import argv
from os import system
from socket import gethostbyname
from psutil import net_if_addrs

network_name = ""
network_value = ""

def lookup(name):
    print(gethostbyname(name))

def isUp(host):
    isDeviceUp = system('ping -c 1 {} > /dev/null'.format(host))
    if isDeviceUp == 0:
        print('UP !')
    else:
        print('DOWN !')

def getMyIp():
    print(net_if_addrs()['Wi-Fi'][1][1])

def main():
    if (len(argv) != 3 and argv[1] != "ip"):
        print("Usage: python network.py <cmd>")
        exit(1)

    network_name = argv[1]

    if (network_name != "ip"):
        network_value = argv[2]

    switch = {
        "lookup": lambda: lookup(network_value),
        "isUp": lambda: isUp(network_value),
        "ip": lambda: getMyIp()
    }

    if network_name in switch:
        func = switch[network_name]
        func()
    else:
        print("Option not found!")
        exit(1)

main()