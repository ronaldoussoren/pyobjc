from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebHistory(TestCase):
    def testConstants(self):
        self.assertIsInstance(WebKit.WebHistoryItemsAddedNotification, str)
        self.assertIsInstance(WebKit.WebHistoryItemsRemovedNotification, str)
        self.assertIsInstance(WebKit.WebHistoryAllItemsRemovedNotification, str)
        self.assertIsInstance(WebKit.WebHistoryLoadedNotification, str)
        self.assertIsInstance(WebKit.WebHistorySavedNotification, str)
        self.assertIsInstance(WebKit.WebHistoryItemsKey, str)

    def testMethods(self):
        self.assertResultIsBOOL(WebKit.WebHistory.loadFromURL_error_)
        self.assertArgIsOut(WebKit.WebHistory.loadFromURL_error_, 1)
        self.assertResultIsBOOL(WebKit.WebHistory.saveToURL_error_)
        self.assertArgIsOut(WebKit.WebHistory.saveToURL_error_, 1)
