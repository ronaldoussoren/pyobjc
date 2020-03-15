import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSFilePromiseProviderHelper(AppKit.NSObject):
    def filePromiseProvider_writePromiseToURL_completionHandler_(self, p, u, h):
        pass


class TestNSFilePromiseProvider(TestCase):
    @min_sdk_level("10.12")
    def testProtocols(self):
        objc.protocolNamed("NSFilePromiseProviderDelegate")

    def testMethods(self):
        self.assertArgIsBlock(
            TestNSFilePromiseProviderHelper.filePromiseProvider_writePromiseToURL_completionHandler_,  # noqa: B950
            2,
            b"v@",
        )
