#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

# syzdavame prilojenie i prozorec
app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle('Sample')

# buton
btn = QPushButton('Click me', w)

@pyqtSlot()
def on_click():
    ''' izvikva se pri klikvane s butona.'''
    print('clicked')
    
@pyqtSlot()
def on_press():
    ''' izvikva se pri natisnat butona.'''
    print('pressed')    

@pyqtSlot()
def on_release():
    ''' izvikva se, kogato butona se otpusne.'''
    print('released')
    
# saediniavane na signalite s tehnite slotove
btn.clicked.connect(on_click)
btn.pressed.connect(on_press)
btn.released.connect(on_release)

# pokazvame prozoreca i startirame prilojenieto
w.show()
app.exec_()

