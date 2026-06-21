from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebHistoryItem(TestCase):
    def test_constants(self):
        self.assertIsInstance(WebKit.WebHistoryItemChangedNotification, str)
