import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSHapticFeedbackHelper(AppKit.NSObject):
    def performFeedbackPattern_performanceTime_(self, p, t):
        pass


class TestNSHapticFeedback(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSHapticFeedbackPattern)
        self.assertIsEnumType(AppKit.NSHapticFeedbackPerformanceTime)

    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(AppKit.NSHapticFeedbackPatternGeneric, 0)
        self.assertEqual(AppKit.NSHapticFeedbackPatternAlignment, 1)
        self.assertEqual(AppKit.NSHapticFeedbackPatternLevelChange, 2)

        self.assertEqual(AppKit.NSHapticFeedbackPerformanceTimeDefault, 0)
        self.assertEqual(AppKit.NSHapticFeedbackPerformanceTimeNow, 1)
        self.assertEqual(AppKit.NSHapticFeedbackPerformanceTimeDrawCompleted, 2)

    @min_os_level("10.11")
    def testProtocols10_11(self):
        objc.protocolNamed("NSHapticFeedbackPerformer")
        self.assertArgHasType(
            TestNSHapticFeedbackHelper.performFeedbackPattern_performanceTime_,
            1,
            objc._C_NSUInteger,
        )
