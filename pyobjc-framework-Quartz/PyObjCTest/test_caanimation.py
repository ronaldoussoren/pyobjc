from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import Quartz
import objc


class TestCAAnimationHelper(Quartz.NSObject):
    def animationDidStop_finished_(self, a, f):
        pass


class TestCAAnimation(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.CAAnimation.shouldArchiveValueForKey_)
        self.assertResultIsBOOL(Quartz.CAAnimation.isRemovedOnCompletion)
        self.assertArgIsBOOL(Quartz.CAAnimation.setRemovedOnCompletion_, 0)

        self.assertArgIsBOOL(TestCAAnimationHelper.animationDidStop_finished_, 1)

        self.assertResultIsBOOL(Quartz.CAPropertyAnimation.isAdditive)
        self.assertArgIsBOOL(Quartz.CAPropertyAnimation.setAdditive_, 0)

        self.assertResultIsBOOL(Quartz.CAPropertyAnimation.isCumulative)
        self.assertArgIsBOOL(Quartz.CAPropertyAnimation.setCumulative_, 0)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(Quartz.kCAAnimationLinear, str)
        self.assertIsInstance(Quartz.kCAAnimationDiscrete, str)
        self.assertIsInstance(Quartz.kCAAnimationPaced, str)

        self.assertIsInstance(Quartz.kCATransitionFade, str)
        self.assertIsInstance(Quartz.kCATransitionMoveIn, str)
        self.assertIsInstance(Quartz.kCATransitionPush, str)
        self.assertIsInstance(Quartz.kCATransitionReveal, str)
        self.assertIsInstance(Quartz.kCATransitionFromRight, str)
        self.assertIsInstance(Quartz.kCATransitionFromLeft, str)
        self.assertIsInstance(Quartz.kCATransitionFromTop, str)
        self.assertIsInstance(Quartz.kCATransitionFromBottom, str)

        self.assertIsInstance(Quartz.kCAAnimationRotateAuto, str)
        self.assertIsInstance(Quartz.kCAAnimationRotateAutoReverse, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(Quartz.kCAAnimationCubic, str)
        self.assertIsInstance(Quartz.kCAAnimationCubicPaced, str)

    @min_sdk_level("10.12")
    def testProtocols(self):
        objc.protocolNamed("CAAnimationDelegate")
