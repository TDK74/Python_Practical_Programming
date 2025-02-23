#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from sys import *

app = QtGui.QApplication(argv)

window = QtGui.QWidget()
window.setWindowTitle('Checkbox')
window.resize(200, 100)

box = QtGui.QVBoxLayout()
radiobox1 = QtGui.QRadioButton('Windows')
radiobox2 = QtGui.QRadioButton('Linux')
radiobox3 = QtGui.QRadioButton('Mac OS')

gb = QtGui.QGroupBox('Select yout OS: ')
hbox = QtGui.QHBoxLayout()
hbox.addWidget(radiobox1)
hbox.addWidget(radiobox2)
hbox.addWidget(radiobox3)

gb.setLayout(hbox)

box.addWidget(gb)

window.setLayout(box)

window.show()
exit(app.exec_())