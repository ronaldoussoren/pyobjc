
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebBackForwardList (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebBackForwardList.containsItem_)

if __name__ == "__main__":
    main()
