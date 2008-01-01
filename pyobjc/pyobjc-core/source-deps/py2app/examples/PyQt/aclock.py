#!/usr/bin/env python

import sys
from qt import *

def QMIN(x, y):
    if y > x: return y
    return x
class AnalogClock(QWidget):
    def __init__(self, *args):
        apply(QWidget.__init__,(self,) + args)
        self.time = QTime.currentTime()
        internalTimer = QTimer(self)
        self.connect(internalTimer, SIGNAL("timeout()"), self.timeout)
        internalTimer.start(5000)

    def timeout(self):
        new_time = QTime.currentTime()
        if new_time.minute() != self.time.minute():
            self.update()

    def paintEvent(self, qe):
        if not self.isVisible():
            return
        self.time = QTime.currentTime()

        pts = QPointArray()
        paint = QPainter(self)
        paint.setBrush(self.foregroundColor())

        cp = QPoint(self.rect().center())
        d = QMIN(self.width(), self.height())
        matrix = QWMatrix()
        matrix.translate(cp.x(), cp.y())
        matrix.scale(d/1000.0, d/1000.0)

        h_angle = 30*(self.time.hour()%12 - 3) + self.time.minute()/2
        matrix.rotate(h_angle)
        paint.setWorldMatrix(matrix)
        pts.setPoints([-20,0,0,-20,300,0,0,20])
        paint.drawPolygon(pts)
        matrix.rotate(-h_angle)

        m_angle = (self.time.minute()-15)*6
        matrix.rotate(m_angle)
        paint.setWorldMatrix(matrix)
        pts.setPoints([-10,0,0,-10,400,0,0,10])
        paint.drawPolygon(pts)
        matrix.rotate(-m_angle)

        for i in range(0,12):
            paint.setWorldMatrix(matrix)
            paint.drawLine(450,0, 500,0)
            matrix.rotate(30)

a = QApplication(sys.argv)
clock = AnalogClock()
clock.resize(100,100)
a.setMainWidget(clock)
clock.show()
a.exec_loop()
