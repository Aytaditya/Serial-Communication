import serial

ser=serial.Serial(port='/dev/ttyACM0', baudrate=9600)

while True:
    value=ser.readline()
    valueInString=str(value,'utf-8')
    print(valueInString)
