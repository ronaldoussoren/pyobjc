from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCIFilterShape(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(Quartz.CIFilterShape.transformBy_interior_, 1)
