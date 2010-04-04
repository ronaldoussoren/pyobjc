
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSResponder (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSResponder.tryToPerform_with_)
        self.assertResultIsBOOL(NSResponder.performKeyEquivalent_)
        self.assertResultIsBOOL(NSResponder.acceptsFirstResponder)
        self.assertResultIsBOOL(NSResponder.becomeFirstResponder)
        self.assertResultIsBOOL(NSResponder.resignFirstResponder)
        self.assertResultIsBOOL(NSResponder.shouldBeTreatedAsInkEvent_)
        self.assertResultIsBOOL(NSResponder.performMnemonic_)
        self.assertArgIsSEL(NSResponder.doCommandBySelector_, 0, b'v@:@')

        self.assertArgIsSEL(NSResponder.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_, 3, b'v@:' + objc._C_NSBOOL + b'^v')
        self.assertArgHasType(NSResponder.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_, 4, b'^v')
        self.assertResultIsBOOL(NSResponder.presentError_)


if __name__ == "__main__":
    main()
