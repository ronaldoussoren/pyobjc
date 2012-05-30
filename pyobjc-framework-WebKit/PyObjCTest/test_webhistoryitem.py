
from PyObjCTools.TestSupport import *
from WebKit import *

try:
    unicode
except NameError:
    unicode = str

class TestWebHistoryItem (TestCase):
    def testConstants(self):
        self.assertIsInstance(WebHistoryItemChangedNotification, unicode)

if __name__ == "__main__":
    main()
