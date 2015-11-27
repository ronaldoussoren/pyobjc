from PyObjCTools.TestSupport import *
from WebKit import *


class TestWKNavigationAction (TestCase):
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(WKNavigationTypeLinkActivated, 0)
        self.assertEqual(WKNavigationTypeFormSubmitted, 1)
        self.assertEqual(WKNavigationTypeBackForward, 2)
        self.assertEqual(WKNavigationTypeReload, 3)
        self.assertEqual(WKNavigationTypeFormResubmitted, 4)
        self.assertEqual(WKNavigationTypeOther, -1)

if __name__ == "__main__":
    main()
