from Foundation import NSObject
from PyObjCTools import NibClassBuilder
from objc import *
from AppKit import NSBezierPath

from fieldMath import *

#____________________________________________________________
class CGraphModel(NibClassBuilder.AutoBaseClass):

    def init(self):
        self.field = [1.0, 1.12, 0.567]
        self.phase = [degToRad(0), degToRad(152.6), degToRad(312.9-360)]
        self.RMSGain = 0
        self.spacing = degToRad(90)
        return self

    def getGraph(self):
        path = NSBezierPath.bezierPath()

        maxMag = 0
        mag = self.fieldValue(0)

        maxMag = max(maxMag, mag)
        path.moveToPoint_(polarToRect((mag, 0)))
        for deg in range(1, 359, 1):
            r = (deg/180.0)*pi
            mag = self.fieldValue(r)
            maxMag = max(maxMag, mag)
            path.lineToPoint_(polarToRect((mag, r)))
        path.closePath()

        return path, maxMag;

    def fieldGain(self):
        gain = 0
        Et = self.field[0] + self.field[1] + self.field[2]
        if Et:          # Don't want to divide by zero in the pathological case
            spacing = [0, self.spacing, 2*self.spacing]

            # This could easily be optimized--but this is just anexample :-)
            for i in range(3):
                for j in range(3):
                    gain += self.field[i]*self.field[j] * cos(self.phase[j]-self.phase[i]) * bessel(spacing[j]-spacing[i])
            gain = sqrt(gain) / Et

        self.RMSGain = gain
        return gain

    def fieldValue(self, a):
        # The intermedate values are used to more closely match standard field equations nomenclature
        E0 = self.field[0]
        E1 = self.field[1]
        E2 = self.field[2]
        B0 = self.phase[0]
        B1 = self.phase[1] + self.spacing * cos(a)
        B2 = self.phase[2] + 2 * self.spacing * cos(a)

        phix = sin(B0) * E0  + sin(B1) * E1 + sin(B2) * E2
        phiy = cos(B0) * E0 + cos(B1) * E1 + cos(B2) * E2
        mag = hypot(phix, phiy)

        return mag


    def setField(self, tower, field):
        self.field[tower] = field

    def getField(self, tower):
        return self.field[tower]

    def setPhase(self, tower, phase):
        self.phase[tower] = phase

    def getPhase(self, tower):
        return self.phase[tower]

    def setSpacing(self, spacing):
        self.spacing = spacing

    def getSpacing(self):
        return self.spacing
