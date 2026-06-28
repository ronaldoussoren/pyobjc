from PyObjCTools.TestSupport import TestCase


import Social


class TestSLTypes(TestCase):
    def test_constants(self):
        self.assertIsInstance(Social.SLServiceTypeTwitter, str)
        self.assertIsInstance(Social.SLServiceTypeFacebook, str)
        self.assertIsInstance(Social.SLServiceTypeSinaWeibo, str)

        self.assertIsInstance(Social.SLServiceTypeTencentWeibo, str)
        self.assertIsInstance(Social.SLServiceTypeLinkedIn, str)
