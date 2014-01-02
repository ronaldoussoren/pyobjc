import Cocoa
import Quartz
import objc

import math

ShadowOffsetChanged = "ShadowOffsetChanged"

class ShadowOffsetView (Cocoa.NSView):
    _offset = objc.ivar(type=Quartz.CGSize.__typestr__)
    _scale = objc.ivar(type=objc._C_FLT)


    def scale(self):
        return self._scale

    def setScale_(self, scale):
        self._scale = scale

    def offset(self):
        return Quartz.CGSizeMake(self._offset.width * self._scale, self._offset.height * self._scale)

    def setOffset_(self, offset):
        offset = Quartz.CGSizeMake(offset.width / self._scale, offset.height / self._scale);
        if self._offset != offset:
            self._offset = offset;
            self.setNeedsDisplay_(True)

    def isOpaque(self):
        return False

    def setOffsetFromPoint_(self, point):
        bounds = self.bounds()
        offset = Quartz.CGSize(
            width = (point.x - Cocoa.NSMidX(bounds)) / (Cocoa.NSWidth(bounds) / 2),
            height = (point.y - Cocoa.NSMidY(bounds)) / (Cocoa.NSHeight(bounds) / 2))
        radius = math.sqrt(offset.width * offset.width + offset.height * offset.height)
        if radius > 1:
            offset.width /= radius;
            offset.height /= radius;

        if self._offset != offset:
            self._offset = offset;
            self.setNeedsDisplay_(True)
            Cocoa.NSNotificationCenter.defaultCenter().postNotificationName_object_(ShadowOffsetChanged, self)

    def mouseDown_(self, event):
        point = self.convertPoint_fromView_(event.locationInWindow(), None)
        self.setOffsetFromPoint_(point)

    def mouseDragged_(self, event):
        point = self.convertPoint_fromView_(event.locationInWindow(), None)
        self.setOffsetFromPoint_(point)

    def drawRect_(self, rect):
        bounds = self.bounds()
        x = Cocoa.NSMinX(bounds)
        y = Cocoa.NSMinY(bounds)
        w = Cocoa.NSWidth(bounds)
        h = Cocoa.NSHeight(bounds)
        r = min(w / 2, h / 2)

        context = Cocoa.NSGraphicsContext.currentContext().graphicsPort()

        Quartz.CGContextTranslateCTM(context, x + w/2, y + h/2)

        Quartz.CGContextAddArc(context, 0, 0, r, 0, math.pi, True)
        Quartz.CGContextClip(context)

        Quartz.CGContextSetGrayFillColor(context, 0.910, 1)
        Quartz.CGContextFillRect(context, Quartz.CGRectMake(-w/2, -h/2, w, h))

        Quartz.CGContextAddArc(context, 0, 0, r, 0, 2*math.pi, True)
        Quartz.CGContextSetGrayStrokeColor(context, 0.616, 1)
        Quartz.CGContextStrokePath(context)

        Quartz.CGContextAddArc(context, 0, -2, r, 0, 2*math.pi, True)
        Quartz.CGContextSetGrayStrokeColor(context, 0.784, 1)
        Quartz.CGContextStrokePath(context)

        Quartz.CGContextMoveToPoint(context, 0, 0)
        Quartz.CGContextAddLineToPoint(context, r * self._offset.width, r * self._offset.height)

        Quartz.CGContextSetLineWidth(context, 2)
        Quartz.CGContextSetGrayStrokeColor(context, 0.33, 1)
        Quartz.CGContextStrokePath(context)
