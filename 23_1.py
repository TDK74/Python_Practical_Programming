#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

class ToggleButton(QtGui.QWidget):
    
    def __init__(self):
        super(ToggleButton, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        b1 = QtGui.QPushButton('one', self)
        b1.setCheckable(True)
        b1.move(10, 10)
        
        b1.clicked[bool].connect(self.setTitle)
        
        b2 = QtGui.QPushButton('two', self)
        b2.setCheckable(True)
        b2.move(10, 60)
        
        b2.clicked[bool].connect(self.setTitle)
        
        b3 = QtGui.QPushButton('three', self)
        b3.setCheckable(True)
        b3.move(10, 110)
        
        b3.clicked[bool].connect(self.setTitle)
        
        self.setGeometry(300, 200, 180, 170)
        self.setWindowTitle('toggle button')
        self.show()
        
    def setTitle(self, pressed):
        source = self.sender()
        
        if pressed:
            self.setWindowTitle(source.text())
        else:
            self.setWindowTitle('toggle button')
            
def main():
    app = QtGui.QApplication(sys.argv)
    ex = ToggleButton()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
