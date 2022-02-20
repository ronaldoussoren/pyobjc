import Foundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSBackgroundActivityScheduler(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSBackgroundActivityResult)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(Foundation.NSBackgroundActivityResultFinished, 1)
        self.assertEqual(Foundation.NSBackgroundActivityResultDeferred, 2)

    @min_os_level("10.10")
    def testMethods10_10(self):
        Foundation.NSBackgroundActivityCompletionHandler = b"v" + objc._C_NSInteger

        self.assertResultIsBOOL(Foundation.NSBackgroundActivityScheduler.repeats)
        self.assertArgIsBOOL(Foundation.NSBackgroundActivityScheduler.setRepeats_, 0)
        self.assertArgIsBlock(
            Foundation.NSBackgroundActivityScheduler.scheduleWithBlock_,
            0,
            Foundation.NSBackgroundActivityCompletionHandler,
        )
        self.assertResultIsBOOL(Foundation.NSBackgroundActivityScheduler.shouldDefer)
