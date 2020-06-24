import sys

from PyObjCTools.TestSupport import TestCase, min_os_level

if sys.maxsize >= 2 ** 32:

    import Social

    class TestSLTypes(TestCase):
        @min_os_level("10.8")
        def testConstants(self):
            self.assertIsInstance(Social.SLServiceTypeTwitter, str)
            self.assertIsInstance(Social.SLServiceTypeFacebook, str)
            self.assertIsInstance(Social.SLServiceTypeSinaWeibo, str)

        @min_os_level("10.9")
        def testConstants10_9(self):
            self.assertIsInstance(Social.SLServiceTypeTencentWeibo, str)
            self.assertIsInstance(Social.SLServiceTypeLinkedIn, str)
