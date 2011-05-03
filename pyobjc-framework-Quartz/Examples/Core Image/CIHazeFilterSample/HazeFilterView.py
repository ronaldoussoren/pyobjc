from Cocoa import *
from Quartz import *

import objc

import MyHazeFilter

class HazeFilterView (NSView):
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
        cg = CGRectMake(
                NSMinX(rect), NSMinY(rect), NSWidth(rect), NSHeight(rect))
        
        context = NSGraphicsContext.currentContext().CIContext()
            
        if self.filter is None:
            # make sure initialize is called
            MyHazeFilter.MyHazeFilter.pyobjc_classMethods.class__()   

            url = NSURL.fileURLWithPath_(
                NSBundle.mainBundle().pathForResource_ofType_(
                    "CraterLake", "jpg"))
            self.filter = CIFilter.filterWithName_("MyHazeRemover")
            self.filter.setValue_forKey_(
                CIImage.imageWithContentsOfURL_(url),
                "inputImage")

            self.filter.setValue_forKey_(
                CIColor.colorWithRed_green_blue_(0.7, 0.9,  1),
                "inputColor") 

        self.filter.setValue_forKey_(self.distance, "inputDistance")
        self.filter.setValue_forKey_(self.slope, "inputSlope")

        if context is not None:
            context.drawImage_atPoint_fromRect_(
                    self.filter.valueForKey_("outputImage"),
                    cg.origin, cg)
