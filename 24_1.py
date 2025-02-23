#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui 

class MessageBox(QtGui.QWidget): 
    def __init__(self):
        super(MessageBox, self).__init__() 
        
        self.initUI() 

    def initUI(self):
        self.setGeometry(300, 300, 250, 150) 
        self.setWindowTitle('Message box')
        self.show()
        
    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                            QtGui.QMessageBox.Yes | 
                                            QtGui.QMessageBox.No, QtGui.QMessageBox.No) 

        if result == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 

def main():
    app = QtGui.QApplication(sys.argv)
    ex = MessageBox()
    sys.exit(app.exec_()) 

if __name__ == '__main__':
    main()
