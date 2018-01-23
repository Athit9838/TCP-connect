import socket
import base64
import os

def Main():
    host = '127.0.0.1'
    port = 6008
    size = 61440

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print 'waiting client connect'
    
    sc, addr = s.accept()

    print 'client host',addr
    a = '/image_frome_client/'
    sb = 'C:\\Users\\Asu\\Desktop\\Network\\test'
    b = 'C:\\Users\\Asu\\Desktop\\Network\\test''/image_frome_client/'

    if not os.path.exists(sb+a):
            os.makedirs(sb+a)
    myfile = open(b +'image.jpg', 'wb')
    while 1:
        data = sc.recv(size)
        if not data:
            break
        data = base64.b64decode(data)
        myfile.write(data)
        print 'writing... '
        myfile.close()
        print 'succesful... '
        sc.close
        break
    sc.close()

if __name__ == '__main__':
    Main()
