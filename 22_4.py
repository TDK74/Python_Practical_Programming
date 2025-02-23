#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from sys import *

app = QtGui.QApplication(argv)

window = QtGui.QWidget()
window.setWindowTitle('Form')
window.resize(200, 100)

Edit1 = QtGui.QLineEdit()
Edit2 = QtGui.QTextEdit()

button1 = QtGui.QPushButton('OK')
button2 = QtGui.QPushButton('Cancel')

hbox = QtGui.QHBoxLayout()

hbox.addWidget(button1)
hbox.addWidget(button2)

form = QtGui.QFormLayout()
form.addRow("Name", Edit1)
form.addRow("Address", Edit2)

form.addRow(hbox)

window.setLayout(form)

window.show()
exit(app.exec_())
