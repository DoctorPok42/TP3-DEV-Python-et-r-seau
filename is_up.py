from sys import argv
from os import system

isDeviceUp = False

def isUp(host):
    isDeviceUp = system('ping -c 1 {} > /dev/null'.format(host))
    if isDeviceUp == 0:
        print('UP !')
    else:
        print('DOWN !')

for host in argv[1:]:
    isUp(host)
