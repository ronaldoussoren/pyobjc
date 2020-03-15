import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSApplicationScriptingHelper(AppKit.NSObject):
    def application_delegateHandlesKey_(self, app, key):
        return 1


class TestNSApplicationScripting(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(
            TestNSApplicationScriptingHelper.application_delegateHandlesKey_
        )
