from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
import sys
import serial
import serial.tools.list_ports


class QPort(object):
    def __init__(self):
        super().__init__()
        self.serial = serial.Serial()

    @classmethod
    def getPortNames(cls):
        """获取设备的端口信息 -> [portName]"""
        try:
            listPortsObj = serial.tools.list_ports.comports()
            # print(listPortsObj)
            listPorts = []
            for obj in listPortsObj:
                listPorts.append(obj[0])
            # print(listPorts)
            return listPorts
        except IOError:
            print('无法获取设备的可用串口信息')
            return []

    def setSerial(self, port="COM7", baudrate=9600, parity='E', stopbits=1, bytesize=8):
        try:
            self.serial.setPort(port)
            self.serial.baudrate = baudrate
            self.serial.parity = parity
            self.serial.stopbits = stopbits
            self.serial.bytesize = bytesize
            # sys.stdout.write("打开串口中")
        except IOError:
            sys.stdout.write('打开串口失败')


class Edit(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        self.setGeometry(0, 0, 200, 200)
        self.appendPlainText('123')

    def write(self, s=None):
        self.appendPlainText(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # std = sys.stdout
    window = QMainWindow()
    window.setGeometry(0, 0, 500, 500)
    edit = Edit(parent=window)
    # sys.stdout = edit
    window.show()
    """业务"""
    port = QPort()
    port.setSerial()
    port.serial.open()
    print(port.serial.isOpen())
    port.serial.close()
    print(port.serial.isOpen())
    """"""
    # sys.stdout = std
    app.exec_()



