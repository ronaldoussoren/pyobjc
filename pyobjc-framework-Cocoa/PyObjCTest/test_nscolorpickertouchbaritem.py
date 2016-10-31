from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSColorPickerTouchBarItem (TestCase):
    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSColorPickerTouchBarItem.showsAlpha)
        self.assertArgIsBOOL(NSColorPickerTouchBarItem.setShowsAlpha_, 0)

        self.assertResultIsBOOL(NSColorPickerTouchBarItem.isEnabled)
        self.assertArgIsBOOL(NSColorPickerTouchBarItem.setEnabled_, 0)

if __name__ == "__main__":
    main()
