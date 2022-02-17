import serial
from serial.tools import list_ports

# --> INTERNET DAS COISAS
# --> Lista de portas do arduido - Ligar a luz em um determinado momento de acordo com a luminosidade do dia
conexao = ""
for port in list_ports.comports():
    print('Dispositivo: {} - porta: {} '.format(port.description, port.device))
    if("ARDUINO" in port.description.upper()):
        try:
            conexao = serial.Serial(port.device, 115200)
            print("Conexão realizada com {}.".format(conexao.portstr))
        except:
            pass

if conexao != "":
    print("Iniciando...")
    while True:
        print("Recebendo dados...")
        resposta = conexao.readline()
        valor = float (resposta.decode())
        print(valor)
        if(valor < 700):
            conexao.write(b'1')
        else:
            conexao.write(b'0')

    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem pontas disponíveis.")

# --> CÓDIGO QUE ESTÁ NO ARDUINO (Sensor)
#
# void setup (){
#     pinMode(10, OUTPUT); # ---> led
#     Serial.begin(115200); # --> taxa de transferencia
# }
#
# void loop(){
#     int valorRecebido;
#     int luz = analogRead(1);
#     Serial.println(luz);
#     delay(500);
#     valorRecebido = Serial.read();
#     if (valorRecebido == '0'){
#         digitalWrite(10, LOW);
#     } else {
#         digitalWrite(10, HIGH);
#     }
# }