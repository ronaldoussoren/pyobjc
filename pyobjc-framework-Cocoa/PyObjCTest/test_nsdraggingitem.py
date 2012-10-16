from PyObjCTools.TestSupport import *

import AppKit

try:
    unicode
except NameError:
    unicode = str

class TestNSDraggingItem (TestCase):
    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(AppKit.NSDraggingImageComponentIconKey, unicode)
        self.assertIsInstance(AppKit.NSDraggingImageComponentLabelKey, unicode)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsBlock(AppKit.NSDraggingItem.setImageComponentsProvider_, 0, b'@')
        self.assertResultIsBlock(AppKit.NSDraggingItem.imageComponentsProvider, b'@')

if __name__ == "__main__":
    main()
