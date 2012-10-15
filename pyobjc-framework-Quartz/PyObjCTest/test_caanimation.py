
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

try:
    unicode
except NameError:
    unicode = str

class TestCAAnimationHelper (NSObject):
    def animationDidStop_finished_(self, a, f): pass

class TestCAAnimation (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(CAAnimation.shouldArchiveValueForKey_)
        self.assertResultIsBOOL(CAAnimation.isRemovedOnCompletion)
        self.assertArgIsBOOL(CAAnimation.setRemovedOnCompletion_, 0)

        self.assertArgIsBOOL(TestCAAnimationHelper.animationDidStop_finished_, 1)

        self.assertResultIsBOOL(CAPropertyAnimation.isAdditive)
        self.assertArgIsBOOL(CAPropertyAnimation.setAdditive_, 0)

        self.assertResultIsBOOL(CAPropertyAnimation.isCumulative)
        self.assertArgIsBOOL(CAPropertyAnimation.setCumulative_, 0)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCAAnimationLinear, unicode)
        self.assertIsInstance(kCAAnimationDiscrete, unicode)
        self.assertIsInstance(kCAAnimationPaced, unicode)

        self.assertIsInstance(kCATransitionFade, unicode)
        self.assertIsInstance(kCATransitionMoveIn, unicode)
        self.assertIsInstance(kCATransitionPush, unicode)
        self.assertIsInstance(kCATransitionReveal, unicode)
        self.assertIsInstance(kCATransitionFromRight, unicode)
        self.assertIsInstance(kCATransitionFromLeft, unicode)
        self.assertIsInstance(kCATransitionFromTop, unicode)
        self.assertIsInstance(kCATransitionFromBottom, unicode)

        self.assertIsInstance(kCAAnimationRotateAuto, unicode)
        self.assertIsInstance(kCAAnimationRotateAutoReverse, unicode)

    @min_os_level('10.7')
    def testConstants10_5(self):
        self.assertIsInstance(kCAAnimationCubic, unicode)
        self.assertIsInstance(kCAAnimationCubicPaced, unicode)


if __name__ == "__main__":
    main()
