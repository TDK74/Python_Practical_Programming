#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore 

class PB(QtGui.QWidget):
    
    def __init__(self):
        super(PB, self).__init__()
        
        self.initUI()

    def initUI(self):
        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25) 

        self.button1 = QtGui.QPushButton('Start', self)
        self.button1.move(30, 80)
        self.button1.clicked.connect(self.doAction) 

        self.timer = QtCore.QBasicTimer()
        self.step = 0 

        self.setGeometry(300, 250, 280, 170) 
        self.setWindowTitle('QProgressBar') 
        self.show() 

    def timerEvent(self, e): 
        if self.step >= 100:
            self.timer.stop() 
            self.button1.setText('Finished') 
            return 

        self.step = self.step + 1 
        self.pbar.setValue(self.step) 

    def doAction(self):
        if self.timer.isActive(): 
            self.timer.stop() 
            self.button1.setText('Start') 
        else: 
            self.timer.start(100, self) 
            self.button1.setText('Stop') 

def main():
    app = QtGui.QApplication(sys.argv)
    ex = PB()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
