#!/usr/bin/python
# -*- coding: utf-8 -*-
   
import sys  
from PyQt4 import QtGui, QtCore  

class EditText(QtGui.QWidget):
    
    def	__init__(self):
        super(EditText, self).__init__()
        
        self.initUI()
    
    def initUI(self):
        self.label1 = QtGui.QLabel(self)
        edit1 = QtGui.QLineEdit(self)
        
        edit1.move(60, 100)
        self.label1.move(60, 40)
        
        edit1.textChanged[str].connect(self.onChanged)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Edit text')
        self.show()
        
    def onChanged(self, text):
        self.label1.setText(text)
        self.label1.adjustSize() 
        
def main():

    app = QtGui.QApplication(sys.argv)
    ex = EditText()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
