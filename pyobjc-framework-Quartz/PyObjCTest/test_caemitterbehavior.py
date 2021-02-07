from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCAEmitterBehavior(TestCase):
    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.CAEmitterBehavior.isEnabled)
        self.assertArgIsBOOL(Quartz.CAAnimation.setEnabled_, 0)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(Quartz.kCAEmitterBehaviorWave, str)
        self.assertIsInstance(Quartz.kCAEmitterBehaviorDrag, str)
        self.assertIsInstance(Quartz.kCAEmitterBehaviorAlignToMotion, str)
        self.assertIsInstance(Quartz.kCAEmitterBehaviorValueOverLife, str)
        self.assertIsInstance(Quartz.kCAEmitterBehaviorColorOverLife, str)
        self.assertIsInstance(Quartz.kCAEmitterBehaviorLight, str)
        self.assertIsInstance(Quartz.kCAEmitterBehaviorAttractor, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(Quartz.kCAEmitterBehaviorSimpleAttractor, str)
