import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSForm(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(AppKit.NSForm.setBordered_, 0)
        self.assertArgIsBOOL(AppKit.NSForm.setBezeled_, 0)
