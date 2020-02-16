from PyObjCTools.TestSupport import *
import WebKit


class TestWKFindResult(TestCase):
    @min_os_level('10.15.4')
    def test_methods10_15_4(self):
        self.assertResultIsBOOL(WebKit.WKFindResult.matchFound)

if __name__ == "__main__":
    main()
