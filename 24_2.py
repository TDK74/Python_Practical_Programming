#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class InputDialog(QtGui.QWidget): 
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 350, 80) 
        self.setWindowTitle('InputDialog') 
        self.button = QtGui.QPushButton('Dialog', self) 
        self.button.setFocusPolicy(QtCore.Qt.NoFocus) 
        self.button.move(20, 20) 
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
        self.setFocus()
        self.edit1 = QtGui.QLineEdit(self)
        self.edit1.move(130, 22)
        
    def showDialog(self):
        #text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter some text:')
        #text, ok = QtGui.QInputDialog.getInt(self, 'Input Dialog', 'Enter a integer value:')
        #text, ok = QtGui.QInputDialog.getDouble(self, 'Input Dialog', 'Enter a float value:')
        text, ok = QtGui.QInputDialog.getItem(self, 'Input Dialog', 'Please select an OS:',
                                              ["Windows", "Linux", "Mac OS"], current = 1)
        
        if ok:
            #self.edit1.setText(text)
            self.edit1.setText(str(text))

app = QtGui.QApplication(sys.argv)
icon = InputDialog()
icon.show()
app.exec_()
