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
            self.setWindowTitle('')
            
def main():
    app = QtGui.QApplication(sys.argv)
    ex = CheckBox()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    
    
    
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
