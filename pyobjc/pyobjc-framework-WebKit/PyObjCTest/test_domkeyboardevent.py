
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMKeyboardEvent (TestCase):
    def testConstants(self):
        self.failUnlessEqual(DOM_KEY_LOCATION_STANDARD, 0)
        self.failUnlessEqual(DOM_KEY_LOCATION_LEFT, 1)
        self.failUnlessEqual(DOM_KEY_LOCATION_RIGHT, 2)
        self.failUnlessEqual(DOM_KEY_LOCATION_NUMPAD, 3)

    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMKeyboardEvent.ctrlKey)
        self.failUnlessResultIsBOOL(DOMKeyboardEvent.shiftKey)
        self.failUnlessResultIsBOOL(DOMKeyboardEvent.altKey)
        self.failUnlessResultIsBOOL(DOMKeyboardEvent.metaKey)
        self.failUnlessResultIsBOOL(DOMKeyboardEvent.getModifierState_)


if __name__ == "__main__":
    main()
