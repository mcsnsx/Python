import serial
from serial.tools import list_ports

# --> INTERNET DAS COISAS
# --> Lista de portas do arduido
for port in list_ports.comports():
    print('Dispositivo: {} - porta: {} '.format(port.description, port.device))

conexao = serial.Serial('COM3', 115200)

acao=input("Digite: \n<L> para Ligar\n<D> para Desligar: ").upper()
while acao=="L" or acao=="D":
    if acao=="L":
        conexao.write(b'1')
    else:
        conexao.write(b'0')
    acao = input("Digite: \n<L> para Ligar\n<D> para Desligar: ").upper()
conexao.close()
print("Conexão encerrada.")