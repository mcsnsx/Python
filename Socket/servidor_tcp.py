from socket import *

# --> APLICAÇÃO SERVIDORA - Abre uma porta para os clientes acessarem API, conexão
servidor = "127.0.0.1" # --> localhost
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor, porta))
obj_socket.listen(2)

print("Aguardando cliente...")

while True:
    con, cliente = obj_socket.accept()
    print("Conectando com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Olah cliente'
        con.send(msg_enviada)
        break
    con.close()