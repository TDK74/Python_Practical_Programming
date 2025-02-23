#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class My(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(300, 100)
        
    def changeEvent(self, e):
        if e.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():
                print("minimized")
            elif self.isMaximized():
                print("maximized")
            elif self.isFullScreen():
                print("full screen")
                
        QtGui.QWidget.changeEvent(self, e)
        
if __name__ == "__main__":
    import sys
    application = QtGui.QApplication(sys.argv)
    window = My()
    window.show()
    sys.exit(application.exec_())
