from PyObjCTools.TestSupport import *
import Social

class TestSLTypes (TestCase):
    @min_os_level("10.8")
    def testConstants(self):
        self.assertIsInstance(Social.SLServiceTypeTwitter, unicode)
        self.assertIsInstance(Social.SLServiceTypeSinaWeibo, unicode)

if __name__ == "__main__":
    main()
