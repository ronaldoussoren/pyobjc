from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class QCPlugInHelper(Quartz.QCPlugIn):
    def createViewController(self):
        return 1


class TestQCPlugInViewController(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsRetained(Quartz.QCPlugIn.createViewController)
        self.assertResultIsRetained(Quartz.QCPlugInHelper.createViewController)
