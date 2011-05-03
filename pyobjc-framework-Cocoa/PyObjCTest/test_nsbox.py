
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSBox (TestCase):
    def testConstants(self):
        self.assertEqual(NSNoTitle, 0)
        self.assertEqual(NSAboveTop, 1)
        self.assertEqual(NSAtTop, 2)
        self.assertEqual(NSBelowTop, 3)
        self.assertEqual(NSAboveBottom, 4)
        self.assertEqual(NSAtBottom, 5)
        self.assertEqual(NSBelowBottom, 6)
        self.assertEqual(NSBoxPrimary, 0)
        self.assertEqual(NSBoxSecondary, 1)
        self.assertEqual(NSBoxSeparator, 2)
        self.assertEqual(NSBoxOldStyle, 3)
        self.assertEqual(NSBoxCustom, 4)

    def testMethods(self):
        self.assertResultIsBOOL(NSBox.isTransparent)
        self.assertArgIsBOOL(NSBox.setTransparent_, 0)


if __name__ == "__main__":
    main()
