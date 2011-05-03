from MyBaseGradientView import *

class MyBezierGradientView (MyBaseGradientView):
    def init(self):
        self = super(MyBaseGradientView, self).init()
        if self is None:
            return None

        self.myOffsetPt = NSMakePoint(0.0, 0.0)
        return self

    def drawRect_(self, rect):
        self.resetGradient()

        bezierPath = NSBezierPath.alloc().init()
        bezierPath.appendBezierPathWithOvalInRect_(rect)

        if self.myIsRadial:
            self.myGradient.drawInBezierPath_relativeCenterPosition_(bezierPath, self.myOffsetPt)

        else:
            self.myGradient.drawInBezierPath_angle_(bezierPath, self.myAngle)
