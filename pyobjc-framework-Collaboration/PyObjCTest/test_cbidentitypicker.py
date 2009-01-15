
from PyObjCTools.TestSupport import *
from Collaboration import *

class TestCBIdentityPicker (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(CBIdentityPicker.setAllowsMultipleSelection_, 0)
        self.failUnlessResultIsBOOL(CBIdentityPicker.allowsMultipleSelection)

        self.failUnlessArgIsSEL(CBIdentityPicker.runModalForWindow_modalDelegate_didEndSelector_contextInfo_, 2, 'v@:@' + objc._C_NSInteger + '^v')
        self.failUnlessArgHasType(CBIdentityPicker.runModalForWindow_modalDelegate_didEndSelector_contextInfo_, 3, '^v')



if __name__ == "__main__":
    main()
