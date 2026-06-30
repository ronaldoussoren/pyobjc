import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSHTTPCookieStorage(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSHTTPCookieAcceptPolicy)
        self.assertEqual(Foundation.NSHTTPCookieAcceptPolicyAlways, 0)
        self.assertEqual(Foundation.NSHTTPCookieAcceptPolicyNever, 1)
        self.assertEqual(
            Foundation.NSHTTPCookieAcceptPolicyOnlyFromMainDocumentDomain, 2
        )

    def test_constants(self):
        self.assertIsInstance(
            Foundation.NSHTTPCookieManagerAcceptPolicyChangedNotification, str
        )
        self.assertIsInstance(
            Foundation.NSHTTPCookieManagerCookiesChangedNotification, str
        )

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertArgIsBlock(
            Foundation.NSHTTPCookieStorage.getCookiesForTask_completionHandler_,
            1,
            b"v@",
        )
