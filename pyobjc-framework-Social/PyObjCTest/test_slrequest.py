import Social
from PyObjCTools.TestSupport import TestCase, min_os_level

SLRequestHandler = b"v@@@"


class TestSLRequest(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Social.SLRequestMethod)

    @min_os_level("10.8")
    def testConstants(self):
        self.assertEqual(Social.SLRequestMethodGET, 0)
        self.assertEqual(Social.SLRequestMethodPOST, 1)
        self.assertEqual(Social.SLRequestMethodDELETE, 2)
        self.assertEqual(Social.SLRequestMethodPUT, 3)

    @min_os_level("10.8")
    def testMethods(self):
        self.assertArgIsBlock(
            Social.SLRequest.performRequestWithHandler_, 0, SLRequestHandler
        )
