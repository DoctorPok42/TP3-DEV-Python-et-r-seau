from sys import argv
from socket import gethostbyname

def lookup(name):
    print(gethostbyname(name))

for hostName in argv[1:]:
    lookup(hostName)