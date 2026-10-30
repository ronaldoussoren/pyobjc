from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCIPlugIn(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(Quartz.CIPlugIn.loadPlugIn_allowNonExecutable_, 1)

        self.assertArgIsBOOL(Quartz.CIPlugIn.loadPlugIn_allowExecutableCode_, 1)
