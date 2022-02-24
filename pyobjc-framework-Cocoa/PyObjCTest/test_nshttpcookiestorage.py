import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSHTTPCookieStorage(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSHTTPCookieAcceptPolicy)

    def testConstants(self):
        self.assertEqual(Foundation.NSHTTPCookieAcceptPolicyAlways, 0)
        self.assertEqual(Foundation.NSHTTPCookieAcceptPolicyNever, 1)
        self.assertEqual(
            Foundation.NSHTTPCookieAcceptPolicyOnlyFromMainDocumentDomain, 2
        )

        self.assertIsInstance(
            Foundation.NSHTTPCookieManagerAcceptPolicyChangedNotification, str
        )
        self.assertIsInstance(
            Foundation.NSHTTPCookieManagerCookiesChangedNotification, str
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            Foundation.NSHTTPCookieStorage.getCookiesForTask_completionHandler_,
            1,
            b"v@",
        )
