
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebHistoryItem (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(WebHistoryItemChangedNotification, unicode)

if __name__ == "__main__":
    main()
