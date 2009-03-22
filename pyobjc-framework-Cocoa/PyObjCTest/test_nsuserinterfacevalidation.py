from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSUserInterfaceValidationHelper (NSObject):
    def action(self): return 1
    def tag(self): return 1

    def validateUserInterfaceItem_(self, a): return 1

class TestNSUserInterfaceValidation (TestCase):
    def testProtocols(self):
        self.failUnlessResultHasType(TestNSUserInterfaceValidationHelper.action, objc._C_SEL)
        self.failUnlessResultHasType(TestNSUserInterfaceValidationHelper.tag, objc._C_NSInteger)
        self.failUnlessResultIsBOOL(TestNSUserInterfaceValidationHelper.validateUserInterfaceItem_)

if __name__ == "__main__":
    main()
