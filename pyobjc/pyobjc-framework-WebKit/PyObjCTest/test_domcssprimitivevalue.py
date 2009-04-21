
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMCSSPrimitiveValue (TestCase):
    def testConstants(self):
        self.failUnlessEqual(DOM_CSS_UNKNOWN, 0)
        self.failUnlessEqual(DOM_CSS_NUMBER, 1)
        self.failUnlessEqual(DOM_CSS_PERCENTAGE, 2)
        self.failUnlessEqual(DOM_CSS_EMS, 3)
        self.failUnlessEqual(DOM_CSS_EXS, 4)
        self.failUnlessEqual(DOM_CSS_PX, 5)
        self.failUnlessEqual(DOM_CSS_CM, 6)
        self.failUnlessEqual(DOM_CSS_MM, 7)
        self.failUnlessEqual(DOM_CSS_IN, 8)
        self.failUnlessEqual(DOM_CSS_PT, 9)
        self.failUnlessEqual(DOM_CSS_PC, 10)
        self.failUnlessEqual(DOM_CSS_DEG, 11)
        self.failUnlessEqual(DOM_CSS_RAD, 12)
        self.failUnlessEqual(DOM_CSS_GRAD, 13)
        self.failUnlessEqual(DOM_CSS_MS, 14)
        self.failUnlessEqual(DOM_CSS_S, 15)
        self.failUnlessEqual(DOM_CSS_HZ, 16)
        self.failUnlessEqual(DOM_CSS_KHZ, 17)
        self.failUnlessEqual(DOM_CSS_DIMENSION, 18)
        self.failUnlessEqual(DOM_CSS_STRING, 19)
        self.failUnlessEqual(DOM_CSS_URI, 20)
        self.failUnlessEqual(DOM_CSS_IDENT, 21)
        self.failUnlessEqual(DOM_CSS_ATTR, 22)
        self.failUnlessEqual(DOM_CSS_COUNTER, 23)
        self.failUnlessEqual(DOM_CSS_RECT, 24)
        self.failUnlessEqual(DOM_CSS_RGBCOLOR, 25)


if __name__ == "__main__":
    main()
