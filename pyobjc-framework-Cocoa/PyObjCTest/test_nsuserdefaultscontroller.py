import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSUserDefaultsController(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSUserDefaultsController.appliesImmediately)
        self.assertArgIsBOOL(AppKit.NSUserDefaultsController.setAppliesImmediately_, 0)
        self.assertResultIsBOOL(AppKit.NSUserDefaultsController.hasUnappliedChanges)
