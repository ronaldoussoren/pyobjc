from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCIColor(TestCase):
    def testMethods(self):
        self.assertResultIsVariableSize(Quartz.CIColor.components)
