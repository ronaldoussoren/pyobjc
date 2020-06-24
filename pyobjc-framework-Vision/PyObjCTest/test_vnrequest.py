import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import Vision

VNRequestProgressHandler = b"v@d@"


class TestVNRequestHelper(Vision.NSObject):
    def progressHandler(self):
        return 1

    def setProgressHandler_(self, v):
        pass

    def indeterminate(self):
        return 1


class TestVNRequest(TestCase):
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(Vision.VNRequest.initWithCompletionHandler_, 0, b"v@@")
        self.assertResultIsBOOL(Vision.VNRequest.preferBackgroundProcessing)
        self.assertArgIsBOOL(Vision.VNRequest.setPreferBackgroundProcessing_, 0)
        self.assertResultIsBOOL(Vision.VNRequest.usesCPUOnly)
        self.assertArgIsBOOL(Vision.VNRequest.setUsesCPUOnly_, 0)
        self.assertResultIsBlock(Vision.VNRequest.completionHandler, b"v@@")

        self.assertResultIsBlock(
            TestVNRequestHelper.progressHandler, VNRequestProgressHandler
        )
        self.assertArgIsBlock(
            TestVNRequestHelper.setProgressHandler_, 0, VNRequestProgressHandler
        )
        self.assertResultIsBOOL(TestVNRequestHelper.indeterminate)

    def test_constants(self):
        self.assertEqual(Vision.VNRequestRevisionUnspecified, 0)

    @min_sdk_level("10.15")
    def testProtocols(self):
        objc.protocolNamed("VNRequestProgressProviding")
