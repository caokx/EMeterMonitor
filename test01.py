from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)

        layout = QHBoxLayout(self)

        button1 = QPushButton('Button 1', self)
        button2 = QPushButton('Button 2', self)
        button3 = QPushButton('Button 3', self)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        # 设置每个按钮的弹簧比例不同
        layout.setStretchFactor(button1, 1)  # 比例为1
        layout.setStretchFactor(button2, 2)  # 比例为2
        layout.setStretchFactor(button3, 3)  # 比例为3


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())