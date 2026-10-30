from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCIColor(TestCase):
    def test_methods(self):
        self.assertResultIsVariableSize(Quartz.CIColor.components)
