from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCIVector(TestCase):
    def testMethods(self):
        self.assertArgIsIn(Quartz.CIVector.vectorWithValues_count_, 0)
        self.assertArgSizeInArg(Quartz.CIVector.vectorWithValues_count_, 0, 1)
        self.assertArgIsIn(Quartz.CIVector.initWithValues_count_, 0)
        self.assertArgSizeInArg(Quartz.CIVector.initWithValues_count_, 0, 1)
