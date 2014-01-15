#
#  Circle.py
#  GraphicsBindings
#
#  Converted by u.fiedler on feb 2005
#  with great help from Bob Ippolito - Thank you Bob!
#
#  The original version was written in Objective-C by Malcolm Crawford
#  http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

from Cocoa import NSObject, NSColor, NSMakeRect, NSUnionRect
from Cocoa import NSShadow, NSMakeSize, NSBezierPath
from objc import super
import objc
from math import sin, cos


class Circle(NSObject):
    """
    Graphic protocol to define methods all graphics objects must implement

    Circle class, adopts Graphic protocol
    Adds radius and color, and support for drawing a shadow
    """
    xLoc = objc.ivar('xLoc', objc._C_DBL)
    yLoc = objc.ivar('yLoc', objc._C_DBL)

    radius = objc.ivar('radius', objc._C_DBL)
    color  = objc.ivar('color')
    shadowOffset = objc.ivar('shadowOffset', objc._C_DBL)
    shadowAngle  = objc.ivar('shadowAngle', objc._C_DBL) # in radians

    @classmethod
    def keysForNonBoundsProperties(cls):
        return ["xLoc", "yLoc", "shadowOffset", "shadowAngle", "color", "radius"]


    def init(self):
        self = super(Circle, self).init()
        if self is None:
            return None

        self.color = NSColor.redColor()
        self.xLoc = 15.0
        self.yLoc = 15.0
        self.radius = 15.0
        return self

    def description(self):
        return "circle"

    def drawingBounds(self):
        drawingBounds = NSMakeRect(self.xLoc - self.radius-1, self.yLoc - self.radius-1,
                      self.radius*2+2, self.radius*2+2)
        if self.shadowOffset > 0.0:
            shadowXOffset = sin(self.shadowAngle)*self.shadowOffset
            shadowYOffset = cos(self.shadowAngle)*self.shadowOffset
            # allow for blur
            shadowBounds = NSMakeRect(self.xLoc - self.radius + shadowXOffset - (self.shadowOffset/2),
               self.yLoc - self.radius + shadowYOffset - (self.shadowOffset/2),
               (self.radius*2)+self.shadowOffset,
               (self.radius*2)+self.shadowOffset)
            drawingBounds = NSUnionRect(shadowBounds, drawingBounds)
        return drawingBounds

    def drawInView_(self, aView):
        # ignore aView here for simplicity...
        (xLoc, yLoc, radius, shadowOffset, shadowAngle) = (self.xLoc, self.yLoc, self.radius, self.shadowOffset, self.shadowAngle)

        circleBounds = NSMakeRect(xLoc-radius, yLoc-radius, radius*2, radius*2)

        # draw shadow if we'll see it
        shadow = NSShadow.alloc().init()
        if shadowOffset > 0.00001:
            shadowXOffset = sin(shadowAngle)*shadowOffset
            shadowYOffset = cos(shadowAngle)*shadowOffset
            shadow.setShadowOffset_(NSMakeSize(shadowXOffset,shadowYOffset))
            shadow.setShadowBlurRadius_(shadowOffset)
            shadow.set()

        # draw circle
        circle = NSBezierPath.bezierPathWithOvalInRect_(circleBounds)
        myColor = self.color
        if myColor is None:
            myColor = NSColor.redColor()
        myColor.set()
        circle.fill()

        shadow.setShadowColor_(None)
        shadow.set()

    def hitTest_isSelected_(self, point, isSelected):
        # ignore isSelected here for simplicity...
        # don't count shadow for selection
        hypotenuse2 = pow((self.xLoc - point.x), 2.0) + pow((self.yLoc - point.y), 2.0)
        return hypotenuse2 < (self.radius * self.radius)


    def initWithCoder_(self, coder):
        if not coder.allowsKeyedCoding():
            print("Circle only works with NSKeyedArchiver")
        self.xLoc = coder.decodeFloatForKey_("xLoc")
        self.yLoc = coder.decodeFloatForKey_("yLoc")
        self.radius = coder.decodeFloatForKey_("radius")
        self.shadowOffset = coder.decodeFloatForKey_("shadowOffset")
        self.shadowAngle = coder.decodeFloatForKey_("shadowAngle")

        colorData = coder.decodeObjectForKey_("color")
        self.color = NSUnarchiver.unarchiveObjectWithData_(colorData)
        return self

    def encodeWithCoder_(self, coder):
        if not coder.allowsKeyedCoding():
            print("Circle only works with NSKeyedArchiver")
        coder.encodeFloat_forKey_(self.xLoc, "xLoc")
        coder.encodeFloat_forKey_(self.yLoc, "yLoc")
        coder.encodeFloat_forKey_(self.radius, "radius")
        coder.encodeFloat_forKey_(self.shadowOffset, "shadowOffset")
        coder.encodeFloat_forKey_(self.shadowAngle, "shadowAngle")

        colorData = NSArchiver.archivedDataWithRootObject_(self.color)
        coder.encodeObject_forKey_(colorData, u"color")


# if any of these properties changes, the bounds have changed
boundsChangingKeys = ["xLoc", "yLoc", "shadowOffset", "shadowAngle", "radius"]
Circle.setKeys_triggerChangeNotificationsForDependentKey_(boundsChangingKeys, u"drawingBounds")
