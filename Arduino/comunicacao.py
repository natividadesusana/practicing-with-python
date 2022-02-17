import serial
from serial.tools import list_ports

# lista as portas do arduino.
for port in list_ports.comports():
    print('Dispositivo: {} - porta: {} '.format(port.description, port.device))

conexao = serial.Serial('COM3', 115200)
acao = input('Digite:\n <L> para Ligar \n <D> para Desligar: ').upper()
while acao == 'L' or acao == 'D':
    if acao == 'L':
        conexao.write(b'1')
    else:
        conexao.write(b'0')
    acao = input('Digite:\n <L> para Ligar \n <D> para Desligar: ').upper()
conexao.close()
print('Conexão encerrada.')



# code in arduino

# void setup() {
#   pinMode(10, OUTPUT);
#   Serial.begin(115200);
# }

# void loop() {
#   int valorRecebido;
#   if(Serial.available()) {
#       valorRecebido = Serial.read();
#       if(valorRecebido == '0') {
#           digitalWrite(10, LOW);
#       } else {
#           digitalWrite(10, HIGH);
#       }
#    }
# }