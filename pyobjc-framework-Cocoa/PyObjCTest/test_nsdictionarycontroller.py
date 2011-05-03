from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSDictionaryControllerHelper (NSObject):
    def isExplicitlyIncluded(self): return 1


class TestNSDictionaryController (TestCase):
    def testProtocols(self):
        self.assertResultIsBOOL(TestNSDictionaryControllerHelper.isExplicitlyIncluded)
    

if __name__ == "__main__":
    main()
