import socket
import re
SERVER_ADDRESS = ('127.0.0.1', 23)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen()
print('Server is running')

pattern = re.compile('[0-9]{4} [A-Z][0-9] (2[0-3]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9].[0-9]{3} [0-9]{2}')

while True:
    connection, address = server_socket.accept()
    print("new connection from {address}".format(address=address))
    data = str(connection.recv(64), encoding='utf-8').strip()
    print(data)

    if pattern.match(data):
        sl = data.split(' ')
        print(data)
        if int(sl[3]) == 0:
            msg = 'спортсмен, нагрудный номер ' + sl[0] + ' прошёл отсечку ' + sl[1] + ' в ' + sl[2][:-2]
            print(msg)
        with open('log.txt', 'a', encoding='utf-8') as flog:
            print(data, file=flog)
    else:
        print("Illegal message format")
        continue
    connection.close()
