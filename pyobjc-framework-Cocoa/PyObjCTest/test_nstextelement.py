import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTextElement(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(AppKit.NSTextElement.isRepresentedElement)
