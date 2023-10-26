from sys import argv
from os import system

def makePing(host):
    system('ping -c 1 {}'.format(host))

for host in argv[1:]:
    makePing(host)
