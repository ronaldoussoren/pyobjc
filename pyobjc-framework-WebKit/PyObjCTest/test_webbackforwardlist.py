from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebBackForwardList(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.WebBackForwardList.containsItem_)
