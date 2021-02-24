from socket import *

host = "127.0.0.1"
port = 8888
ADDR = (host, port)

def socket_med(msg):
    s = socket()
    s.connect(ADDR)
    s.send(msg.encode())
    data = s.recv(1024)
    s.close()
    return data



def login():
    name = input("please input your name:")
    msg = 'L '+name
    response = socket_med(msg)
    if response.decode() == "OK":
        print("%s come into the chatroom"% name)
        return True
    else:
        print(response.decode())
        return False

##


def main():
    while True:
        if login():
            break

    data = input("please input chat")



if __name__ == '__main__':
    main()
