import Cocoa
import objc
import Quartz
from objc import super  # noqa: A004
from SampleCIView import SampleCIView


class CIMicroPaintView(SampleCIView):
    imageAccumulator = objc.ivar()
    brushFilter = objc.ivar()
    compositeFilter = objc.ivar()
    color = objc.ivar()
    brushSize = objc.ivar(objc._C_FLT)

    def initWithFrame_(self, frame):
        self = super().initWithFrame_(frame)
        if self is None:
            return None

        self.brushSize = 25.0
        self.color = Cocoa.NSColor.colorWithDeviceRed_green_blue_alpha_(
            0.0, 0.0, 0.0, 1.0
        )

        self.brushFilter = Quartz.CIFilter.filterWithName_("CIRadialGradient")
        self.brushFilter.setDefaults()
        for k, v in (
            (
                "inputColor1",
                Quartz.CIColor.colorWithRed_green_blue_alpha_(0.0, 0.0, 0.0, 0.0),
            ),
            ("inputRadius0", 0.0),
        ):
            self.brushFilter.setValue_forKey_(v, k)

        self.compositeFilter = Quartz.CIFilter.filterWithName_("CISourceOverCompositing")
        self.compositeFilter.setDefaults()

        return self

    def viewBoundsDidChange_(self, bounds):
        if self.imageAccumulator is not None and bounds == self.imageAccumulator.extent():
            print("Nothing changed")
            return

        # Create a new accumulator and composite the old one over the it.

        c = Quartz.CIImageAccumulator.alloc().initWithExtent_format_(
            bounds, Quartz.kCIFormatRGBA16
        )
        f = Quartz.CIFilter.filterWithName_("CIConstantColorGenerator")
        f.setDefaults()
        f.setValue_forKey_(
            Quartz.CIColor.colorWithRed_green_blue_alpha_(1.0, 1.0, 1.0, 1.0),
            "inputColor",
        )

        if self.imageAccumulator is not None:
            f = Quartz.CIFilter.filterWithName_("CISourceOverCompositing")
            f.setDefaults()
            f.setValue_forKey_(self.imageAccumulator.image(), "inputImage")
            f.setValue_forKey_(c.image(), "inputBackgroundImage")
            c.setImage_(f.valueForKey_("outputImage"))

        self.imageAccumulator = c
        self.setImage_(self.imageAccumulator.image())

    def mouseDragged_(self, event):
        loc = self.convertPoint_fromView_(event.locationInWindow(), None)

        rect = Quartz.CGRectMake(
            loc.x - self.brushSize,
            loc.y - self.brushSize,
            2.0 * self.brushSize,
            2.0 * self.brushSize,
        )
        self.brushFilter.setValue_forKey_(self.brushSize, "inputRadius1")

        cicolor = Quartz.CIColor.alloc().initWithColor_(self.color)
        self.brushFilter.setValue_forKey_(cicolor, "inputColor0")

        self.brushFilter.setValue_forKey_(
            Quartz.CIVector.vectorWithX_Y_(loc.x, loc.y), "inputCenter"
        )

        self.compositeFilter.setValue_forKey_(
            self.brushFilter.valueForKey_("outputImage"), "inputImage"
        )
        self.compositeFilter.setValue_forKey_(
            self.imageAccumulator.image(), "inputBackgroundImage"
        )

        self.imageAccumulator.setImage_dirtyRect_(
            self.compositeFilter.valueForKey_("outputImage"), rect
        )

        self.setImage_dirtyRect_(self.imageAccumulator.image(), rect)

    def mouseDown_(self, event):
        self.mouseDragged_(event)
