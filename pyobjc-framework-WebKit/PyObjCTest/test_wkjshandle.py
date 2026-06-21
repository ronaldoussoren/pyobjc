from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKJSHandle(TestCase):
    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertArgIsBlock(
            WebKit.WKJSHandle.windowProxyFrameInfo_,
            0,
            b"v@",
        )
