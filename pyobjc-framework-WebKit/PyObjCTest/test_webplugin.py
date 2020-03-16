from PyObjCTools.TestSupport import TestCase
import WebKit  # noqa: F401


class TestWebPluginHelper(WebKit.NSObject):
    def webPlugInSetIsSelected_(self, v):
        pass


class TestWebPlugin(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(TestWebPluginHelper.webPlugInSetIsSelected_, 0)
