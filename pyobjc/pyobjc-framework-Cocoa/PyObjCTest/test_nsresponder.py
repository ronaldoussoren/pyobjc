
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSResponder (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSResponder.tryToPerform_with_)
        self.failUnlessResultIsBOOL(NSResponder.performKeyEquivalent_)
        self.failUnlessResultIsBOOL(NSResponder.acceptsFirstResponder)
        self.failUnlessResultIsBOOL(NSResponder.becomeFirstResponder)
        self.failUnlessResultIsBOOL(NSResponder.resignFirstResponder)
        self.failUnlessResultIsBOOL(NSResponder.shouldBeTreatedAsInkEvent_)
        self.failUnlessResultIsBOOL(NSResponder.performMnemonic_)
        self.failUnlessArgIsSEL(NSResponder.doCommandBySelector_, 0, 'v@:@')

        self.failUnlessArgIsSEL(NSResponder.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_, 3, 'v@:' + objc._C_NSBOOL + '^v')
        self.failUnlessArgHasType(NSResponder.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_, 4, '^v')
        self.failUnlessResultIsBOOL(NSResponder.presentError_)


if __name__ == "__main__":
    main()
