
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMCSSPrimitiveValue (TestCase):
    def testConstants(self):
        self.assertEqual(DOM_CSS_UNKNOWN, 0)
        self.assertEqual(DOM_CSS_NUMBER, 1)
        self.assertEqual(DOM_CSS_PERCENTAGE, 2)
        self.assertEqual(DOM_CSS_EMS, 3)
        self.assertEqual(DOM_CSS_EXS, 4)
        self.assertEqual(DOM_CSS_PX, 5)
        self.assertEqual(DOM_CSS_CM, 6)
        self.assertEqual(DOM_CSS_MM, 7)
        self.assertEqual(DOM_CSS_IN, 8)
        self.assertEqual(DOM_CSS_PT, 9)
        self.assertEqual(DOM_CSS_PC, 10)
        self.assertEqual(DOM_CSS_DEG, 11)
        self.assertEqual(DOM_CSS_RAD, 12)
        self.assertEqual(DOM_CSS_GRAD, 13)
        self.assertEqual(DOM_CSS_MS, 14)
        self.assertEqual(DOM_CSS_S, 15)
        self.assertEqual(DOM_CSS_HZ, 16)
        self.assertEqual(DOM_CSS_KHZ, 17)
        self.assertEqual(DOM_CSS_DIMENSION, 18)
        self.assertEqual(DOM_CSS_STRING, 19)
        self.assertEqual(DOM_CSS_URI, 20)
        self.assertEqual(DOM_CSS_IDENT, 21)
        self.assertEqual(DOM_CSS_ATTR, 22)
        self.assertEqual(DOM_CSS_COUNTER, 23)
        self.assertEqual(DOM_CSS_RECT, 24)
        self.assertEqual(DOM_CSS_RGBCOLOR, 25)


if __name__ == "__main__":
    main()
