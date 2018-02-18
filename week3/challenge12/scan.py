import getopt
import sys
import socket


def is_ip(address):
    sep = address.split('.')
    if len(sep) != 4:
        return False
    for i, x in enumerate(sep):
        try:
            int_x = int(x)
            if int_x < 0 or int_x > 255:
                return False
        except ValueError:
            return False
    return True


try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["host=", "port="])
except getopt.GetoptError:
    print('Parameter Error')
    exit()
for opt, arg in opts:
    if opt == '--host':
        host = arg
        if is_ip(host) == False:
            print('Parameter Error')
            exit()
    elif opt == '--port':
        port = arg


def port_is_free(host, port):
    s = socket.socket()
    s.settimeout(0.1)
    try:
        return s.connect_ex((host, port))
    finally:
        s.close()


if '-' in arg:
    arglist = arg.split('-')
    if int(arglist[0]) <= 0:
        print('Parameter Error')
        exit()
    if int(arglist[1]) >= 100000:
        print('Parameter Error')
        exit()
    arglist = [i for i in range(int(arglist[0]), int(arglist[1]) + 1)]
    for x in arglist:
        if port_is_free(host, x) == 0:
            print(x, 'open')
        else:
            print(x, 'close')
    # print(arglist)
else:
    if int(arg) <= 0:
        print('Parameter Error')
        exit()
    if int(arg) >= 100000:
        print('Parameter Error')
        exit()
    if port_is_free(host, int(arg)) == 0:
        print(arg, 'open')
    else:
        print(arg, 'close')
