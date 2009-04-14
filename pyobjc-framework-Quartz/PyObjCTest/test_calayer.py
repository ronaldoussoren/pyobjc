
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
from Quartz.QuartzCore import *

class TestCALayerHelper (NSObject):
    def preferredSizeOfLayer_(self, layer): return 1

class TestCALayer (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessEqual(kCALayerNotSizable, 0)
        self.failUnlessEqual(kCALayerMinXMargin, 1)
        self.failUnlessEqual(kCALayerWidthSizable, 2)
        self.failUnlessEqual(kCALayerMaxXMargin, 4)
        self.failUnlessEqual(kCALayerMinYMargin, 8)
        self.failUnlessEqual(kCALayerHeightSizable, 16)
        self.failUnlessEqual(kCALayerMaxYMargin, 32)
        self.failUnlessEqual(kCALayerLeftEdge, 1)
        self.failUnlessEqual(kCALayerRightEdge, 2)
        self.failUnlessEqual(kCALayerBottomEdge, 4)
        self.failUnlessEqual(kCALayerTopEdge, 8)

        self.failUnlessIsInstance(kCAGravityCenter, unicode)
        self.failUnlessIsInstance(kCAGravityTop, unicode)
        self.failUnlessIsInstance(kCAGravityBottom, unicode)
        self.failUnlessIsInstance(kCAGravityLeft, unicode)
        self.failUnlessIsInstance(kCAGravityRight, unicode)
        self.failUnlessIsInstance(kCAGravityTopLeft, unicode)
        self.failUnlessIsInstance(kCAGravityTopRight, unicode)
        self.failUnlessIsInstance(kCAGravityBottomLeft, unicode)
        self.failUnlessIsInstance(kCAGravityBottomRight, unicode)
        self.failUnlessIsInstance(kCAGravityResize, unicode)
        self.failUnlessIsInstance(kCAGravityResizeAspect, unicode)
        self.failUnlessIsInstance(kCAGravityResizeAspectFill, unicode)
        self.failUnlessIsInstance(kCAFilterLinear, unicode)
        self.failUnlessIsInstance(kCAFilterNearest, unicode)
        self.failUnlessIsInstance(kCAOnOrderIn, unicode)
        self.failUnlessIsInstance(kCAOnOrderOut, unicode)
        self.failUnlessIsInstance(kCATransition, unicode)


    def testMethods(self):
        self.failUnlessResultIsBOOL(CALayer.shouldArchiveValueForKey_)
        self.failUnlessResultIsBOOL(CALayer.isHidden)
        self.failUnlessArgIsBOOL(CALayer.setHidden_, 0)
        self.failUnlessResultIsBOOL(CALayer.isDoubleSided)
        self.failUnlessArgIsBOOL(CALayer.setDoubleSided_, 0)
        self.failUnlessResultIsBOOL(CALayer.masksToBounds)
        self.failUnlessArgIsBOOL(CALayer.setMasksToBounds_, 0)
        self.failUnlessResultIsBOOL(CALayer.containsPoint_)
        self.failUnlessResultIsBOOL(CALayer.isOpaque)
        self.failUnlessArgIsBOOL(CALayer.setOpaque_, 0)
        self.failUnlessResultIsBOOL(CALayer.needsDisplayOnBoundsChange)
        self.failUnlessArgIsBOOL(CALayer.setNeedsDisplayOnBoundsChange_, 0)

        self.failUnlessResultHasType(TestCALayerHelper.preferredSizeOfLayer_, CGSize.__typestr__)




if __name__ == "__main__":
    main()
