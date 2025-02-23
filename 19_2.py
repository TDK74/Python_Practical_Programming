#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, uic
from sys import *

application = QtGui.QApplication(argv)

window = uic.loadUi("Main.ui")

QtCore.QObject.connect(window.pushButton, QtCore.SIGNAL('clicked()'), QtGui.qApp.quit)
# QtCore.QObject.connect(window.pushButton, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))

window.show()
exit(application.exec_())
