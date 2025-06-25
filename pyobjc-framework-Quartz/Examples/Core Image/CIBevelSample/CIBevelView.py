from math import sin

import objc
import Quartz
import Cocoa
from objc import super  # noqa: A004
from SampleCIView import SampleCIView

NUM_POINTS = 4


class CIBevelView(SampleCIView):
    currentPoint = objc.ivar(type=objc._C_INT)
    points = objc.ivar()
    angleTime = objc.ivar(type=objc._C_FLT)
    lineImage = objc.ivar()
    twirlFilter = objc.ivar()
    heightFieldFilter = objc.ivar()
    shadedFilter = objc.ivar()

    def initWithFrame_(self, frameRect):
        self = super().initWithFrame_(frameRect)
        if self is None:
            return None

        self.points = [None] * NUM_POINTS
        self.points[0] = Quartz.CGPointMake(
            0.5 * frameRect.size.width, frameRect.size.height - 100.0
        )
        self.points[1] = Quartz.CGPointMake(150.0, 100.0)
        self.points[2] = Quartz.CGPointMake(frameRect.size.width - 150.0, 100.0)
        self.points[3] = Quartz.CGPointMake(
            0.7 * self.points[0].x + 0.3 * self.points[2].x,
            0.7 * self.points[0].y + 0.3 * self.points[2].y,
        )

        url = Cocoa.NSURL.fileURLWithPath_(
            Cocoa.NSBundle.mainBundle().pathForResource_ofType_("lightball", "tiff")
        )

        self.lightball = Quartz.CIImage.imageWithContentsOfURL_(url)

        self.heightFieldFilter = Quartz.CIFilter.filterWithName_("CIHeightFieldFromMask")
        self.heightFieldFilter.setDefaults()
        self.heightFieldFilter.setValue_forKey_(15.0, "inputRadius")

        self.twirlFilter = Quartz.CIFilter.filterWithName_("CITwirlDistortion")
        self.twirlFilter.setDefaults()
        self.twirlFilter.setValue_forKey_(
            Quartz.CIVector.vectorWithX_Y_(
                0.5 * frameRect.size.width, 0.5 * frameRect.size.height
            ),
            "inputCenter",
        )
        self.twirlFilter.setValue_forKey_(300.0, "inputRadius")
        self.twirlFilter.setValue_forKey_(0.0, "inputAngle")

        self.shadedFilter = Quartz.CIFilter.filterWithName_("CIShadedMaterial")
        self.shadedFilter.setDefaults()
        self.shadedFilter.setValue_forKey_(self.lightball, "inputShadingImage")
        self.shadedFilter.setValue_forKey_(20.0, "inputScale")

        # 1/30 second should give us decent animation
        Cocoa.NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
            1.0 / 30.0, self, "changeTwirlAngle:", None, True
        )
        return self

    def changeTwirlAngle_(self, timer):
        self.angleTime += timer.timeInterval()
        self.twirlFilter.setValue_forKey_(-0.2 * sin(self.angleTime * 5.0), "inputAngle")
        self.updateImage()

    def mouseDragged_(self, event):
        loc = self.convertPoint_fromView_(event.locationInWindow(), None)
        self.points[self.currentPoint].x = loc.x
        self.points[self.currentPoint].y = loc.y
        self.lineImage = None

        # normally we'd want this, but the timer will cause us to
        # redisplay anyway
        # self.setNeedsDisplay_(True)

    def mouseDown_(self, event):
        d = 1e4
        loc = self.convertPoint_fromView_(event.locationInWindow(), None)
        for i in range(NUM_POINTS):
            x = self.points[i].x - loc.x
            y = self.points[i].y - loc.y
            t = x * x + y * y

            if t < d:
                self.currentPoint = i
                d = t

        self.mouseDragged_(event)

    def updateImage(self):
        context = Cocoa.NSGraphicsContext.currentContext().CIContext()
        if self.lineImage is None:
            bounds = self.bounds()
            layer = context.createCGLayerWithSize_info_(
                Quartz.CGSizeMake(Cocoa.NSWidth(bounds), Cocoa.NSHeight(bounds)), None
            )

            cg = Quartz.CGLayerGetContext(layer)

            Quartz.CGContextSetRGBStrokeColor(cg, 1, 1, 1, 1)
            Quartz.CGContextSetLineCap(cg, Quartz.kCGLineCapRound)

            Quartz.CGContextSetLineWidth(cg, 60.0)
            Quartz.CGContextMoveToPoint(cg, self.points[0].x, self.points[0].y)
            for i in range(1, NUM_POINTS):
                Quartz.CGContextAddLineToPoint(cg, self.points[i].x, self.points[i].y)
            Quartz.CGContextStrokePath(cg)

            self.lineImage = Quartz.CIImage.alloc().initWithCGLayer_(layer)

        self.heightFieldFilter.setValue_forKey_(self.lineImage, "inputImage")
        self.twirlFilter.setValue_forKey_(
            self.heightFieldFilter.valueForKey_("outputImage"), "inputImage"
        )

        self.shadedFilter.setValue_forKey_(
            self.twirlFilter.valueForKey_("outputImage"), "inputImage"
        )

        self.setImage_(self.shadedFilter.valueForKey_("outputImage"))
