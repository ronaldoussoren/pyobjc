from PyObjCTools.TestSupport import *
from AppKit import *


class TestNSTextInputContext (TestCase):
    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultIsBOOL(NSTextInputContext.acceptsGlyphInfo)
        self.assertArgIsBOOL(NSTextInputContext.setAcceptsGlyphInfo_, 0)
        self.assertResultIsBOOL(NSTextInputContext.handleEvent_)

    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(NSTextInputContextKeyboardSelectionDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
