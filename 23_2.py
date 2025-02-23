#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class CheckBox(QtGui.QWidget):
    
    def __init__(self):
        super(CheckBox, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        cb = QtGui.QCheckBox('show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        self.setGeometry(290, 290, 240, 140)
        self.setWindowTitle('checkbox sample')
        self.show()
        
    def changeTitle(self, state):
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('checkbox sample')
        else:
            self.setWindowTitle('not checked')
            
def main():
    app = QtGui.QApplication(sys.argv)
    ex = CheckBox()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
