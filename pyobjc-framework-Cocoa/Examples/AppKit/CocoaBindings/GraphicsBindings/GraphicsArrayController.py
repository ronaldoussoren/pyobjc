#
#  GraphicsArrayController.py
#  GraphicsBindings
#
#  Converted by u.fiedler on feb 2005
#  with great help from Bob Ippolito - Thank you Bob!
#
#  The original version was written in Objective-C by Malcolm Crawford
#  http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

from sys import maxint
from Foundation import *
from AppKit import *
from random import random
from math import fabs

class GraphicsArrayController (NSArrayController):
    """Allow filtering by color, just for the fun of it"""

    filterColor = objc.IBOutlet()
    newCircle = objc.IBOutlet()
    shouldFilter = objc.ivar.BOOL()
    graphicsView = objc.IBOutlet()

    def arrangeObjects_(self, objects):
        "Filtering is not yet connected in IB!"
        # XXX: This doesn't work yet, so disable
        if self.shouldFilter:
            self.shouldFilter = False

        if not self.shouldFilter:
            return super(GraphicsArrayController, self).arrangeObjects_(objects)

        if self.filterColor is None:
            self.filterColor = NSColor.blackColor().colorUsingColorSpaceName_(NSCalibratedRGBColorSpace)

        filterHue = self.filterColor.hueComponent()
        filteredObjects = []
        for item in objects:
            hue = item.color.hueComponent()
            if ((fabs(hue - filterHue) < 0.05) or
                (fabs(hue - filterHue) > 0.95) or
                (item is self.newCircle)):
                filteredObjects.append(item)
                self.newCircle = None
        return super(GraphicsArrayController, self).arrangeObjects_(filteredObjects)
        
    def newObject(self):
        "Randomize attributes of new circles so we get a pretty display"
        self.newCircle = super(GraphicsArrayController, self).newObject()
        radius = 5.0 + 15.0 * random()
        self.newCircle.radius = radius
        
        height = self.graphicsView.bounds().size.height
        width  = self.graphicsView.bounds().size.width
        
        xOffset = 10.0 + (height - 20.0) * random()
        yOffset = 10.0 + (width - 20.0) * random()
        
        self.newCircle.xLoc = xOffset
        self.newCircle.yLoc = height - yOffset
        
        color = NSColor.colorWithCalibratedHue_saturation_brightness_alpha_(
            random(),
            (0.5 + random() / 2.0),
            (0.333 + random() / 3.0),
            1.0)
        
        self.newCircle.color = color
        return self.newCircle
