
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMNodeIterator (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMNodeIterator.expandEntityReferences)

        self.assertResultIsBOOL(DOMNodeIterator.pointerBeforeReferenceNode)

if __name__ == "__main__":
    main()
