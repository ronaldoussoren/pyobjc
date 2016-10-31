from PyObjCTools.TestSupport import *

import AppKit

class TestNSSharingServicePickerTouchBarItem (TestCase):
    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSSharingServicePickerTouchBarItem.isEnabled)
        self.assertArgIsBOOL(AppKit.NSSharingServicePickerTouchBarItem.setEnabled_, 0)

    @min_sdk_level('10.12')
    def testProtocols10_12(self):
        objc.protocolNamed('NSSharingServicePickerTouchBarItemDelegate')

if __name__ == "__main__":
    main()
