from PyObjCTools.TestSupport import TestCase, min_sdk_level

import Accessibility


class TestAXBrailleMapHelper(Accessibility.NSObject):
    def accessibilityBrailleMapRenderRegion(self):
        return 1

    def setAccessibilityBrailleMapRenderRegion_(self, a):
        pass

    def accessibilityBrailleMapRenderer(self):
        return 1

    def setAccessibilityBrailleMapRenderer_(self, a):
        pass


class TestAXBrailleMap(TestCase):
    @min_sdk_level("12.1")
    def test_protocols(self):
        self.assertProtocolExists("AXBrailleMapRenderer")

    def test_methods(self):
        self.assertResultHasType(
            TestAXBrailleMapHelper.accessibilityBrailleMapRenderRegion,
            Accessibility.CGRect.__typestr__,
        )
        self.assertArgHasType(
            TestAXBrailleMapHelper.setAccessibilityBrailleMapRenderRegion_,
            0,
            Accessibility.CGRect.__typestr__,
        )

        self.assertResultIsBlock(
            TestAXBrailleMapHelper.accessibilityBrailleMapRenderer, b"v@"
        )
        self.assertArgIsBlock(
            TestAXBrailleMapHelper.setAccessibilityBrailleMapRenderer_, 0, b"v@"
        )
