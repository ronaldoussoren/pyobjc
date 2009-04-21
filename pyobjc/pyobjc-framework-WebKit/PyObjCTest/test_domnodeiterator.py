
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMNodeIterator (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMNodeIterator.expandEntityReferences)

if __name__ == "__main__":
    main()
