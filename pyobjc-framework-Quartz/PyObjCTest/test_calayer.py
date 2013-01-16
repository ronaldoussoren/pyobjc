
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
from Quartz.QuartzCore import *

try:
    unicode
except NameError:
    unicode = str

class TestCALayerHelper (NSObject):
    def preferredSizeOfLayer_(self, layer): return 1

class TestCALayer (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertEqual(kCALayerNotSizable, 0)
        self.assertEqual(kCALayerMinXMargin, 1)
        self.assertEqual(kCALayerWidthSizable, 2)
        self.assertEqual(kCALayerMaxXMargin, 4)
        self.assertEqual(kCALayerMinYMargin, 8)
        self.assertEqual(kCALayerHeightSizable, 16)
        self.assertEqual(kCALayerMaxYMargin, 32)
        self.assertEqual(kCALayerLeftEdge, 1)
        self.assertEqual(kCALayerRightEdge, 2)
        self.assertEqual(kCALayerBottomEdge, 4)
        self.assertEqual(kCALayerTopEdge, 8)

        self.assertIsInstance(kCAGravityCenter, unicode)
        self.assertIsInstance(kCAGravityTop, unicode)
        self.assertIsInstance(kCAGravityBottom, unicode)
        self.assertIsInstance(kCAGravityLeft, unicode)
        self.assertIsInstance(kCAGravityRight, unicode)
        self.assertIsInstance(kCAGravityTopLeft, unicode)
        self.assertIsInstance(kCAGravityTopRight, unicode)
        self.assertIsInstance(kCAGravityBottomLeft, unicode)
        self.assertIsInstance(kCAGravityBottomRight, unicode)
        self.assertIsInstance(kCAGravityResize, unicode)
        self.assertIsInstance(kCAGravityResizeAspect, unicode)
        self.assertIsInstance(kCAGravityResizeAspectFill, unicode)
        self.assertIsInstance(kCAFilterLinear, unicode)
        self.assertIsInstance(kCAFilterNearest, unicode)
        self.assertIsInstance(kCAOnOrderIn, unicode)
        self.assertIsInstance(kCAOnOrderOut, unicode)
        self.assertIsInstance(kCATransition, unicode)


    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(CALayer.shouldArchiveValueForKey_)
        self.assertResultIsBOOL(CALayer.isHidden)
        self.assertArgIsBOOL(CALayer.setHidden_, 0)
        self.assertResultIsBOOL(CALayer.isDoubleSided)
        self.assertArgIsBOOL(CALayer.setDoubleSided_, 0)
        self.assertResultIsBOOL(CALayer.masksToBounds)
        self.assertArgIsBOOL(CALayer.setMasksToBounds_, 0)
        self.assertResultIsBOOL(CALayer.containsPoint_)
        self.assertResultIsBOOL(CALayer.isOpaque)
        self.assertArgIsBOOL(CALayer.setOpaque_, 0)
        self.assertResultIsBOOL(CALayer.needsDisplayOnBoundsChange)
        self.assertArgIsBOOL(CALayer.setNeedsDisplayOnBoundsChange_, 0)

        self.assertResultHasType(TestCALayerHelper.preferredSizeOfLayer_, CGSize.__typestr__)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(CALayer.needsDisplayForKey_)
        self.assertResultIsBOOL(CALayer.isGeometryFlipped)
        self.assertArgIsBOOL(CALayer.setGeometryFlipped_, 0)
        self.assertResultIsBOOL(CALayer.contentsAreFlipped)

        self.assertResultHasType(CALayer.contentsCenter, CGRect.__typestr__)
        self.assertArgHasType(CALayer.setContentsCenter_, 0, CGRect.__typestr__)
        self.assertResultIsBOOL(CALayer.needsDisplay)
        self.assertResultIsBOOL(CALayer.needsLayout)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCAFilterTrilinear, unicode)


if __name__ == "__main__":
    main()
