#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore 

class Splitter(QtGui.QWidget):
    
    def __init__(self):
        super(Splitter, self).__init__()
        
        self.initUI() 

    def initUI(self):
        hbox = QtGui.QHBoxLayout(self)
        
        topleft = QtGui.QFrame(self)
        topleft.setFrameShape(QtGui.QFrame.StyledPanel)
        
        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.StyledPanel)
        
        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)
        
        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright) 

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom) 

        hbox.addWidget(splitter2) 
        self.setLayout(hbox)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        
        self.setGeometry(500, 500, 500, 200)
        self.setWindowTitle('Splitter')
        self.show() 

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Splitter()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
