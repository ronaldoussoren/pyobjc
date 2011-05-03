
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSAnimationHelper (NSObject):
    def animationShouldStart_(self, animation):
        return 1

class TestNSAnimation (TestCase):
    def testConstants(self):
        self.assertEqual(NSAnimationEaseInOut, 0)
        self.assertEqual(NSAnimationEaseIn, 1)
        self.assertEqual(NSAnimationEaseOut, 2)
        self.assertEqual(NSAnimationLinear, 3)

        self.assertEqual(NSAnimationBlocking, 0)
        self.assertEqual(NSAnimationNonblocking, 1)
        self.assertEqual(NSAnimationNonblockingThreaded, 2)

        self.assertIsInstance(NSAnimationProgressMarkNotification, unicode)
        self.assertIsInstance(NSAnimationProgressMark, unicode)

        self.assertIsInstance(NSViewAnimationTargetKey, unicode)
        self.assertIsInstance(NSViewAnimationStartFrameKey, unicode)
        self.assertIsInstance(NSViewAnimationEndFrameKey, unicode)
        self.assertIsInstance(NSViewAnimationEffectKey, unicode)
        self.assertIsInstance(NSViewAnimationFadeInEffect, unicode)
        self.assertIsInstance(NSViewAnimationFadeOutEffect, unicode)

        self.assertIsInstance(NSAnimationTriggerOrderIn, unicode)
        self.assertIsInstance(NSAnimationTriggerOrderOut, unicode)

    def testProtocol(self):
        self.assertResultIsBOOL(TestNSAnimationHelper.animationShouldStart_)

if __name__ == "__main__":
    main()
