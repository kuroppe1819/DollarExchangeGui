# -*- coding: utf-8 -*-
import sys
import requests
from PyQt4 import QtGui, QtCore

_size = 40
_getDollar = 0

class Tab1Widget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Tab1Widget, self).__init__()
        global _getDollar

        _getDollar = self.rate()
        label = QtGui.QLabel(_getDollar, self)
        font = QtGui.QFont()
        font.setPointSize(_size)
        label.setFont(font)
        label.move(35, 0)

    def rate(self):
        request = requests.get("http://www.gaitameonline.com/rateaj/getrate").json()
        _getDollar = request['quotes'][20]['ask']
        return _getDollar


class Tab2Widget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Tab2Widget, self).__init__()

        dollar = QtGui.QLabel('ドル')
        yen = QtGui.QLabel('円')
        button = QtGui.QPushButton('→', self)
        button.setFixedWidth(20)
        self.dollarInput = QtGui.QLineEdit()
        self.yenOutput = QtGui.QLineEdit()
        self.dollarInput.setFixedWidth(50)
        self.yenOutput.setFixedWidth(60)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.dollarInput)
        hbox.addWidget(dollar)
        hbox.addStretch(1)
        hbox.addWidget(button)
        hbox.addStretch(1)
        hbox.addWidget(self.yenOutput)
        hbox.addWidget(yen)
        self.setLayout(hbox)
        self.connect(button, QtCore.SIGNAL('clicked()'), self.DollarChange)

    def DollarChange(self):
        global _getDollar
        val = float(self.dollarInput.text())
        self.yenOutput.setText(str(int(val * float(_getDollar))))

class UI(QtGui.QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self.initUI()

    def initUI(self):
        qtab = QtGui.QTabWidget()
        qtab.addTab(Tab1Widget(parent=self), 'レート')
        qtab.addTab(Tab2Widget(parent=self), '変換')
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(qtab)
        self.setLayout(hbox)
        self.setGeometry(0, 30, 250, 100)
        self.setWindowTitle('DollExchange')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()