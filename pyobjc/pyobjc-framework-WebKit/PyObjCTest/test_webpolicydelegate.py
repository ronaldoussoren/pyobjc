
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebPolicyDelegate (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(WebActionNavigationTypeKey, unicode)
        self.failUnlessIsInstance(WebActionElementKey, unicode)
        self.failUnlessIsInstance(WebActionButtonKey, unicode)
        self.failUnlessIsInstance(WebActionModifierFlagsKey, unicode)
        self.failUnlessIsInstance(WebActionOriginalURLKey, unicode)


if __name__ == "__main__":
    main()
