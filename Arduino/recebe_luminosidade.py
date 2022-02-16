import serial
from serial.tools import list_ports

# --> INTERNET DAS COISAS
# --> Lista de portas do arduido
conexao= ""
for port in list_ports.comports():
    print('Dispositivo: {} - porta: {} '.format(port.description, port.device))
    if ("ARDUINO" in port.description.upper()):
        try:
            conexao = serial.Serial(port.device, 115200)
            print("Conexão realizada com {}.".format(conexao.portstr))
        except:
            pass

if conexao != "":
    while True:
        resposta = conexao.readline()
        print(float(resposta.decode()))
    conexao.close()


