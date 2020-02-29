import Cocoa
from MyBaseGradientView import MyBaseGradientView


class MyBezierGradientView(MyBaseGradientView):
    def init(self):
        self = super(MyBaseGradientView, self).init()
        if self is None:
            return None

        self.myOffsetPt = Cocoa.NSMakePoint(0.0, 0.0)
        return self

    def drawRect_(self, rect):
        self.resetGradient()

        bezierPath = Cocoa.NSBezierPath.alloc().init()
        bezierPath.appendBezierPathWithOvalInRect_(rect)

        if self.myIsRadial:
            self.myGradient.drawInBezierPath_relativeCenterPosition_(
                bezierPath, self.myOffsetPt
            )

        else:
            self.myGradient.drawInBezierPath_angle_(bezierPath, self.myAngle)
