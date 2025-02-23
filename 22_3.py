#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from sys import *

app = QtGui.QApplication(argv)

window = QtGui.QWidget()
window.setWindowTitle('Tabs')
window.resize(200, 200)

windows = QtGui.QWidget()

tabs = QtGui.QTabWidget()
tabs.addTab(QtGui.QPushButton("1"), "Tab_1")
tabs.addTab(QtGui.QPushButton("2"), "Tab_2")
tabs.addTab(QtGui.QPushButton("3"), "Tab_3")
tabs.setCurrentIndex(0)

vbox = QtGui.QHBoxLayout()
vbox.addWidget(tabs)

window.setLayout(vbox)

window.show()
exit(app.exec_())
