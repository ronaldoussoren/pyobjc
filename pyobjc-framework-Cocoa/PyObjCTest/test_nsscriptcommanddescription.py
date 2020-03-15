import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSScriptCommandDescriptionHelper(Foundation.NSScriptCommandDescription):
    def isOptionalArgumentWithName_(self, name):
        return 1


class TestNSScriptCommandDescription(TestCase):
    def testMethods(self):
        # This should be tested on the actual Foundation.NSScriptCommandDescription class,
        # but for some reason that class doesn't seem to have the
        # required method (at least not without instantating the class)
        self.assertResultIsBOOL(
            TestNSScriptCommandDescriptionHelper.isOptionalArgumentWithName_
        )
