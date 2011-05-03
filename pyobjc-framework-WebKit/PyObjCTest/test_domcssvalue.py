
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMCSSValue (TestCase):
    def testConstants(self):
        self.assertEqual(DOM_CSS_INHERIT, 0)
        self.assertEqual(DOM_CSS_PRIMITIVE_VALUE, 1)
        self.assertEqual(DOM_CSS_VALUE_LIST, 2)
        self.assertEqual(DOM_CSS_CUSTOM, 3)


if __name__ == "__main__":
    main()
