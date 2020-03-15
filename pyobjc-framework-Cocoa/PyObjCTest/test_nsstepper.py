import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSStepper(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSStepper.valueWraps)
        self.assertArgIsBOOL(AppKit.NSStepper.setValueWraps_, 0)
        self.assertResultIsBOOL(AppKit.NSStepper.autorepeat)
        self.assertArgIsBOOL(AppKit.NSStepper.setAutorepeat_, 0)
