from PyQt5.QtCore import *
import pyqtgraph
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from pyqtgraph import PlotWidget
import pyqtgraph as pg


# from UI_MainWindow import DATADIC, DATADICKEY


class PlotWindowConjunction(QtWidgets.QMainWindow):
    def __init__(self, title='电压合相', scope=200, chose=[0, 1, 2], DATADIC={}, DATADICKEY=[]):
        super().__init__()
        self.title = title
        self.scope = scope
        self.chose = chose
        self.DATADIC = DATADIC
        self.DATADICKEY = DATADICKEY
        self.dataA = []
        self.dataB = []
        self.dataC = []
        self.length = 0
        self.resize(800, 600)
        self.setWindowTitle(self.title)
        # self.setWindowFlags(Qt.WindowCloseButtonHint)

        for key in DATADICKEY:
            self.dataA.append(DATADIC[key][self.chose[0]])
            self.dataB.append(DATADIC[key][self.chose[1]])
            self.dataC.append(DATADIC[key][self.chose[2]])
        self.length = len(self.dataA)
        self.plot()
        # 连接成功后开始定时读取电表数据
        self.timer = pg.QtCore.QTimer()
        # 定时器信号绑定 update_data 函数
        self.timer.timeout.connect(self.updateData)
        # 定时器间隔50ms，可以理解为 50ms 刷新一次数据
        self.timer.start(1000)

    def plot(self):
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        pg.setConfigOptions(leftButtonPan=False, antialias=True)  # antialias抗锯齿

        self.plotWidget = PlotWidget()
        self.setCentralWidget(self.plotWidget)
        self.plotWidget.setBackground('w')
        # 设置坐标坐标轴标签
        self.plotWidget.setLabel('left', self.title, font="10pt")
        # 设置坐标轴范围
        # self.plotVoltage.setYRange(210, 230)
        # 设置底部坐标轴标签
        self.plotWidget.setLabel('bottom', '时间', font="10pt")
        # 改变刻度字体
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(10)
        font.setBold(True)
        self.plotWidget.getAxis("left").setStyle(tickFont=font)
        self.plotWidget.getAxis("bottom").setStyle(tickFont=font)
        """鼠标互动"""
        self.plotWidget.setMouseEnabled(x=True, y=False)
        self.plotWidget.setAutoVisible(x=False, y=True)

        # 设置该控件尺寸和相对位置，没有起作用
        # self.plotWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.plotWidget.addLegend()
        self.plotCurveA = self.plotWidget.plot(np.array(self.dataA[-self.scope:]),
                                               pen=pyqtgraph.mkPen(color=(255, 255, 0), width=1.5),
                                               name="A相")
        self.plotCurveB = self.plotWidget.plot(np.array(self.dataB[-self.scope:]),
                                               pen=pyqtgraph.mkPen(color=(0, 255, 0), width=1.5),
                                               name="B相")
        self.plotCurveC = self.plotWidget.plot(np.array(self.dataC[-self.scope:]),
                                               pen=pyqtgraph.mkPen(color=(255, 0, 0), width=1.5),
                                               name="C相")

    def updateData(self):
        if len(self.DATADIC) == 0:
            return
        # 当采集到数据，DATADIC长度大于self.length时使用
        # if self.length < self.DATADICKEY.__len__():
        #     self.length = self.DATADICKEY.__len__()

        if self.length == self.DATADIC.__len__():
            return
        '''if 内部'''
        self.dataA.append(self.DATADIC[self.DATADICKEY[-1]][self.chose[0]])
        self.dataB.append(self.DATADIC[self.DATADICKEY[-1]][self.chose[1]])
        self.dataC.append(self.DATADIC[self.DATADICKEY[-1]][self.chose[2]])
        '''if 外部'''
        self.plotCurveA.setData(np.array(self.dataA[-self.scope:]))
        self.plotCurveB.setData(np.array(self.dataB[-self.scope:]))
        self.plotCurveC.setData(np.array(self.dataC[-self.scope:]))
        self.length = self.DATADIC.__len__()