import datetime

import pyqtgraph
from PyQt5 import QtGui, QtWidgets
import numpy as np
from pyqtgraph import PlotWidget
import pyqtgraph as pg


class PlotHistoryWindowConjunction(QtWidgets.QMainWindow):
    def __init__(self, title='电压合相', chose=[0, 1, 2],
                 beginTime='2022-10-23  10:10:36', endTime='2023-10-24  15:21:45',
                 DATADIC={}, DATADICKEY=[]):
        super().__init__()
        self.title = title
        self.chose = chose
        self.DATADIC = DATADIC
        self.DATADICKEY = []
        self.dataA = []
        self.dataB = []
        self.dataC = []
        self.length = 0
        self.resize(800, 600)
        self.setWindowTitle(self.title)
        # self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.beginTime = datetime.datetime.strptime(beginTime, '%Y-%m-%d %H:%M:%S')
        self.endTime = datetime.datetime.strptime(endTime, '%Y-%m-%d %H:%M:%S')



        for key in DATADICKEY:
            if self.beginTime < datetime.datetime.strptime(key, '%Y-%m-%d %H:%M:%S') < self.endTime:
                self.DATADICKEY.append(key)
        for key in self.DATADICKEY:
            self.dataA.append(DATADIC[key][self.chose[0]])
            self.dataB.append(DATADIC[key][self.chose[1]])
            self.dataC.append(DATADIC[key][self.chose[2]])
        self.length = len(self.dataA)
        self.plot()


    def plot(self):
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        pg.setConfigOptions(leftButtonPan=True, antialias=True)  # antialias抗锯齿

        self.plotWidget = PlotWidget(parent=self)
        self.setCentralWidget(self.plotWidget)
        self.plotWidget.setBackground('w')
        # 设置坐标轴标签
        self.plotWidget.setLabel('left', self.title, font="10pt")
        # 设置坐标轴范围
        # self.plotVoltage.setYRange(210, 230)
        # 设置底部坐标轴标签
        self.plotWidget.setLabel('bottom', '时间', font="10pt")
        '''横坐标显示时间'''
        length = len(self.dataA)
        y = self.plotWidget.getAxis('bottom')
        x = [0, length // 4, length // 2, length // 4 * 3, length - 1]
        strs = [self.DATADICKEY[0][11:], self.DATADICKEY[length // 4][11:], self.DATADICKEY[length // 2][11:],
                self.DATADICKEY[length // 4 * 3][11:], self.DATADICKEY[-1][11:]]  # 设置每个刻度值的显示数值
        ticks = [[i, j] for i, j in zip(x, strs)]  # 刻度值与显示数值绑定
        y.setTicks([ticks])
        ''''''

        """鼠标互动"""
        self.plotWidget.setMouseEnabled(x=True, y=False)
        self.plotWidget.setAutoVisible(x=False, y=True)

        # 改变刻度字体
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(10)
        font.setBold(True)
        self.plotWidget.getAxis("left").setStyle(tickFont=font)
        self.plotWidget.getAxis("bottom").setStyle(tickFont=font, autoExpandTextSpace=False)


        self.plotWidget.addLegend()
        self.plotCurveA = self.plotWidget.plot(np.array(self.dataA),
                                               pen=pyqtgraph.mkPen(color=(255, 255, 0), width=1.5),
                                               name="A相")
        self.plotCurveB = self.plotWidget.plot(np.array(self.dataB),
                                               pen=pyqtgraph.mkPen(color=(0, 255, 0), width=1.5),
                                               name="B相")
        self.plotCurveC = self.plotWidget.plot(np.array(self.dataC),
                                               pen=pyqtgraph.mkPen(color=(255, 0, 0), width=1.5),
                                               name="C相")

