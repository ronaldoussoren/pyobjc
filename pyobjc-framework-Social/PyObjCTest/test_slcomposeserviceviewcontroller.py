from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import Social

    class TestSLComposeServiceViewController (TestCase):
        @min_os_level("10.10")
        def testMethods(self):
            self.assertResultIsBOOL(Social.SLComposeServiceViewController.isContentValid)

if __name__ == "__main__":
    main()
