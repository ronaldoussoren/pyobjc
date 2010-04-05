
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebPolicyDelegate (TestCase):
    def testConstants(self):
        self.assertIsInstance(WebActionNavigationTypeKey, unicode)
        self.assertIsInstance(WebActionElementKey, unicode)
        self.assertIsInstance(WebActionButtonKey, unicode)
        self.assertIsInstance(WebActionModifierFlagsKey, unicode)
        self.assertIsInstance(WebActionOriginalURLKey, unicode)


if __name__ == "__main__":
    main()
