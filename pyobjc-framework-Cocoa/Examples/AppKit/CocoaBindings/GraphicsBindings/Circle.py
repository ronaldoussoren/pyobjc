#
#  Circle.py
#  GraphicsBindings
#
#  Converted by u.fiedler on feb 2005
#  with great help from Bob Ippolito - Thank you Bob!
#
#  The original version was written in Objective-C by Malcolm Crawford
#  http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

from Foundation import *
from AppKit import *
from objc import ivar
from math import sin, cos #, sqrt, atan2


class Circle(NSObject):
    """
    Graphic protocol to define methods all graphics objects must implement

    Circle class, adopts Graphic protocol
    Adds radius and color, and support for drawing a shadow
    """
    xLoc = ivar(u'xLoc', 'd')
    yLoc = ivar(u'yLoc', 'd')

    radius = ivar(u'radius', 'd')
    color  = ivar(u'color')
    shadowOffset = ivar(u'shadowOffset', 'd')
    shadowAngle  = ivar(u'shadowAngle', 'd') # in radians


    def keysForNonBoundsProperties(cls):
        return [u"xLoc", u"yLoc", u"shadowOffset", u"shadowAngle", u"color", u"radius"]
    keysForNonBoundsProperties = classmethod(keysForNonBoundsProperties)


    def init(self):
        self = super(Circle, self).init()
        if self == None: return None
        self.color = NSColor.redColor()
        self.xLoc = 15.0
        self.yLoc = 15.0
        self.radius = 15.0
        return self

    def description(self):
        return u"circle"

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
        if myColor == None: myColor = NSColor.redColor()
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
            print "Circle only works with NSKeyedArchiver"
        self.xLoc = coder.decodeFloatForKey_(u"xLoc")
        self.yLoc = coder.decodeFloatForKey_(u"yLoc")
        self.radius = coder.decodeFloatForKey_(u"radius")
        self.shadowOffset = coder.decodeFloatForKey_(u"shadowOffset")
        self.shadowAngle = coder.decodeFloatForKey_(u"shadowAngle")

        colorData = coder.decodeObjectForKey_(u"color")
        self.color = NSUnarchiver.unarchiveObjectWithData_(colorData)
        return self

    def encodeWithCoder_(self, coder):
        if not coder.allowsKeyedCoding():
            print "Circle only works with NSKeyedArchiver"
        coder.encodeFloat_forKey_(self.xLoc, u"xLoc")
        coder.encodeFloat_forKey_(self.yLoc, u"yLoc")
        coder.encodeFloat_forKey_(self.radius, u"radius")
        coder.encodeFloat_forKey_(self.shadowOffset, u"shadowOffset")
        coder.encodeFloat_forKey_(self.shadowAngle, u"shadowAngle")

        colorData = NSArchiver.archivedDataWithRootObject_(self.color)
        coder.encodeObject_forKey_(colorData, u"color")


# if any of these properties changes, the bounds have changed
boundsChangingKeys = [u"xLoc", u"yLoc", u"shadowOffset", u"shadowAngle", u"radius"]
Circle.setKeys_triggerChangeNotificationsForDependentKey_(boundsChangingKeys, u"drawingBounds")
