import Social
from PyObjCTools.TestSupport import TestCase

SLRequestHandler = b"v@@@"


class TestSLRequest(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Social.SLRequestMethod)
        self.assertEqual(Social.SLRequestMethodGET, 0)
        self.assertEqual(Social.SLRequestMethodPOST, 1)
        self.assertEqual(Social.SLRequestMethodDELETE, 2)
        self.assertEqual(Social.SLRequestMethodPUT, 3)

    def test_methods(self):
        self.assertArgIsBlock(
            Social.SLRequest.performRequestWithHandler_, 0, SLRequestHandler
        )
