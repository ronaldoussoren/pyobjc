from MyBaseGradientView import *

class MyRectGradientView (MyBaseGradientView):
    def init(self):
        self = super(MyRectGradientView, self).init()
        if self is None:
            return self
        
        self.myOffsetPt = NSMakePoint(0.0, 0.0)
        return self

    def drawRect_(self, rect):
        self.resetGradient()

        # if the "Radial Gradient" checkbox is turned on, draw using 'myOffsetPt'
        if self.myIsRadial:
            self.myGradient.drawInRect_relativeCenterPosition_(self.bounds(), self.myOffsetPt)

        else:
            self.myGradient.drawInRect_angle_(self.bounds(), self.myAngle)
