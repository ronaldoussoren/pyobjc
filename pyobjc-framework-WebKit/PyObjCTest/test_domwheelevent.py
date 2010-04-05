
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMWheelEvent (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMWheelEvent.ctrlKey)
        self.assertResultIsBOOL(DOMWheelEvent.shiftKey)
        self.assertResultIsBOOL(DOMWheelEvent.altKey)
        self.assertResultIsBOOL(DOMWheelEvent.metaKey)
        self.assertResultIsBOOL(DOMWheelEvent.isHorizontal)

if __name__ == "__main__":
    main()
