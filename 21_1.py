#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *


app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle('Sample')


btn = QPushButton('Click me', w)

@pyqtSlot()
def on_click():
    print('clicked')
    
@pyqtSlot()
def on_press():
    print('pressed')    

@pyqtSlot()
def on_release():
    print('released')
    

btn.clicked.connect(on_click)
btn.pressed.connect(on_press)
btn.released.connect(on_release)


w.show()
app.exec_()
