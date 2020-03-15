import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSStepperCell(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSStepperCell.valueWraps)
        self.assertArgIsBOOL(AppKit.NSStepperCell.setValueWraps_, 0)
        self.assertResultIsBOOL(AppKit.NSStepperCell.autorepeat)
        self.assertArgIsBOOL(AppKit.NSStepperCell.setAutorepeat_, 0)
