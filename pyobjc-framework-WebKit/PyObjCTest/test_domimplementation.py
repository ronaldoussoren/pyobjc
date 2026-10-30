from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMImplementation(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMImplementation.hasFeature_version_)
        self.assertResultIsBOOL(WebKit.DOMImplementation.hasFeature__)
