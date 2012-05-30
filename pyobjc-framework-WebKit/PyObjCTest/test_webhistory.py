
from PyObjCTools.TestSupport import *
from WebKit import *

try:
    unicode
except NameError:
    unicode = str

class TestWebHistory (TestCase):
    def testConstants(self):
        self.assertIsInstance(WebHistoryItemsAddedNotification, unicode)
        self.assertIsInstance(WebHistoryItemsRemovedNotification, unicode)
        self.assertIsInstance(WebHistoryAllItemsRemovedNotification, unicode)
        self.assertIsInstance(WebHistoryLoadedNotification, unicode)
        self.assertIsInstance(WebHistorySavedNotification, unicode)
        self.assertIsInstance(WebHistoryItemsKey, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(WebHistory.loadFromURL_error_)
        self.assertArgIsOut(WebHistory.loadFromURL_error_, 1)
        self.assertResultIsBOOL(WebHistory.saveToURL_error_)
        self.assertArgIsOut(WebHistory.saveToURL_error_, 1)


if __name__ == "__main__":
    main()
