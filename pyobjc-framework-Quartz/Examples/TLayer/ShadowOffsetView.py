from Cocoa import *
from Quartz import *
import objc

import math

ShadowOffsetChanged = "ShadowOffsetChanged"

class ShadowOffsetView (NSView):
    _offset = objc.ivar(type=CGSize.__typestr__)
    _scale = objc.ivar(type=objc._C_FLT)


    def scale(self):
        return self._scale

    def setScale_(self, scale):
        self._scale = scale

    def offset(self):
        return CGSizeMake(self._offset.width * self._scale, self._offset.height * self._scale)

    def setOffset_(self, offset):
        offset = CGSizeMake(offset.width / self._scale, offset.height / self._scale);
        if self._offset != offset:
            self._offset = offset;
            self.setNeedsDisplay_(True)

    def isOpaque(self):
        return False

    def setOffsetFromPoint_(self, point):
        bounds = self.bounds()
        offset = CGSize(
            width = (point.x - NSMidX(bounds)) / (NSWidth(bounds) / 2),
            height = (point.y - NSMidY(bounds)) / (NSHeight(bounds) / 2))
        radius = math.sqrt(offset.width * offset.width + offset.height * offset.height)
        if radius > 1:
            offset.width /= radius;
            offset.height /= radius;

        if self._offset != offset:
            self._offset = offset;
            self.setNeedsDisplay_(True)
            NSNotificationCenter.defaultCenter().postNotificationName_object_(ShadowOffsetChanged, self)

    def mouseDown_(self, event):
        point = self.convertPoint_fromView_(event.locationInWindow(), None)
        self.setOffsetFromPoint_(point)

    def mouseDragged_(self, event):
        point = self.convertPoint_fromView_(event.locationInWindow(), None)
        self.setOffsetFromPoint_(point)

    def drawRect_(self, rect):
        bounds = self.bounds()
        x = NSMinX(bounds)
        y = NSMinY(bounds)
        w = NSWidth(bounds)
        h = NSHeight(bounds)
        r = min(w / 2, h / 2)

        context = NSGraphicsContext.currentContext().graphicsPort()

        CGContextTranslateCTM(context, x + w/2, y + h/2)

        CGContextAddArc(context, 0, 0, r, 0, math.pi, True)
        CGContextClip(context)

        CGContextSetGrayFillColor(context, 0.910, 1)
        CGContextFillRect(context, CGRectMake(-w/2, -h/2, w, h))

        CGContextAddArc(context, 0, 0, r, 0, 2*math.pi, True)
        CGContextSetGrayStrokeColor(context, 0.616, 1)
        CGContextStrokePath(context)

        CGContextAddArc(context, 0, -2, r, 0, 2*math.pi, True)
        CGContextSetGrayStrokeColor(context, 0.784, 1)
        CGContextStrokePath(context)

        CGContextMoveToPoint(context, 0, 0)
        CGContextAddLineToPoint(context, r * self._offset.width, r * self._offset.height)

        CGContextSetLineWidth(context, 2)
        CGContextSetGrayStrokeColor(context, 0.33, 1)
        CGContextStrokePath(context)
