from Cocoa import *


class MyBaseGradientView (NSView):
    myGradient = objc.ivar()
    myStartColor = objc.ivar()
    myEndColor = objc.ivar()

    forceColorChange = objc.ivar.bool()
    myAngle = objc.ivar.double()
    myIsRadial = objc.ivar.bool()
    myOffsetPt = objc.ivar.NSPoint()


    def resetGradient(self):
        if self.forceColorChange and self.myGradient is not None:
            self.myGradient = None

        if self.myGradient is None:
            self.myGradient = NSGradient.alloc().initWithStartingColor_endingColor_(
                    self.myStartColor, self.myEndColor)
            self.forceColorChange = False


    def setStartColor_(self, startColor):
        self.myStartColor = startColor
        self.forceColorChange = True
        self.setNeedsDisplay_(True)

    def setEndColor_(self, endColor):
        self.myEndColor = endColor;
        self.forceColorChange = True
        self.setNeedsDisplay_(True)

    def setAngle_(self, angle):
        self.myAngle = angle
        self.setNeedsDisplay_(True)

    def setRadialDraw_(self, isRadial):
        self.myIsRadial = isRadial
        self.setNeedsDisplay_(True)

    def getRelativeCenterPositionFromEvent_(self, theEvent):
        curMousePt = self.convertPoint_fromView_(theEvent.locationInWindow(), None)
        pt = NSMakePoint( (curMousePt.x - NSMidX(self.bounds())) / (self.bounds().size.width / 2.0),
                          (curMousePt.y - NSMidY(self.bounds())) / (self.bounds().size.height / 2.0))
        return pt

    def mouseDown_(self, theEvent):
        if self.myIsRadial:
            self.myOffsetPt = self.getRelativeCenterPositionFromEvent_(theEvent)
            self.setNeedsDisplay_(True)

    def mouseDragged_(self, theEvent):
        if self.myIsRadial:
            self.myOffsetPt = self.getRelativeCenterPositionFromEvent_(theEvent)
            self.setNeedsDisplay_(True)
