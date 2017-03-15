import socket

def main():
    host = '127.0.0.1'
    port = 3001

    server = ('127.0.0.1', 3000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print('connected to server on port 3000')

    message = raw_input('-> ')
    while message != 'q':
        s.sendto(message, server)
        data, addr = s.recvfrom(1024)
        print('received message from ' + str(addr) + ': ' + str(data))
        message = raw_input('-> ')
    s.close()

if __name__ == '__main__':
    main()