from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebHistoryItem(TestCase):
    def testConstants(self):
        self.assertIsInstance(WebKit.WebHistoryItemChangedNotification, str)
