#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from sys import *

app = QtGui.QApplication(argv)

window = QtGui.QWidget()
window.setWindowTitle('Grid program')
window.resize(100, 100)

button1 = QtGui.QPushButton('1')
button2 = QtGui.QPushButton('2')
button3 = QtGui.QPushButton('3')
button4 = QtGui.QPushButton('4')

grid = QtGui.QGridLayout()

grid.addWidget(button1, 0, 0)
grid.addWidget(button2, 0, 1)
grid.addWidget(button3, 1, 0)
grid.addWidget(button4, 1, 1)

window.setLayout(grid)

window.show()
exit(app.exec_())
