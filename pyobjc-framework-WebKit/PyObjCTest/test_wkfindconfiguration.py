from PyObjCTools.TestSupport import *
import WebKit


class TestWKFindConfiguration(TestCase):
    @min_os_level('10.15.4')
    def test_methods10_15_4(self):
        self.assertResultIsBOOL(WebKit.WKFindConfiguration.backwards)
        self.assertArgIsBOOL(WebKit.WKFindConfiguration.setBackwards_, 0)

        self.assertResultIsBOOL(WebKit.WKFindConfiguration.caseSensitive)
        self.assertArgIsBOOL(WebKit.WKFindConfiguration.setCaseSensitive_, 0)

        self.assertResultIsBOOL(WebKit.WKFindConfiguration.wraps)
        self.assertArgIsBOOL(WebKit.WKFindConfiguration.setWraps_, 0)


if __name__ == "__main__":
    main()
