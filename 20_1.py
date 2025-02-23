#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

def main():
    # predavane na argumentite na prilojenieto,
    # ukazani v komandnia red
    
    app = QtGui.QApplication(sys.argv)
    
    window = QtGui.QWidget()
    window.resize(300, 300)
    window.move(100, 100)
    # window.setGeometry(300, 300, 100, 100)    
    window.setWindowTitle('Example')
    # window.setWindowIcon(QtGui.QIcon('logo.png'))
    window.show()
    
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    
