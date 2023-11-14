import sys
import time
import serial
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

from FCS import FCS


class QGetDataThread(QThread):
    signal_ = pyqtSignal(bytes)

    def __init__(self, serial=None, message=None):
        super().__init__()
        self.serial = serial
        self.write = bytes.fromhex(message)
        self.read = bytes.fromhex('')

    def run(self):
        while True:
            if self.serial.isOpen():
                self.serial.flushInput()  # 清空缓存
                try:
                    self.serial.write(self.write)
                except IOError:
                    break
                time.sleep(1)
                try:
                    self.serial.flushOutput()
                except IOError:
                    return
                if self.serial.isOpen():
                    try:
                        lenOfRead = self.serial.inWaiting()
                    except IOError:
                        lenOfRead = 0
                        pass
                else:
                    continue
                if lenOfRead:
                    self.read = self.serial.read(lenOfRead)
                    if FCS.testFcs(cp=self.read[5:-1]):
                        # read = ''.join(map(lambda x: (" " if len(hex(x)) >= 4 else " 0") + hex(x)[2:],
                        #                self.read))
                        # sys.stdout.write('接收报文<-' + read)
                        self.signal_.emit(self.read)
                    else:
                        read_ = ''.join(map(lambda x: (" " if len(hex(x)) >= 4 else " 0") + hex(x)[2:],
                                            self.read))
                        sys.stdout.write('接收报文<-' + read_ + '接收报文校验码错误')

                else:
                    sys.stdout.write('未接收到报文')
            else:
                time.sleep(1)


def select68(message):
    print(len(message))


def pp():
    # print('pp')
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()
    mainWindow.setGeometry(0, 0, 500, 500)
    mainWindow.show()
    serial = serial.Serial(port='COM7', baudrate=9600, parity='E', stopbits=1, bytesize=8)
    """test serial"""
    message = '68 1e 00 43 05 aa aa aa aa aa aa a1 12 77 05 03 00 50 02 02 00 00 01 00 00 10 04 01 00 a8 bc 16'
    serial.write(bytes.fromhex(message))
    time.sleep(0.4)
    lenOfRead = serial.inWaiting()  # 获取缓冲数据（接收数据）长度
    print(lenOfRead)
    if lenOfRead:
        read = serial.read(lenOfRead)
        if FCS.testFcs(cp=read[5:-1]):
            # read = ''.join(map(lambda x: (" " if len(hex(x)) >= 4 else " 0") + hex(x)[2:], read))
            print('通信正常')
    else:
        print('通信异常')
        exit()

    timer = QTimer()
    timer.timeout.connect(pp)
    timer.start(1000)

    thread = QGetDataThread(serial, message)
    thread.signal_.connect(select68)
    thread.start()

    time.sleep(3)
    thread.terminate()

    app.exec_()
