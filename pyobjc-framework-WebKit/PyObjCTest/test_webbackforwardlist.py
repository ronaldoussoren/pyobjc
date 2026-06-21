from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebBackForwardList(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.WebBackForwardList.containsItem_)
