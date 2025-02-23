#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class FontDialog(QtGui.QWidget): 
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        hbox = QtGui.QHBoxLayout()
        self.setGeometry(500, 300, 550, 110) 
        self.setWindowTitle('FontDialog') 
        button = QtGui.QPushButton('Font', self) 
        button.setFocusPolicy(QtCore.Qt.NoFocus)
        button.move(20, 20)
        hbox.addWidget(button)
        self.connect(button, QtCore.SIGNAL('clicked()'), self.showDialog)
        self.label = QtGui.QLabel('Hello, world!', self)
        self.label.move(130, 20)
        hbox.addWidget(self.label, 1)
        self.setLayout(hbox)
        
    def showDialog(self):
        font, ok = QtGui.QFontDialog.getFont()
        
        if ok:
            self.label.setFont(font)
            
app = QtGui.QApplication(sys.argv)
cd = FontDialog()
cd.show()
app.exec_()
