#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

# syzdavame prilojenie i prozorec
app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle('Sample')

# buton
btn = QPushButton('Click me', w)

@pyqtSlot()
def on_click():
    ''' izvikva se pri klikvane s butona.'''
    print('clicked')
    
@pyqtSlot()
def on_press():
    ''' izvikva se pri natisnat butona.'''
    print('pressed')    

@pyqtSlot()
def on_release():
    ''' izvikva se, kogato butona se otpusne.'''
    print('released')
    
# saediniavane na signalite s tehnite slotove
btn.clicked.connect(on_click)
btn.pressed.connect(on_press)
btn.released.connect(on_release)

# pokazvame prozoreca i startirame prilojenieto
w.show()
app.exec_()



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
    


QtGui.grabShortcut(QtGui.QKeySequence("Ctrl+A"))    # reagirane na klavishna kombinacia

self.edit1.setFocus()   # zadavane na fokus v pole za vavejdane



from PyQt4 import QtCore, QtGui

class Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self, parent)
        widget = QtGui.QWidget(self)
        layout = QtGui.QVBoxLayout(widget)
        self.edit = QtGui.QLineEdit(self)
        self.list = QtGui.QListWidget(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.list)
        slef.setCentralWidget(widget)
        
    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseMove:
            if event.buttons() == QtCore.Qt.NoButton:
                pos = event.pos()
                self.edit.setText('x: %d, y: %d' % (pos.x(), pos.y()))
            else:
                pass # pravim neshto drugo
                
        return QtGui.QMainWindow.eventFilter(self, source, event)
        
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            print("No Button")
        elif event.buttons() == QtCore.Qt.LeftButton:
            print("Left Button")
        elif event.buttons() == QtCore.Qt.RightButton:
            print("Right Button")
            
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.show()
    app.installEventFilter(win)
    sys.exit(application.exec_())
    
    
    
