#!/usr/bin/python
# -*- coding: utf-8 -*-

# ...
button = QtGui.QPushButton("Button", window)
button.resize(100, 30)
button.move(10, 50)
window.show()
# ...

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



from PyQt4 import QtCore, QtGui
from sys import *

app = QtGui.QApplication(argv)

window = QtGui.QWidget()
window.setWindowTitle('Tabs')
window.resize(200, 200)

# windows = QtGui.QWidget()

tabs = QtGui.QTabWidget()
tabs.addTab(QtGui.QPushButton("1"), "Tab_1")
tabs.addTab(QtGui.QPushButton("2"), "Tab_2")
tabs.addTab(QtGui.QPushButton("3"), "Tab_3")
tabs.setCurrentIndex(0)

vbox = QtGui.QVBoxLayout()
vbox.addWidget(tabs)

window.setLayout(vbox)

window.show()
exit(app.exec_())



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
