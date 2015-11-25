from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSHapticFeedbackHelper (NSObject):
    def performFeedbackPattern_performanceTime_(self, p, t): pass

class TestNSHapticFeedback (TestCase):
    @min_os_level('10.11')
    def testConstants(self):
        self.assertEqual(NSHapticFeedbackPatternGeneric, 0)
        self.assertEqual(NSHapticFeedbackPatternAlignment, 1)
        self.assertEqual(NSHapticFeedbackPatternLevelChange, 2)

        self.assertEqual(NSHapticFeedbackPerformanceTimeDefault, 0)
        self.assertEqual(NSHapticFeedbackPerformanceTimeNow, 1)
        self.assertEqual(NSHapticFeedbackPerformanceTimeDrawCompleted, 2)

    @min_os_level('10.11')
    def testProtocols10_11(self):
        objc.protocolNamed('NSHapticFeedbackPerformer')
        self.assertArgHasType(TestNSHapticFeedbackHelper.performFeedbackPattern_performanceTime_, 1, objc._C_NSUInteger)

if __name__ == "__main__":
    main()
