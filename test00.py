import time

import serial

if __name__ == '__main__':
    try:
        serial = serial.Serial(port='COM7', baudrate=9600, parity='E', stopbits=1, bytesize=8)
    except IOError:
        print('串口被占用')
        exit()
    messageAddress = '68 17 00 43 45 AA AA AA AA AA AA a1 D8 FB 05 01 00 40 01 02 00 00 ED 03 16'
    serial.write(bytes.fromhex(messageAddress))
    time.sleep(0.4)
    lenRead = serial.inWaiting()
    if lenRead:
        read = serial.read(lenRead)
        readMessage = ''.join(map(lambda x: (" " if len(hex(x)) >= 4 else " 0") + hex(x)[2:], read))
        print(readMessage)
    else:
        print('未接收到电表信息')



