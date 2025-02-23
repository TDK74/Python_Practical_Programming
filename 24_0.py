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



QtGui.QMessageBox.information(window, "Info", "No errors") 

result = QtGui.QMessageBox.question(self, "Format C:?", "All data will be lost. Are your sure?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, defaultButton = QtGui.QMessageBox.No) 

result = QtGui.QMessageBox.warning(self, "Format C:?", "All data will be lost. Are your sure?", QtGui. QMessageBox.Yes | QtGui.QMessageBox.No, defaultButton = QtGui.QMessageBox.No) 

result = QtGui.QMessageBox.critical(self, "Format C:?", "All data will be lost. Are your sure?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, defaultButton = QtGui.QMessageBox.No)

QtGui.QMessageBox.about(self, "About", "Simple program\n Ver. 1.0.0\n\n (c) 2018 Tsvetan Krastev")



import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class InputDialog(QtGui.QWidget): 
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 350, 80) 
        self.setWindowTitle('InputDialog') 
        self.button = QtGui.QPushButton('Dialog', self) 
        self.button.setFocusPolicy(QtCore.Qt.NoFocus) 
        self.button.move(20, 20) 
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
        self.setFocus()
        self.edit1 = QtGui.QLineEdit(self)
        self.edit1.move(130, 22)
        
    def showDialog(self):
        #text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter some text:')
        #text, ok = QtGui.QInputDialog.getInt(self, 'Input Dialog', 'Enter a integer value:')
        #text, ok = QtGui.QInputDialog.getDouble(self, 'Input Dialog', 'Enter a float value:')
        text, ok = QtGui.QInputDialog.getItem(self, 'Input Dialog', 'Please select an OS:',
                                              ["Windows", "Linux", "Mac OS"], current = 1)
        
        if ok:
            #self.edit1.setText(text)
            self.edit1.setText(str(text))

app = QtGui.QApplication(sys.argv)
icon = InputDialog()
icon.show()
app.exec_()


import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class OpenFile(QtGui.QMainWindow): 
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setGeometry(300, 300, 350, 300) 
        self.setWindowTitle('OpenFile')
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit) 
        self.statusBar() 
        self.setFocus() 
        exit = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        exit.setShortcut('Ctrl+O') 
        exit.setStatusTip('0pen new File')
        self.connect(exit, QtCore.SIGNAL('triggered()'), self.showDialog) 

        menubar = self.menuBar() 
        file = menubar.addMenu('&File') 
        file.addAction(exit) 

    def showDialog(self): 
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\') 
        file = open(filename) 
        data = file.read() 
        self.textEdit.setText(data)
        
app = QtGui.QApplication(sys.argv)
cd = OpenFile()
cd.show()
app.exec_()



import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class FontDialog(QtGui.QWidget): 
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        hbox = QtGui.QHBoxLayout()
        self.setGeometry(500, 300, 550, 110) 
        self.setWindowTitle('FontDialog') 
        button = QtGui.QPushButton('Font', self) 
        button.setFocusPolicy(QtCore.Qt.NoFocus)
        button.move(20, 20)
        hbox.addWidget(button)
        self.connect(button, QtCore.SIGNAL('clicked()'), self.showDialog)
        self.label = QtGui.QLabel('Hello, world!', self)
        self.label.move(130, 20)
        hbox.addWidget(self.label, 1)
        self.setLayout(hbox)
        
    def showDialog(self):
        font, ok = QtGui.QFontDialog.getFont()
        
        if ok:
            self.label.setFont(font)
            
app = QtGui.QApplication(sys.argv)
cd = FontDialog()
cd.show()
app.exec_()


color = QtGui.QColorDialog.getColor()