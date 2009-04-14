
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCAAnimationHelper (NSObject):
    def animationDidStop_finished_(self, a, f): pass

class TestCAAnimation (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(CAAnimation.shouldArchiveValueForKey_)
        self.failUnlessResultIsBOOL(CAAnimation.isRemovedOnCompletion)
        self.failUnlessArgIsBOOL(CAAnimation.setRemovedOnCompletion_, 0)

        self.failUnlessArgIsBOOL(TestCAAnimationHelper.animationDidStop_finished_, 1)

        self.failUnlessResultIsBOOL(CAPropertyAnimation.isAdditive)
        self.failUnlessArgIsBOOL(CAPropertyAnimation.setAdditive_, 0)

        self.failUnlessResultIsBOOL(CAPropertyAnimation.isCumulative)
        self.failUnlessArgIsBOOL(CAPropertyAnimation.setCumulative_, 0)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(kCAAnimationLinear, unicode)
        self.failUnlessIsInstance(kCAAnimationDiscrete, unicode)
        self.failUnlessIsInstance(kCAAnimationPaced, unicode)

        self.failUnlessIsInstance(kCATransitionFade, unicode)
        self.failUnlessIsInstance(kCATransitionMoveIn, unicode)
        self.failUnlessIsInstance(kCATransitionPush, unicode)
        self.failUnlessIsInstance(kCATransitionReveal, unicode)
        self.failUnlessIsInstance(kCATransitionFromRight, unicode)
        self.failUnlessIsInstance(kCATransitionFromLeft, unicode)
        self.failUnlessIsInstance(kCATransitionFromTop, unicode)
        self.failUnlessIsInstance(kCATransitionFromBottom, unicode)

    def testConstants(self):
        self.failUnlessIsInstance(kCAAnimationRotateAuto, unicode)
        self.failUnlessIsInstance(kCAAnimationRotateAutoReverse, unicode)



if __name__ == "__main__":
    main()
