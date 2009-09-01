from PyObjCTools.TestSupport import *
from AppKit import *


class TestNSTextInputContext (TestCase):
    @min_os_level('10.6')
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSTextInputContext.acceptsGlyphInfo)
        self.failUnlessArgIsBOOL(NSTextInputContext.setAcceptsGlyphInfo_, 0)
        self.failUnlessResultIsBOOL(NSTextInputContext.handleEvent_)

    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(NSTextInputContextKeyboardSelectionDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
