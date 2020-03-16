from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMImplementation(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMImplementation.hasFeature_version_)
        self.assertResultIsBOOL(WebKit.DOMImplementation.hasFeature__)
