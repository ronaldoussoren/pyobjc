import ImageCaptureCore
from PyObjCTools.TestSupport import TestCase


class TestICDeviceBrowserHelper(ImageCaptureCore.NSObject):
    def deviceBrowser_didAddDevice_moreComing_(self, b, d, m):
        pass

    def deviceBrowser_didRemoveDevice_moreGoing_(self, b, d, m):
        pass


class TestICDeviceBrowser(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(ImageCaptureCore.ICAuthorizationStatus, str)

    def testProtocolObjects(self):
        self.assertProtocolExists("ICDeviceBrowserDelegate")

    def testMethods(self):
        self.assertArgIsBOOL(
            TestICDeviceBrowserHelper.deviceBrowser_didAddDevice_moreComing_, 2
        )
        self.assertArgIsBOOL(
            TestICDeviceBrowserHelper.deviceBrowser_didRemoveDevice_moreGoing_, 2
        )

        self.assertResultIsBOOL(ImageCaptureCore.ICDeviceBrowser.isBrowsing)
