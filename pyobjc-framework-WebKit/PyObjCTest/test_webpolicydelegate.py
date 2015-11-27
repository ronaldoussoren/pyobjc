
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebPolicyDelegate (TestCase):
    def testConstants(self):
        self.assertIsInstance(WebActionNavigationTypeKey, unicode)
        self.assertIsInstance(WebActionElementKey, unicode)
        self.assertIsInstance(WebActionButtonKey, unicode)
        self.assertIsInstance(WebActionModifierFlagsKey, unicode)
        self.assertIsInstance(WebActionOriginalURLKey, unicode)

        self.assertEqual(WebNavigationTypeLinkClicked, 0)
        self.assertEqual(WebNavigationTypeFormSubmitted, 1)
        self.assertEqual(WebNavigationTypeBackForward, 2)
        self.assertEqual(WebNavigationTypeReload, 3)
        self.assertEqual(WebNavigationTypeFormResubmitted, 4)
        self.assertEqual(WebNavigationTypeOther, 5)

    def testProtocols(self):
        self.assertIsInstance(objc.protocolNamed("WebPolicyDecisionListener"), objc.formal_protocol)

    @min_sdk_level('10.11')
    def testProtocols10_11(self):
        self.assertIsInstance(objc.protocolNamed("WebPolicyDelegate"), objc.formal_protocol)


if __name__ == "__main__":
    main()
