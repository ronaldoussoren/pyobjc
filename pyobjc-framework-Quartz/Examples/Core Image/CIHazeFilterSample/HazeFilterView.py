import objc
import Quartz
import Cocoa

import MyHazeFilter

class HazeFilterView (Cocoa.NSView):
    filter = objc.ivar()
    distance = objc.ivar(type=objc._C_FLT)
    slope = objc.ivar(type=objc._C_FLT)

    def distanceSliderChanged_(self, sender):
        self.distance = sender.floatValue()
        self.setNeedsDisplay_(True)

    def slopeSliderChanged_(self, sender):
        self.slope = sender.floatValue()
        self.setNeedsDisplay_(True)

    def drawRect_(self, rect):
        cg = Quartz.CGRectMake(
                Cocoa.NSMinX(rect), Cocoa.NSMinY(rect), Cocoa.NSWidth(rect), Cocoa.NSHeight(rect))

        context = Cocoa.NSGraphicsContext.currentContext().CIContext()

        if self.filter is None:
            # make sure initialize is called
            MyHazeFilter.MyHazeFilter.pyobjc_classMethods.class__()

            url = Cocoa.NSURL.fileURLWithPath_(
                Cocoa.NSBundle.mainBundle().pathForResource_ofType_(
                    "CraterLake", "jpg"))
            self.filter = Quartz.CIFilter.filterWithName_("MyHazeRemover")
            self.filter.setValue_forKey_(
                Quartz.CIImage.imageWithContentsOfURL_(url),
                "inputImage")

            self.filter.setValue_forKey_(
                Quartz.CIColor.colorWithRed_green_blue_(0.7, 0.9,  1),
                "inputColor")

        self.filter.setValue_forKey_(self.distance, "inputDistance")
        self.filter.setValue_forKey_(self.slope, "inputSlope")

        if context is not None:
            context.drawImage_atPoint_fromRect_(
                    self.filter.valueForKey_("outputImage"),
                    cg.origin, cg)
