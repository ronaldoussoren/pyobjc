from PyObjCTools.TestSupport import TestCase
import Quartz


class TestQCPlugInViewController(TestCase):
    def test_methods(self):
        self.assertResultIsRetained(Quartz.QCPlugIn.createViewController)
