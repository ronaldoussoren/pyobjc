from PyObjCTools.TestSupport import *
from WebKit import *


class TestWebPagePreferences(TestCase):
    def test_constants(self):
        self.assertEqual(WKContentModeRecommended, 0)
        self.assertEqual(WKContentModeMobile, 1)
        self.assertEqual(WKContentModeDesktop, 2)


if __name__ == "__main__":
    main()
