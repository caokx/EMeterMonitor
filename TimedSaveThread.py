import os
import sys
import time

import openpyxl
from PyQt5 import QtCore


class TimedSaveThread(QtCore.QThread):
    def __init__(self, DATADIC=None, current_=None):
        super().__init__()
        self.DATADIC = DATADIC
        self.current_ = current_

    def run(self):
        self.write()

    def write(self):
        data = self.DATADIC.copy()
        # 创建excel文件
        xlsx = openpyxl.Workbook()
        # 获取活跃的工作表
        table = xlsx.active
        table.title = "record"

        # 表头
        table['A1'] = "时间"
        table['B1'] = "电压A相(V)"
        table['C1'] = "电压B相(V)"
        table['D1'] = "电压C相(V)"
        table['E1'] = "电流A相(A)"
        table['F1'] = "电流B相(A)"
        table['G1'] = "电流C相(A)"
        table['H1'] = "总功率(W)"
        table['I1'] = "功率A相(W)"
        table['J1'] = "功率B相(W)"
        table['K1'] = "功率C相(W)"
        table['L1'] = "总功率因数"
        table['M1'] = "功率因数A相"
        table['N1'] = "功率因数B相"
        table['O1'] = "功率因数C相"
        table['P1'] = "电能量(kw*h)"

        # 写入
        i = 2
        for key in data.keys():
            table['A' + str(i)] = key
            table['B' + str(i)] = data[key][0]
            table['C' + str(i)] = data[key][1]
            table['D' + str(i)] = data[key][2]
            table['E' + str(i)] = data[key][3]
            table['F' + str(i)] = data[key][4]
            table['G' + str(i)] = data[key][5]
            table['H' + str(i)] = data[key][6]
            table['I' + str(i)] = data[key][7]
            table['J' + str(i)] = data[key][8]
            table['K' + str(i)] = data[key][9]
            table['L' + str(i)] = data[key][10]
            table['M' + str(i)] = data[key][11]
            table['N' + str(i)] = data[key][12]
            table['O' + str(i)] = data[key][13]
            table['P' + str(i)] = data[key][14]
            i += 1
        # 保存
        # 以当前时间命名文件
        time_ = self.current_.strftime('%Y-%m-%d_%H-%M-%S')
        target = 'history/' + time_ + '.xlsx'
        xlsx.save(target)
        xlsx.close()
        # sys.stdout.write('文件已定时保存成功')

