import Metal
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level

MTL4CommitFeedbackHandler = b"v@"


class TestMTL4CommitFeedbackHelper(Metal.NSObject):
    def GPUStartTime(self):
        return 1

    def GPUEndTime(self):
        return 1


class TestMTL4CommitFeedback(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4CommitFeedback")

    def test_protocol_methos(self):
        self.assertResultHasType(TestMTL4CommitFeedbackHelper.GPUStartTime, objc._C_DBL)
        self.assertResultHasType(TestMTL4CommitFeedbackHelper.GPUEndTime, objc._C_DBL)
