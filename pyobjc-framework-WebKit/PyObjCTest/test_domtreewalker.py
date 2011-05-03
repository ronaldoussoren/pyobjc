
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMTreeWalker (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMTreeWalker.expandEntityReferences)

if __name__ == "__main__":
    main()
