
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSAnimation (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSAnimationEaseInOut, 0)
        self.failUnlessEqual(NSAnimationEaseIn, 1)
        self.failUnlessEqual(NSAnimationEaseOut, 2)
        self.failUnlessEqual(NSAnimationLinear, 3)

        self.failUnlessEqual(NSAnimationBlocking, 0)
        self.failUnlessEqual(NSAnimationNonblocking, 1)
        self.failUnlessEqual(NSAnimationNonblockingThreaded, 2)

        self.failUnlessIsInstance(NSAnimationProgressMarkNotification, unicode)
        self.failUnlessIsInstance(NSAnimationProgressMark, unicode)

        self.failUnlessIsInstance(NSViewAnimationTargetKey, unicode)
        self.failUnlessIsInstance(NSViewAnimationStartFrameKey, unicode)
        self.failUnlessIsInstance(NSViewAnimationEndFrameKey, unicode)
        self.failUnlessIsInstance(NSViewAnimationEffectKey, unicode)
        self.failUnlessIsInstance(NSViewAnimationFadeInEffect, unicode)
        self.failUnlessIsInstance(NSViewAnimationFadeOutEffect, unicode)

        self.failUnlessIsInstance(NSAnimationTriggerOrderIn, unicode)
        self.failUnlessIsInstance(NSAnimationTriggerOrderOut, unicode)



if __name__ == "__main__":
    main()
