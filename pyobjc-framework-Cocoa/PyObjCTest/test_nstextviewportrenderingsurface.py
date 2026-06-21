import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestNSTextViewportRenderingSurface(TestCase):
    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists("NSTextViewportRenderingSurface", AppKit)
        self.assertProtocolExists("NSTextViewportRenderingSurfaceKey", AppKit)
