from PyQt5 import QtCore, QtGui, QtWidgets

from QPlainTextEditRedirection import QPlainTextEditRedirection


class Ui_MainWindow(object):
    def __init__(self):
        """"""
        self.tab0Con0 = None
        self.tab2 = None
        self.tab1 = None
        self.tab0 = None
        self.vbox = None
        self.splitter = None  # 分割器
        self.edit = None  # 文本显示框
        self.tabWidget = None  # 分页类型
        """"""

    def setupUi(self, widget):
        if not isinstance(widget, QtWidgets.QWidget):
            raise ValueError('参数widget必须是PyQt5.QtWidgets.QWidget')
        """整体布局"""
        self.splitter = QtWidgets.QSplitter(widget)  # 创建分割器
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)  # 添加组件
        self.edit = QPlainTextEditRedirection(self.splitter)  # 添加组件
        self.splitter.setSizes([400, 100])  # 设置组件比例

        self.vbox = QtWidgets.QVBoxLayout()  # 创建垂直布局器
        self.vbox.addWidget(self.splitter)  # 添加组件
        widget.setLayout(self.vbox)  # 设置窗口布局

        """tabWidget布局"""
        self.tab0 = QtWidgets.QWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab0, '端口设置')
        self.tabWidget.addTab(self.tab1, '实时数据')
        self.tabWidget.addTab(self.tab2, '历史数据')

        """tab0布局"""
        self.tab0Con0 = QtWidgets.QGroupBox(title="串口设置")
        self.tab0Con1 = QtWidgets.QGroupBox(title='连接设置')
        self.tab0V = QtWidgets.QVBoxLayout()
        self.tab0H = QtWidgets.QHBoxLayout()
        # 垂直方向布局
        self.tab0V.addStretch(1)
        self.tab0V.addWidget(self.tab0Con0)
        self.tab0V.addStretch(1)
        self.tab0V.addWidget(self.tab0Con1)
        self.tab0V.addStretch(20)
        # 水平方向
        self.tab0H.addLayout(self.tab0V)
        self.tab0H.addStretch()
        self.tab0.setLayout(self.tab0H)

        """tab0Con0"""
        self.tab0Con0G = QtWidgets.QGridLayout()
        self.tab0Con0.setLayout(self.tab0Con0G)
        '''串口号'''
        self.tab0Con0H0Lab = QtWidgets.QLabel("串口号")
        self.tab0Con0H0Com = QtWidgets.QComboBox()
        self.tab0Con0G.addWidget(self.tab0Con0H0Lab, 0, 0)
        self.tab0Con0G.addWidget(self.tab0Con0H0Com, 0, 1)
        '''波特率'''
        self.tab0Con0H1Lab = QtWidgets.QLabel("波特率")
        self.tab0Con0H1Com = QtWidgets.QComboBox()
        self.tab0Con0G.addWidget(self.tab0Con0H1Lab, 1, 0)
        self.tab0Con0G.addWidget(self.tab0Con0H1Com, 1, 1)
        '''校验位'''
        self.tab0Con0H2Lab = QtWidgets.QLabel("校验位")
        self.tab0Con0H2Com = QtWidgets.QComboBox()
        self.tab0Con0G.addWidget(self.tab0Con0H2Lab, 2, 0)
        self.tab0Con0G.addWidget(self.tab0Con0H2Com, 2, 1)
        '''数据位'''
        self.tab0Con0H3Lab = QtWidgets.QLabel("数据位")
        self.tab0Con0H3Com = QtWidgets.QComboBox()
        self.tab0Con0G.addWidget(self.tab0Con0H3Lab, 3, 0)
        self.tab0Con0G.addWidget(self.tab0Con0H3Com, 3, 1)
        '''停止位'''
        self.tab0Con0H4Lab = QtWidgets.QLabel("停止位")
        self.tab0Con0H4Com = QtWidgets.QComboBox()
        self.tab0Con0G.addWidget(self.tab0Con0H4Lab, 4, 0)
        self.tab0Con0G.addWidget(self.tab0Con0H4Com, 4, 1)

        '''tab0Con1'''
        self.tab0Con1G = QtWidgets.QGridLayout()
        self.tab0Con1.setLayout(self.tab0Con1G)
        '''打开串口'''
        self.tab0Con1H0Bn = QtWidgets.QPushButton("打开串口")
        self.tab0Con1H0Lab = QtWidgets.QLabel('关闭')
        self.tab0Con1G.addWidget(self.tab0Con1H0Bn, 0, 0)
        self.tab0Con1G.addWidget(self.tab0Con1H0Lab, 0, 1)
        '''关闭串口'''
        self.tab0Con1H1Bn = QtWidgets.QPushButton("关闭串口")
        self.tab0Con1H1Lab = QtWidgets.QLabel('')
        self.tab0Con1G.addWidget(self.tab0Con1H1Bn, 1, 0)
        self.tab0Con1G.addWidget(self.tab0Con1H1Lab, 1, 1)
        '''通信测试'''
        self.tab0Con1H2Bn = QtWidgets.QPushButton("通信测试")
        self.tab0Con1H2Lab = QtWidgets.QLabel('..')
        self.tab0Con1G.addWidget(self.tab0Con1H2Bn, 2, 0)
        self.tab0Con1G.addWidget(self.tab0Con1H2Lab, 2, 1)
        '''采集数据'''
        self.tab0Con1H3Bn = QtWidgets.QPushButton("采集数据")
        self.tab0Con1H3Lab = QtWidgets.QLabel('停止')
        self.tab0Con1G.addWidget(self.tab0Con1H3Bn, 3, 0)
        self.tab0Con1G.addWidget(self.tab0Con1H3Lab, 3, 1)
        '''停止采集'''
        self.tab0Con1H4Bn = QtWidgets.QPushButton("停止采集")
        self.tab0Con1H4Lab = QtWidgets.QLabel('')
        self.tab0Con1G.addWidget(self.tab0Con1H4Bn, 4, 0)
        self.tab0Con1G.addWidget(self.tab0Con1H4Lab, 4, 1)

        '''tab1'''
        self.tab1H = QtWidgets.QHBoxLayout()
        self.tab1Con0 = QtWidgets.QGroupBox('电压')
        self.tab1Con1 = QtWidgets.QGroupBox('电流')
        self.tab1Con2 = QtWidgets.QGroupBox('功率')
        self.tab1Con3 = QtWidgets.QGroupBox('功率因数')
        self.tab1Con4 = QtWidgets.QGroupBox('电能量')
        self.tab1H.addWidget(self.tab1Con0)
        self.tab1H.addWidget(self.tab1Con1)
        self.tab1H.addWidget(self.tab1Con2)
        self.tab1H.addWidget(self.tab1Con3)
        self.tab1H.addWidget(self.tab1Con4)
        self.tab1H.addStretch()

        self.tab1V = QtWidgets.QVBoxLayout()
        self.tab1V.addLayout(self.tab1H)
        self.tab1V.addStretch()
        self.tab1.setLayout(self.tab1V)
        '''tab1Con0 电压'''
        self.tab1Con0G = QtWidgets.QGridLayout()
        self.tab1Con0Lab0 = QtWidgets.QLabel('选相')
        self.tab1Con0Com1 = QtWidgets.QComboBox()
        self.tab1Con0G.addWidget(self.tab1Con0Lab0, 0, 0)
        self.tab1Con0G.addWidget(self.tab1Con0Com1, 0, 1)

        self.tab1Con0Bn2 = QtWidgets.QPushButton('绘图')
        self.tab1Con0Com3 = QtWidgets.QComboBox()
        self.tab1Con0G.addWidget(self.tab1Con0Bn2, 1, 0)
        self.tab1Con0G.addWidget(self.tab1Con0Com3, 1, 1)
        self.tab1Con0.setLayout(self.tab1Con0G)
        '''tab1Con1 电流'''
        self.tab1Con1G = QtWidgets.QGridLayout()
        self.tab1Con1Lab0 = QtWidgets.QLabel('选相')
        self.tab1Con1Com1 = QtWidgets.QComboBox()
        self.tab1Con1G.addWidget(self.tab1Con1Lab0, 0, 0)
        self.tab1Con1G.addWidget(self.tab1Con1Com1, 0, 1)

        self.tab1Con1Bn2 = QtWidgets.QPushButton('绘图')
        self.tab1Con1Com3 = QtWidgets.QComboBox()
        self.tab1Con1G.addWidget(self.tab1Con1Bn2, 1, 0)
        self.tab1Con1G.addWidget(self.tab1Con1Com3, 1, 1)

        self.tab1Con1.setLayout(self.tab1Con1G)
        '''tab1Con2 功率'''
        self.tab1Con2G = QtWidgets.QGridLayout()
        self.tab1Con2Lab0 = QtWidgets.QLabel('选相')
        self.tab1Con2Com1 = QtWidgets.QComboBox()
        self.tab1Con2G.addWidget(self.tab1Con2Lab0, 0, 0)
        self.tab1Con2G.addWidget(self.tab1Con2Com1, 0, 1)

        self.tab1Con2Bn2 = QtWidgets.QPushButton('绘图')
        self.tab1Con2Com3 = QtWidgets.QComboBox()
        self.tab1Con2G.addWidget(self.tab1Con2Bn2, 1, 0)
        self.tab1Con2G.addWidget(self.tab1Con2Com3, 1, 1)

        self.tab1Con2.setLayout(self.tab1Con2G)
        '''tab1Con3 功率因数'''
        self.tab1Con3G = QtWidgets.QGridLayout()
        self.tab1Con3Lab0 = QtWidgets.QLabel('选相')
        self.tab1Con3Com1 = QtWidgets.QComboBox()
        self.tab1Con3G.addWidget(self.tab1Con3Lab0, 0, 0)
        self.tab1Con3G.addWidget(self.tab1Con3Com1, 0, 1)

        self.tab1Con3Bn2 = QtWidgets.QPushButton('绘图')
        self.tab1Con3Com3 = QtWidgets.QComboBox()
        self.tab1Con3G.addWidget(self.tab1Con3Bn2, 1, 0)
        self.tab1Con3G.addWidget(self.tab1Con3Com3, 1, 1)
        self.tab1Con3.setLayout(self.tab1Con3G)
        '''tab1Con4 电能量'''
        self.tab1Con4G = QtWidgets.QGridLayout()
        self.tab1Con4Lab0 = QtWidgets.QLabel('选相')
        self.tab1Con4Com1 = QtWidgets.QComboBox()
        self.tab1Con4G.addWidget(self.tab1Con4Lab0, 0, 0)
        self.tab1Con4G.addWidget(self.tab1Con4Com1, 0, 1)

        self.tab1Con4Bn2 = QtWidgets.QPushButton('绘图')
        self.tab1Con4Com3 = QtWidgets.QComboBox()
        self.tab1Con4G.addWidget(self.tab1Con4Bn2, 1, 0)
        self.tab1Con4G.addWidget(self.tab1Con4Com3, 1, 1)
        self.tab1Con4.setLayout(self.tab1Con4G)

        '''tab2'''
        self.tab2H_1 = QtWidgets.QHBoxLayout()
        self.tab2Con_1 = QtWidgets.QGroupBox('绘图设置')
        self.tab2H_1.addWidget(self.tab2Con_1)
        self.tab2H_1.addStretch(20)
        self.tab2H = QtWidgets.QHBoxLayout()
        self.tab2Con0 = QtWidgets.QGroupBox('电压')
        self.tab2Con1 = QtWidgets.QGroupBox('电流')
        self.tab2Con2 = QtWidgets.QGroupBox('功率')
        self.tab2Con3 = QtWidgets.QGroupBox('功率因数')
        self.tab2Con4 = QtWidgets.QGroupBox('电能量')
        self.tab2H.addWidget(self.tab2Con0)
        self.tab2H.addWidget(self.tab2Con1)
        self.tab2H.addWidget(self.tab2Con2)
        self.tab2H.addWidget(self.tab2Con3)
        self.tab2H.addWidget(self.tab2Con4)
        self.tab2H.addStretch()

        self.tab2V = QtWidgets.QVBoxLayout()
        self.tab2V.addLayout(self.tab2H_1)
        self.tab2V.addLayout(self.tab2H)
        self.tab2V.addStretch()
        self.tab2.setLayout(self.tab2V)
        '''tab2Con_1'''
        self.tab2Con_1V = QtWidgets.QVBoxLayout()
        self.tab2Con_1H0 = QtWidgets.QHBoxLayout()
        self.tab2Con_1Bn0 = QtWidgets.QPushButton('选择文件')
        self.tab2Con_1Lab1 = QtWidgets.QLabel('history/')
        self.tab2Con_1H0.addWidget(self.tab2Con_1Bn0)
        self.tab2Con_1H0.addWidget(self.tab2Con_1Lab1)

        self.tab2Con_1H1 = QtWidgets.QHBoxLayout()
        self.tab2Con_1Bn2 = QtWidgets.QLabel('开始时间')
        self.tab2Con_1Lab3 = QtWidgets.QLineEdit('')
        self.tab2Con_1H1.addWidget(self.tab2Con_1Bn2)
        self.tab2Con_1H1.addWidget(self.tab2Con_1Lab3)

        self.tab2Con_1H2 = QtWidgets.QHBoxLayout()
        self.tab2Con_1Bn4 = QtWidgets.QLabel('结束时间')
        self.tab2Con_1Lab5 = QtWidgets.QLineEdit('')
        self.tab2Con_1H2.addWidget(self.tab2Con_1Bn4)
        self.tab2Con_1H2.addWidget(self.tab2Con_1Lab5)

        self.tab2Con_1V.addLayout(self.tab2Con_1H0)
        self.tab2Con_1V.addLayout(self.tab2Con_1H1)
        self.tab2Con_1V.addLayout(self.tab2Con_1H2)
        self.tab2Con_1.setLayout(self.tab2Con_1V)

        '''tab2Con0 电压'''
        self.tab2Con0G = QtWidgets.QGridLayout()
        self.tab2Con0Lab0 = QtWidgets.QLabel('选相')
        self.tab2Con0Com1 = QtWidgets.QComboBox()
        self.tab2Con0G.addWidget(self.tab2Con0Lab0, 0, 0)
        self.tab2Con0G.addWidget(self.tab2Con0Com1, 0, 1)

        self.tab2Con0Bn2 = QtWidgets.QPushButton('绘图')
        self.tab2Con0Com3 = QtWidgets.QComboBox()
        self.tab2Con0G.addWidget(self.tab2Con0Bn2, 1, 0)
        self.tab2Con0G.addWidget(self.tab2Con0Com3, 1, 1)
        self.tab2Con0.setLayout(self.tab2Con0G)
        '''tab2Con1 电流'''
        self.tab2Con1G = QtWidgets.QGridLayout()
        self.tab2Con1Lab0 = QtWidgets.QLabel('选相')
        self.tab2Con1Com1 = QtWidgets.QComboBox()
        self.tab2Con1G.addWidget(self.tab2Con1Lab0, 0, 0)
        self.tab2Con1G.addWidget(self.tab2Con1Com1, 0, 1)

        self.tab2Con1Bn2 = QtWidgets.QPushButton('绘图')
        self.tab2Con1Com3 = QtWidgets.QComboBox()
        self.tab2Con1G.addWidget(self.tab2Con1Bn2, 1, 0)
        self.tab2Con1G.addWidget(self.tab2Con1Com3, 1, 1)

        self.tab2Con1.setLayout(self.tab2Con1G)
        '''tab2Con2 功率'''
        self.tab2Con2G = QtWidgets.QGridLayout()
        self.tab2Con2Lab0 = QtWidgets.QLabel('选相')
        self.tab2Con2Com1 = QtWidgets.QComboBox()
        self.tab2Con2G.addWidget(self.tab2Con2Lab0, 0, 0)
        self.tab2Con2G.addWidget(self.tab2Con2Com1, 0, 1)

        self.tab2Con2Bn2 = QtWidgets.QPushButton('绘图')
        self.tab2Con2Com3 = QtWidgets.QComboBox()
        self.tab2Con2G.addWidget(self.tab2Con2Bn2, 1, 0)
        self.tab2Con2G.addWidget(self.tab2Con2Com3, 1, 1)

        self.tab2Con2.setLayout(self.tab2Con2G)
        '''tab2Con3 功率因数'''
        self.tab2Con3G = QtWidgets.QGridLayout()
        self.tab2Con3Lab0 = QtWidgets.QLabel('选相')
        self.tab2Con3Com1 = QtWidgets.QComboBox()
        self.tab2Con3G.addWidget(self.tab2Con3Lab0, 0, 0)
        self.tab2Con3G.addWidget(self.tab2Con3Com1, 0, 1)

        self.tab2Con3Bn2 = QtWidgets.QPushButton('绘图')
        self.tab2Con3Com3 = QtWidgets.QComboBox()
        self.tab2Con3G.addWidget(self.tab2Con3Bn2, 1, 0)
        self.tab2Con3G.addWidget(self.tab2Con3Com3, 1, 1)
        self.tab2Con3.setLayout(self.tab2Con3G)
        '''tab2Con4 电能量'''
        self.tab2Con4G = QtWidgets.QGridLayout()
        self.tab2Con4Lab0 = QtWidgets.QLabel('选相')
        self.tab2Con4Com1 = QtWidgets.QComboBox()
        self.tab2Con4G.addWidget(self.tab2Con4Lab0, 0, 0)
        self.tab2Con4G.addWidget(self.tab2Con4Com1, 0, 1)

        self.tab2Con4Bn2 = QtWidgets.QPushButton('绘图')
        self.tab2Con4Com3 = QtWidgets.QComboBox()
        self.tab2Con4G.addWidget(self.tab2Con4Bn2, 1, 0)
        self.tab2Con4G.addWidget(self.tab2Con4Com3, 1, 1)
        self.tab2Con4.setLayout(self.tab2Con4G)

    '''设置Ui界面'''

    def setUi(self):
        '''tab0'''
        # 比特率，添加items
        self.tab0Con0H1Com.addItems(['1200', '2400', '4800', '9600', '14400', '19200', '38400', '56000'])
        # 设置默认item作为选项
        self.tab0Con0H1Com.setCurrentText('9600')

        # 校验位
        self.tab0Con0H2Com.addItems(['EVEN', 'ODD', 'NONE'])
        self.tab0Con0H2Com.setCurrentText('EVEN')

        # 数据位
        self.tab0Con0H3Com.addItems(['8', '7', '6', '5'])
        self.tab0Con0H3Com.setCurrentText('8')

        # 停止位
        self.tab0Con0H4Com.addItems(['1', '1.5', '2'])
        self.tab0Con0H4Com.setCurrentText('1')

        '''tab1'''
        for i in range(4):
            exec('self.tab1Con' + str(i) + "Com1.addItems(['A相', 'B相', 'C相', '三相'])")
            exec("self.tab1Con" + str(i) + "Com3.addItems(['200', '3600', '43200'])")
        self.tab1Con2Com1.insertItem(0, '总功率')
        self.tab1Con3Com1.insertItem(0, '总功率')
        self.tab1Con2Com1.setCurrentIndex(4)
        self.tab1Con3Com1.setCurrentIndex(4)
        self.tab1Con0Com1.setCurrentIndex(3)
        self.tab1Con1Com1.setCurrentIndex(3)


        self.tab1Con4Com1.addItems(['正向有功'])
        self.tab1Con4Com3.addItems(['200', '3600', '43200'])

        '''tab2'''
        for i in range(4):
            exec('self.tab2Con' + str(i) + "Com1.addItems(['A相', 'B相', 'C相', '三相'])")
            exec("self.tab2Con" + str(i) + "Com3.addItems(['200', '3600', '43200'])")

        self.tab2Con2Com1.insertItem(0, '总功率')
        self.tab2Con3Com1.insertItem(0, '总功率')
        self.tab2Con2Com1.setCurrentIndex(4)
        self.tab2Con3Com1.setCurrentIndex(4)
        self.tab2Con0Com1.setCurrentIndex(3)
        self.tab2Con1Com1.setCurrentIndex(3)


        self.tab2Con4Com1.addItems(['正向有功'])
        self.tab2Con4Com3.addItems(['200', '3600', '43200'])




        self.tab0Con1H1Bn.setEnabled(False)
        self.tab0Con1H2Bn.setEnabled(False)
        self.tab0Con1H3Bn.setEnabled(False)
        self.tab0Con1H4Bn.setEnabled(False)
        pass
