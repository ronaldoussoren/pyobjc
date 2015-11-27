from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMediaLibraryBrowserController (TestCase):
    def testConstants(self):
        self.assertEqual(NSMediaLibraryAudio, 1 << 0)
        self.assertEqual(NSMediaLibraryImage, 1 << 1)
        self.assertEqual(NSMediaLibraryMovie, 1 << 2)

    @min_os_level('10.9')
    def testMethods(self):
        self.assertResultIsBOOL(NSMediaLibraryBrowserController.isVisible)
        self.assertArgIsBOOL(NSMediaLibraryBrowserController.setVisible_, 0)

if __name__ == "__main__":
    main()
