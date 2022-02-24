import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAsynchronousKeyValueLoadingHelper(AVFoundation.NSObject):
    def statusOfValueForKey_error_(self, k, e):
        return 1

    def loadValuesAsynchronouslyForKeys_completionHandler_(self, k, h):
        pass


class TestAVAsynchronousKeyValueLoading(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVKeyValueStatus)

    @min_os_level("10.7")
    def testConstants(self):
        self.assertEqual(AVFoundation.AVKeyValueStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVKeyValueStatusLoading, 1)
        self.assertEqual(AVFoundation.AVKeyValueStatusLoaded, 2)
        self.assertEqual(AVFoundation.AVKeyValueStatusFailed, 3)
        self.assertEqual(AVFoundation.AVKeyValueStatusCancelled, 4)

    @min_os_level("10.7")
    def testProtocols(self):
        objc.protocolNamed("AVAsynchronousKeyValueLoading")

        self.assertResultHasType(
            TestAVAsynchronousKeyValueLoadingHelper.statusOfValueForKey_error_,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestAVAsynchronousKeyValueLoadingHelper.statusOfValueForKey_error_,
            1,
            b"o^@",
        )
        self.assertArgIsBlock(
            TestAVAsynchronousKeyValueLoadingHelper.loadValuesAsynchronouslyForKeys_completionHandler_,  # noqa: B950
            1,
            b"v",
        )
