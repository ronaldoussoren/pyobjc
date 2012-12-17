from Cocoa import *
from Quartz import *
import objc

from Extras import makeRandomPointInRect
from Circle import Circle

gCircleCount = 3

class NSEvent (objc.Category(NSEvent)):
    def locationInView_(self, view):
        return view.convertPoint_fromView_(self.locationInWindow(), None)

class TLayerView (NSView):
    circles = objc.ivar()
    shadowRadius = objc.ivar(type=objc._C_FLT)
    shadowOffset = objc.ivar(type=CGSize.__typestr__)
    useTLayer = objc.ivar(type=objc._C_BOOL)

    def initWithFrame_(self, frame):
        circleRadius = 100
        colors = [
            ( 0.5, 0.0, 0.5, 1 ),
            ( 1.0, 0.7, 0.0, 1 ),
            ( 0.0, 0.5, 0.0, 1 ),
        ]

        self = super(TLayerView, self).initWithFrame_(frame)
        if self is None:
            return None

        self.useTLayer = False;
        self.circles = []

        for c in  colors:
            color = NSColor.colorWithCalibratedRed_green_blue_alpha_(*c)
            circle = Circle.alloc().init()
            circle.color = color
            circle.radius = circleRadius
            circle.center = makeRandomPointInRect(self.bounds())
            self.circles.append(circle)

        self.registerForDraggedTypes_([NSColorPboardType])
        self.setNeedsDisplay_(True)
        return self

    def setShadowRadius_(self, radius):
        if radius != self.shadowRadius:
            self.shadowRadius = radius
            self.setNeedsDisplay_(True)

    def setShadowOffset_(self, offset):
        if self.shadowOffset != offset:
            self.shadowOffset = offset
            self.setNeedsDisplay_(True)

    def setUsesTransparencyLayers_(self, state):
        if self.useTLayer != state:
            self.useTLayer = state
            self.setNeedsDisplay_(True)

    def isOpaque(self):
        return True

    def acceptsFirstMouse_(self, event):
        return True

    def boundsForCircle_(self, circle):
        dx = 2 * abs(self.shadowOffset.width) + 2 * self.shadowRadius;
        dy = 2 * abs(self.shadowOffset.height) + 2 * self.shadowRadius;
        return NSInsetRect(circle.bounds(), -dx, -dy)

    def dragCircleAtIndex_withEvent_(self, index, event):
        circle = self.circles[index]
        del self.circles[index]
        self.circles.append(circle)

        self.setNeedsDisplayInRect_(self.boundsForCircle_(circle))

        mask = NSLeftMouseDraggedMask | NSLeftMouseUpMask;

        start = event.locationInView_(self)

        while (1):
            event = self.window().nextEventMatchingMask_(mask)
            if event.type() == NSLeftMouseUp:
                break

            self.setNeedsDisplayInRect_(self.boundsForCircle_(circle))

            center = circle.center
            point = event.locationInView_(self)
            center.x += point.x - start.x;
            center.y += point.y - start.y;
            circle.center = center

            self.setNeedsDisplayInRect_(self.boundsForCircle_(circle))

            start = point;

    def indexOfCircleAtPoint_(self, point):
        for idx, circle in reversed(list(enumerate(self.circles))):
            center = circle.center
            radius = circle.radius
            dx = point.x - center.x
            dy = point.y - center.y
            if dx * dx + dy * dy < radius * radius:
                return idx
        return -1

    def mouseDown_(self, event):
        point = event.locationInView_(self)
        index = self.indexOfCircleAtPoint_(point)
        if index >= 0:
            self.dragCircleAtIndex_withEvent_(index, event)

    def setFrame_(self, frame):
        super(TLayerView, self).setFrame_(frame)
        self.setNeedsDisplay_(True)

    def drawRect_(self, rect):
        context = NSGraphicsContext.currentContext().graphicsPort()

        CGContextSetRGBFillColor(context, 0.7, 0.7, 0.9, 1)
        CGContextFillRect(context, rect)

        CGContextSetShadow(context, self.shadowOffset, self.shadowRadius)

        if self.useTLayer:
            CGContextBeginTransparencyLayer(context, None)

        for circle in self.circles:
            bounds = self.boundsForCircle_(circle)
            if NSIntersectsRect(bounds, rect):
                circle.draw()

        if self.useTLayer:
            CGContextEndTransparencyLayer(context)

    def draggingEntered_(self, sender):
        # Since we have only registered for NSColorPboardType drags, this is
        # actually unneeded. If you were to register for any other drag types,
        # though, this code would be necessary.

        if (sender.draggingSourceOperationMask() & NSDragOperationGeneric) != 0:
            pasteboard = sender.draggingPasteboard()
            if pasteboard.types().containsObject_(NSColorPboardType):
                return NSDragOperationGeneric

        return NSDragOperationNone

    def performDragOperation_(self, sender):
        point = self.convertPoint_fromView_(sender.draggingLocation(), None)
        index = self.indexOfCircleAtPoint_(point)

        if index >= 0:
            # The current drag location is inside the bounds of a circle so we
            # accept the drop and move on to concludeDragOperation:.
            return True

        return False

    def concludeDragOperation_(self, sender):
        color = NSColor.colorFromPasteboard_(sender.draggingPasteboard())
        point = self.convertPoint_fromView_(sender.draggingLocation(), None)
        index = self.indexOfCircleAtPoint_(point)

        if index >= 0:
            circle = self.circles[index]
            circle.color = color
            self.setNeedsDisplayInRect_(self.boundsForCircle_(circle))
