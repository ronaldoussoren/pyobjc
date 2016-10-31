from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTouchBar (TestCase):
    @min_os_level('10.12')
    def testMethods(self):
        self.assertResultIsBOOL(NSTouchBar.isVisible)
        #self.assertArgIsBOOL(NSTouchBar.setVisible_, 0)

        self.assertResultIsBOOL(NSApplication.isAutomaticCustomizeTouchBarMenuItemEnabled)
        self.assertArgIsBOOL(NSApplication.setAutomaticCustomizeTouchBarMenuItemEnabled_, 0)

    @min_sdk_level('10.12')
    def testProtocolObjects(self):
        objc.protocolNamed('NSTouchBarDelegate')
        objc.protocolNamed('NSTouchBarProvider')

if __name__ == "__main__":
    main()
