from socket import *


host="0.0.0.0"
port=8888
ADDR=(host,port)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)
users={}

def do_login(c,name):


        if name in users or 'admin' in users:
            c.send("user exists,please choose another name".encode())


        else:
            c.send(b'OK')
            for i in users:
                users[i].send(("welcome %s login"% name).encode())
            users[name] = c







def main():
    while True:
        connfd, addr = s.accept()
    # try:

        data = connfd.recv(1024)

        request = data.decode().split(' ')
        # print(request)
        if request[0] == 'L':
            do_login(connfd,request[1])
        else:
            print("wrony request")
    # except Exception as e:
    #     print(e,'error')
    #     print(users)
    #     del users[request[1]]
    #     print(users)
    #     continue











if __name__ == '__main__':
    main()