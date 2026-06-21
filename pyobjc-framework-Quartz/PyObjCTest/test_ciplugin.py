from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCIPlugIn(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(Quartz.CIPlugIn.loadPlugIn_allowNonExecutable_, 1)

    @min_os_level("10.7")
    def test_methods10_7(self):
        self.assertArgIsBOOL(Quartz.CIPlugIn.loadPlugIn_allowExecutableCode_, 1)
