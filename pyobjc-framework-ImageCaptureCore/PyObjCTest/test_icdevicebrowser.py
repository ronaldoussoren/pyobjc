from PyObjCTools.TestSupport import *

from ImageCaptureCore import *

class TestICDeviceBrowserHelper (NSObject):
    def deviceBrowser_didAddDevice_moreComing_(self, b, d, m): pass
    def deviceBrowser_didRemoveDevice_moreGoing_(self, b, d, m): pass

class TestICDeviceBrowser (TestCase):
    def testProtocolObjects(self):
        objc.protocolNamed('ICDeviceBrowserDelegate')

    def testMethods(self):
        self.assertArgIsBOOL(TestICDeviceBrowserHelper.deviceBrowser_didAddDevice_moreComing_, 2)
        self.assertArgIsBOOL(TestICDeviceBrowserHelper.deviceBrowser_didRemoveDevice_moreGoing_, 2)

        self.assertResultIsBOOL(ICDeviceBrowser.isBrowsing)


if __name__ == "__main__":
    main()
