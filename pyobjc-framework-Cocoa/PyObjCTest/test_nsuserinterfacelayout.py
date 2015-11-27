from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSUserInterfaceLayout (TestCase):
    def testConstants(self):
        self.assertEqual(NSUserInterfaceLayoutDirectionLeftToRight, 0)
        self.assertEqual(NSUserInterfaceLayoutDirectionRightToLeft, 1)
        self.assertEqual(NSUserInterfaceLayoutOrientationHorizontal, 0)
        self.assertEqual(NSUserInterfaceLayoutOrientationVertical, 1)

if __name__ == "__main__":
    main()
