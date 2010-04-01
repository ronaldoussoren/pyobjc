
from PyObjCTools.TestSupport import *
from Collaboration import *

class TestCBIdentityPicker (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(CBIdentityPicker.setAllowsMultipleSelection_, 0)
        self.assertResultIsBOOL(CBIdentityPicker.allowsMultipleSelection)

        self.assertArgIsSEL(CBIdentityPicker.runModalForWindow_modalDelegate_didEndSelector_contextInfo_, 2, b'v@:@' + objc._C_NSInteger + b'^v')
        self.assertArgHasType(CBIdentityPicker.runModalForWindow_modalDelegate_didEndSelector_contextInfo_, 3, b'^v')



if __name__ == "__main__":
    main()
