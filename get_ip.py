from psutil import net_if_addrs

def getMyIp():
    print(net_if_addrs()['Wi-Fi'][1][1])

getMyIp()