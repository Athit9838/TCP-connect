import socket
import base64

def Main():
    host = '127.0.0.1'
    port = 6008
    size = 61440
    file = 'a.jpg'
    
    bytesl = open(file, 'rb').read()
    bytesl = base64.b64encode(bytesl)

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((host, port))
    c.send(bytesl)
    print 'send file succesful'
    c.close()

if __name__ == '__main__':
    Main()
