import serial, time

ser=serial.Serial('/dev/ttyUSB0', 115200)

input = ser.readline()
#print("Start the output")
while input != "echo: Z2.00":
    print (input.decode("utf-8"))
    input = ser.readline()
    
#Send initialization command to read temp every 5 seconds
print("Send Command")
cmd="M155 S5"
ser.write(cmd.encode())

while True:
    
    
    buffer = ser.readline()
    print("Buffer")
    print (buffer.decode("utf-8"))
            