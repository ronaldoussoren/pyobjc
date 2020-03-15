import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSUserDefaultsController(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSUserDefaultsController.appliesImmediately)
        self.assertArgIsBOOL(AppKit.NSUserDefaultsController.setAppliesImmediately_, 0)
        self.assertResultIsBOOL(AppKit.NSUserDefaultsController.hasUnappliedChanges)
