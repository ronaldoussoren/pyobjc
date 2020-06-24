from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKOpenPanelParameters(TestCase):
    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(WebKit.WKOpenPanelParameters.allowsMultipleSelection)

    @min_os_level("10.13.4")
    def testMethods10_13_4(self):
        self.assertResultIsBOOL(WebKit.WKOpenPanelParameters.allowsDirectories)
