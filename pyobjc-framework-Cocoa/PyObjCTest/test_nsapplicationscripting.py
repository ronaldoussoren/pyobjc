from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSApplicationScriptingHelper (NSObject):
    def application_delegateHandlesKey_(self, app, key):
        return 1


class TestNSApplicationScripting (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(TestNSApplicationScriptingHelper.application_delegateHandlesKey_)

if __name__ == "__main__":
    main()
