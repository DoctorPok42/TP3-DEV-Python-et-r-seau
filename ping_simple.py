from os import system

def ping(host):
    system('ping -c 1 {}'.format(host))

if __name__ == '__main__':
    ping('8.8.8.8')