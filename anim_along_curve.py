#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

This programs animates a ball object 
along a curve.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
'''

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QPixmap, QPainterPath
from PyQt5.QtCore import QObject, QPointF, QPropertyAnimation, pyqtProperty
import sys

                              
class Ball(QLabel):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        pix = QPixmap("ball.png")
        self.h = pix.height()
        self.w = pix.width()
        
        self.setPixmap(pix)
        
    def _set_pos(self, pos):
        
        self.move(pos.x() - self.w/2, pos.y() - self.h/2)

    pos = pyqtProperty(QPointF, fset=_set_pos)   
       
    
class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initAnimation()
        
        
    def paintEvent(self, e):    
        
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)   
        self.drawPath(qp)
        qp.end()       
        
        
    def drawPath(self, qp):
              
        qp.drawPath(self.path)        
        
        
    def initUI(self):    
        
        self.path = QPainterPath()
        self.path.moveTo(30, 30)
        self.path.cubicTo(30, 30, 200, 350, 350, 30)        
        
        self.ball = Ball(self)

        self.ball.pos = QPointF(30, 30)
        
        self.setWindowTitle("Animation along curve")
        self.setGeometry(300, 300, 400, 300)
        self.show()
        
        
    def initAnimation(self):
        
        self.anim = QPropertyAnimation(self.ball, b'pos')
        self.anim.setDuration(7000)
        
        self.anim.setStartValue(QPointF(30, 30))
        
        vals = [p/100 for p in range(0, 101)]

        for i in vals:
            self.anim.setKeyValueAt(i, self.path.pointAtPercent(i))  
                
        self.anim.setEndValue(QPointF(350, 30))        
        self.anim.start()
        
                  
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
