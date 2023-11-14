from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
import sys
import datetime


class QPlainTextEditRedirection(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.setMaximumBlockCount(1000)
    def write(self, message):
        self.appendPlainText(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.appendPlainText(message)
        self.appendPlainText('-----------------------')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(0, 0, 500, 500)
    edit = QPlainTextEditRedirection(parent=window)
    std = sys.stdout
    sys.stdout = edit
    edit.setGeometry(0, 0, 200, 200)
    window.show()
    app.exec_()
    sys.stdout = std
