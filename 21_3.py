#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        widget = QtGui.QWidget(self)
        layout = QtGui.QVBoxLayout(widget)
        self.edit = QtGui.QLineEdit(self)
        self.list = QtGui.QListWidget(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.list)
        self.setCentralWidget(widget)
        
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
    sys.exit(app.exec_())
