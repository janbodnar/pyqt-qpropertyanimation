#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

This programs animates the color of a QLabel.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, 
        QLabel, QHBoxLayout, QSizePolicy)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty
import sys


class MyLabel(QLabel):
    
    def __init__(self, text):
        super().__init__(text)

    def _set_color(self, col):
        
        palette = self.palette()
        palette.setColor(self.foregroundRole(), col)
        self.setPalette(palette)

    color = pyqtProperty(QColor, fset=_set_color)


class Example(QWidget):

    def __init__(self):
        super().__init__()


        self.initUI()
        
        
    def initUI(self):     

        hbox = QHBoxLayout(self)
        
        self.button = QPushButton("Start", self)
        self.button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        hbox.addWidget(self.button)
        
        hbox.addSpacing(40)

        self.label = MyLabel("Summer")
        font = self.label.font()
        font.setPointSize(35)
        self.label.setFont(font)
        hbox.addWidget(self.label)

        self.anim = QPropertyAnimation(self.label, b"color")
        self.anim.setDuration(2500)
        self.anim.setLoopCount(2)
        self.anim.setStartValue(QColor(0, 0, 0))
        self.anim.setEndValue(QColor(255, 255, 255))

        self.button.clicked.connect(self.anim.start)
        
        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Color anim')
        self.show()    
        
if __name__ == "__main__":
    
    app = QApplication([])
    ex = Example()
    ex.show()
    app.exec_()
