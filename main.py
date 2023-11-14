import sys
from PyQt5.QtWidgets import QApplication
from QMyMainWindow import QMyMainWindow
from QMyWidget import QMyWidget




if __name__ == '__main__':
    app = QApplication(sys.argv)
    '''根据电脑屏幕大小，设置软件窗口尺寸'''
    screen = app.primaryScreen()    # 获取当前的屏幕对象
    available_size = screen.availableGeometry()      # 获取可用屏幕尺寸

    mainWindow = QMyMainWindow(screenSize=available_size)   # 创建自定义主窗口
    '''为主窗口添加中央组件'''
    centralWidget = QMyWidget()   # 创建组件 设置父亲
    mainWindow.setCentralWidget(centralWidget)  # 设置中央组件

    '''输出重定向'''
    sys.stdout = centralWidget.ui.edit
    print = sys.stdout.write

    mainWindow.show()
    app.exec_()




