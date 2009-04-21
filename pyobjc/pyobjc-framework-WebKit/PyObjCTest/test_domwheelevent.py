
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMWheelEvent (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMWheelEvent.ctrlKey)
        self.failUnlessResultIsBOOL(DOMWheelEvent.shiftKey)
        self.failUnlessResultIsBOOL(DOMWheelEvent.altKey)
        self.failUnlessResultIsBOOL(DOMWheelEvent.metaKey)
        self.failUnlessResultIsBOOL(DOMWheelEvent.isHorizontal)

if __name__ == "__main__":
    main()
