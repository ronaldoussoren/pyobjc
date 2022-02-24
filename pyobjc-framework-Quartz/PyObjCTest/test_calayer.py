from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import Quartz
import objc


class TestCALayerHelper(Quartz.NSObject):
    def preferredSizeOfLayer_(self, layer):
        return 1


class TestCALayer(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Quartz.CALayerContentsFilter, str)
        self.assertIsTypedEnum(Quartz.CALayerContentsFormat, str)
        self.assertIsTypedEnum(Quartz.CALayerContentsGravity, str)
        self.assertIsTypedEnum(Quartz.CALayerCornerCurve, str)

    @min_os_level("10.5")
    def testConstants(self):
        self.assertEqual(Quartz.kCALayerNotSizable, 0)
        self.assertEqual(Quartz.kCALayerMinXMargin, 1)
        self.assertEqual(Quartz.kCALayerWidthSizable, 2)
        self.assertEqual(Quartz.kCALayerMaxXMargin, 4)
        self.assertEqual(Quartz.kCALayerMinYMargin, 8)
        self.assertEqual(Quartz.kCALayerHeightSizable, 16)
        self.assertEqual(Quartz.kCALayerMaxYMargin, 32)
        self.assertEqual(Quartz.kCALayerLeftEdge, 1)
        self.assertEqual(Quartz.kCALayerRightEdge, 2)
        self.assertEqual(Quartz.kCALayerBottomEdge, 4)
        self.assertEqual(Quartz.kCALayerTopEdge, 8)

        self.assertIsInstance(Quartz.kCAGravityCenter, str)
        self.assertIsInstance(Quartz.kCAGravityTop, str)
        self.assertIsInstance(Quartz.kCAGravityBottom, str)
        self.assertIsInstance(Quartz.kCAGravityLeft, str)
        self.assertIsInstance(Quartz.kCAGravityRight, str)
        self.assertIsInstance(Quartz.kCAGravityTopLeft, str)
        self.assertIsInstance(Quartz.kCAGravityTopRight, str)
        self.assertIsInstance(Quartz.kCAGravityBottomLeft, str)
        self.assertIsInstance(Quartz.kCAGravityBottomRight, str)
        self.assertIsInstance(Quartz.kCAGravityResize, str)
        self.assertIsInstance(Quartz.kCAGravityResizeAspect, str)
        self.assertIsInstance(Quartz.kCAGravityResizeAspectFill, str)
        self.assertIsInstance(Quartz.kCAFilterLinear, str)
        self.assertIsInstance(Quartz.kCAFilterNearest, str)
        self.assertIsInstance(Quartz.kCAOnOrderIn, str)
        self.assertIsInstance(Quartz.kCAOnOrderOut, str)
        self.assertIsInstance(Quartz.kCATransition, str)

        self.assertEqual(Quartz.kCALayerMinXMinYCorner, 1 << 0)
        self.assertEqual(Quartz.kCALayerMaxXMinYCorner, 1 << 1)
        self.assertEqual(Quartz.kCALayerMinXMaxYCorner, 1 << 2)
        self.assertEqual(Quartz.kCALayerMaxXMaxYCorner, 1 << 3)

    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.CALayer.shouldArchiveValueForKey_)
        self.assertResultIsBOOL(Quartz.CALayer.isHidden)
        self.assertArgIsBOOL(Quartz.CALayer.setHidden_, 0)
        self.assertResultIsBOOL(Quartz.CALayer.isDoubleSided)
        self.assertArgIsBOOL(Quartz.CALayer.setDoubleSided_, 0)
        self.assertResultIsBOOL(Quartz.CALayer.masksToBounds)
        self.assertArgIsBOOL(Quartz.CALayer.setMasksToBounds_, 0)
        self.assertResultIsBOOL(Quartz.CALayer.containsPoint_)
        self.assertResultIsBOOL(Quartz.CALayer.isOpaque)
        self.assertArgIsBOOL(Quartz.CALayer.setOpaque_, 0)
        self.assertResultIsBOOL(Quartz.CALayer.needsDisplayOnBoundsChange)
        self.assertArgIsBOOL(Quartz.CALayer.setNeedsDisplayOnBoundsChange_, 0)

        self.assertResultHasType(
            TestCALayerHelper.preferredSizeOfLayer_, Quartz.CGSize.__typestr__
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(Quartz.CALayer.needsDisplayForKey_)
        self.assertResultIsBOOL(Quartz.CALayer.isGeometryFlipped)
        self.assertArgIsBOOL(Quartz.CALayer.setGeometryFlipped_, 0)
        self.assertResultIsBOOL(Quartz.CALayer.contentsAreFlipped)

        self.assertResultHasType(
            Quartz.CALayer.contentsCenter, Quartz.CGRect.__typestr__
        )
        self.assertArgHasType(
            Quartz.CALayer.setContentsCenter_, 0, Quartz.CGRect.__typestr__
        )
        self.assertResultIsBOOL(Quartz.CALayer.needsDisplay)
        self.assertResultIsBOOL(Quartz.CALayer.needsLayout)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(Quartz.CALayer.shouldRasterize)
        self.assertArgIsBOOL(Quartz.CALayer.setShouldRasterize_, 0)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(Quartz.CALayer.drawsAsynchronously)
        self.assertArgIsBOOL(Quartz.CALayer.setDrawsAsynchronously_, 0)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(Quartz.CALayer.allowsEdgeAntialiasing)
        self.assertArgIsBOOL(Quartz.CALayer.setAllowsEdgeAntialiasing_, 0)
        self.assertResultIsBOOL(Quartz.CALayer.allowsGroupOpacity)
        self.assertArgIsBOOL(Quartz.CALayer.setAllowsGroupOpacity_, 0)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(Quartz.kCAFilterTrilinear, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(Quartz.kCAContentsFormatRGBA8Uint, str)
        self.assertIsInstance(Quartz.kCAContentsFormatRGBA16Float, str)
        self.assertIsInstance(Quartz.kCAContentsFormatGray8Uint, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(Quartz.kCACornerCurveCircular, str)
        self.assertIsInstance(Quartz.kCACornerCurveContinuous, str)

    @min_sdk_level("10.6")
    def testProtocols(self):
        objc.protocolNamed("CAAction")

    @min_sdk_level("10.12")
    def testProtocols10_12(self):
        objc.protocolNamed("CALayerDelegate")
        objc.protocolNamed("CALayoutManager")
