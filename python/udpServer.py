import socket

def main():
    host = '127.0.0.1'
    port = 3000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print('server started on port 3000')
    
    while True:
        data, addr = s.recvfrom(1024)
        print('received message from ' + str(addr) + ': ' + str(data))
        data = str(data).upper()
        print('sending ' + str(data) + ' to ' + str(addr))
        s.sendto(data, addr)
    s.close()

if __name__ == '__main__':
    main()
