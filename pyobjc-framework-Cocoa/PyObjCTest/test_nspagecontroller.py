from PyObjCTools.TestSupport import *
import AppKit

class TestNSPageController (TestCase):
    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(AppKit.NSPageControllerTransitionStyleStackHistory, 0)
        self.assertEqual(AppKit.NSPageControllerTransitionStyleStackBook, 1)
        self.assertEqual(AppKit.NSPageControllerTransitionStyleHorizontalStrip, 2)

if __name__ == "__main__":
    main()
