#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

def main():
    
    app = QtGui.QApplication(sys.argv)
    
    # zadavame shrifta
    QtGui.QToolTip.setFont(QtGui.QFont('Arial', 14))
    # parametri na prozoreca
    window = QtGui.QWidget()
    window.setToolTip('This is a window.')
    window.resize(300, 300)
    window.move(100, 100)
    # window.setGeometry(300, 300, 100, 100)
    window.setWindowTitle('Example')
    window.setWindowIcon(QtGui.QIcon('logo.png'))
    
    # parametri na butona
    button = QtGui.QPushButton('Close', window)
    button.clicked.connect(QtCore.QCoreApplication.instance().quit)
    button.move(50, 50)
    button.setToolTip('This is a button.')
    button.resize(button.sizeHint())
    
    window.show()
    
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
