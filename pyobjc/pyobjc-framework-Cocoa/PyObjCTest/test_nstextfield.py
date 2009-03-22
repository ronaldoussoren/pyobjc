from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSTextField (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSTextField.drawsBackground)
        self.failUnlessArgIsBOOL(NSTextField.setDrawsBackground_, 0)
        self.failUnlessResultIsBOOL(NSTextField.isBordered)
        self.failUnlessArgIsBOOL(NSTextField.setBordered_, 0)
        self.failUnlessResultIsBOOL(NSTextField.isBezeled)
        self.failUnlessArgIsBOOL(NSTextField.setBezeled_, 0)
        self.failUnlessResultIsBOOL(NSTextField.isEditable)
        self.failUnlessArgIsBOOL(NSTextField.setEditable_, 0)
        self.failUnlessResultIsBOOL(NSTextField.isSelectable)
        self.failUnlessArgIsBOOL(NSTextField.setSelectable_, 0)
        self.failUnlessResultIsBOOL(NSTextField.textShouldBeginEditing_)
        self.failUnlessResultIsBOOL(NSTextField.textShouldEndEditing_)
        self.failUnlessResultIsBOOL(NSTextField.acceptsFirstResponder)
        self.failUnlessResultIsBOOL(NSTextField.allowsEditingTextAttributes)
        self.failUnlessArgIsBOOL(NSTextField.setAllowsEditingTextAttributes_, 0)
        self.failUnlessResultIsBOOL(NSTextField.importsGraphics)
        self.failUnlessArgIsBOOL(NSTextField.setImportsGraphics_, 0)

if __name__ == "__main__":
    main()
