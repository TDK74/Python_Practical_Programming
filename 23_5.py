#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 
from PyQt4 import QtGui, QtCore 

class ComboBox(QtGui.QWidget):
    
    def __init__(self):
        super(ComboBox, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.label1 = QtGui.QLabel("Windows", self)
        
        combo = QtGui.QComboBox(self)
        combo.addItem("Windows")
        combo.addItem("Linux")
        combo.addItem("FreeBSD")
        combo.addItem("MacOS")
                      
        combo.move(20, 20)
        self.label1.move(30, 150)
        
        combo.activated[str].connect(self.onActivated)
        
        self.setGeometry(200, 200, 200, 200)
        self.setWindowTitle('Combo box')
        self.show()
    
    def onActivated(self, text):
        self.label1.setText(text)
        self.label1.adjustSize()

def main(): 
    app = QtGui.QApplication(sys.argv)
    ex = ComboBox()
    sys.exit(app.exec_()) 

if __name__ == '__main__':
    main()
