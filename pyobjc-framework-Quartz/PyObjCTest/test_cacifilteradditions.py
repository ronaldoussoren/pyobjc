from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCACIFilterAdditions(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.CIFilter.isEnabled)
        self.assertArgIsBOOL(Quartz.CIFilter.setEnabled_, 0)
