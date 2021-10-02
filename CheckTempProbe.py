import serial, datetime, re
from datetime import timedelta

fileHeader = "Date Time,Top Temp,Bottom Temp\n"
f=open("/home/pi/datafile.csv", "a")
f.write(fileHeader)
f.close()

dataBuffer=[]
debug = False
buffer = ''
minuteInterval = 10.0

ser=serial.Serial('/dev/ttyUSB0', 115200)
 
#Get past the POST messages of the RAMPS_14
while buffer != b'echo: Z2.00\n':
    
    buffer = ser.readline()
    if debug:
        print (buffer.decode("utf-8"))

if debug:
    print("Send Command")
cmd=b'M155 S60\n'
ser.write(cmd)
startTime = datetime.datetime.now()
while True:
    buff=ser.readline().decode()        
    currTime = datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p')
    tempStr = re.search("[T]\:\d{1,}[.]\d{1,}", buff)
    if debug:
        print(type(buff))
        print(buff)
        print(tempStr)
    if tempStr:
        topTemp = tempStr.group().replace('T:','')
    else:
        topTemp = ''
    if debug:
        print(type(topTemp))
    tempStr = re.search("[B]\:\d{1,}[.]\d{1,}", buff)
    if debug:
        print(tempStr)
    if tempStr:
        bottTemp = tempStr.group().replace('B:','')
    else:
        bottTemp = ''
    if debug:
        print(type(re.search("[B]\:\d{1,}[.]\d{1,}", buff)))
    currRow = currTime+","+topTemp+","+bottTemp+"\n"
    dataBuffer.append(currRow)
    #The regular expression to get the top temperature and
    #the bottom temperature
    #/[B|T]\:\d{1,}[.]\d{1,}/gm
    diff = datetime.datetime.now() - startTime
    if diff.seconds/60 >= minuteInterval:
        if debug:
            for row in dataBuffer:
                print(dataBuffer)
        #Append dataBuffer to file
        f = open("/home/pi/datafile.csv", "a")
        for row in dataBuffer:
                f.write(row)
        f.close()
        
        print("Buffer Written")
        startTime = datetime.datetime.now()
