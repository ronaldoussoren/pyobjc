
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebHistory (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(WebHistoryItemsAddedNotification, unicode)
        self.failUnlessIsInstance(WebHistoryItemsRemovedNotification, unicode)
        self.failUnlessIsInstance(WebHistoryAllItemsRemovedNotification, unicode)
        self.failUnlessIsInstance(WebHistoryLoadedNotification, unicode)
        self.failUnlessIsInstance(WebHistorySavedNotification, unicode)
        self.failUnlessIsInstance(WebHistoryItemsKey, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(WebHistory.loadFromURL_error_)
        self.failUnlessArgIsOut(WebHistory.loadFromURL_error_, 1)
        self.failUnlessResultIsBOOL(WebHistory.saveToURL_error_)
        self.failUnlessArgIsOut(WebHistory.saveToURL_error_, 1)


if __name__ == "__main__":
    main()
