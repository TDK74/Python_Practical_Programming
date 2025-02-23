#!/usr/bin/python
# -*- coding: utf-8 -*-
    
import sys
from PyQt4 import QtGui, QtCore

class Calendar(QtGui.QWidget):
    
    def __init__(self):
        super(Calendar, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(30, 30)
        cal.clicked[QtCore.QDate].connect(self.showDate)
        
        self.label1 = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.label1.setText(date.toString())
        self.label1.move(150, 250)
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('calendar')
        self.show()
        
    def showDate(self, date):
        self.label1.setText(date.toString())
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Calendar()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()