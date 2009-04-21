
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMTreeWalker (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMTreeWalker.expandEntityReferences)

if __name__ == "__main__":
    main()
