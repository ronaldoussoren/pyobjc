import Foundation
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    min_sdk_level,
)


class TestNSURLRequest(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSURLRequestAttribution)
        self.assertIsEnumType(Foundation.NSURLRequestCachePolicy)
        self.assertIsEnumType(Foundation.NSURLRequestNetworkServiceType)

    def testConstants(self):
        self.assertEqual(Foundation.NSURLRequestUseProtocolCachePolicy, 0)
        self.assertEqual(Foundation.NSURLRequestReloadIgnoringLocalCacheData, 1)
        self.assertEqual(Foundation.NSURLRequestReloadIgnoringLocalAndRemoteCacheData, 4)
        self.assertEqual(
            Foundation.NSURLRequestReloadIgnoringCacheData,
            Foundation.NSURLRequestReloadIgnoringLocalCacheData,
        )
        self.assertEqual(Foundation.NSURLRequestReturnCacheDataElseLoad, 2)
        self.assertEqual(Foundation.NSURLRequestReturnCacheDataDontLoad, 3)
        self.assertEqual(Foundation.NSURLRequestReloadRevalidatingCacheData, 5)

        self.assertEqual(Foundation.NSURLNetworkServiceTypeDefault, 0)
        self.assertEqual(Foundation.NSURLNetworkServiceTypeVoIP, 1)
        self.assertEqual(Foundation.NSURLNetworkServiceTypeVideo, 2)
        self.assertEqual(Foundation.NSURLNetworkServiceTypeBackground, 3)
        self.assertEqual(Foundation.NSURLNetworkServiceTypeVoice, 4)
        self.assertEqual(Foundation.NSURLNetworkServiceTypeResponsiveData, 6)
        self.assertEqual(Foundation.NSURLNetworkServiceTypeAVStreaming, 8)
        self.assertEqual(Foundation.NSURLNetworkServiceTypeResponsiveAV, 9)
        self.assertEqual(Foundation.NSURLNetworkServiceTypeCallSignaling, 11)

        self.assertEqual(Foundation.NSURLRequestAttributionDeveloper, 0)
        self.assertEqual(Foundation.NSURLRequestAttributionUser, 1)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSURLRequest.HTTPShouldHandleCookies)
        self.assertArgIsBOOL(
            Foundation.NSMutableURLRequest.setHTTPShouldHandleCookies_, 0
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(Foundation.NSURLRequest.HTTPShouldUsePipelining)
        self.assertArgIsBOOL(
            Foundation.NSMutableURLRequest.setHTTPShouldUsePipelining_, 0
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(Foundation.NSURLRequest.allowsCellularAccess)
        self.assertArgIsBOOL(Foundation.NSMutableURLRequest.setAllowsCellularAccess_, 0)

        self.assertResultIsBOOL(Foundation.NSURLRequest.supportsSecureCoding)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(Foundation.NSURLRequest.allowsExpensiveNetworkAccess)
        self.assertArgIsBOOL(
            Foundation.NSMutableURLRequest.setAllowsExpensiveNetworkAccess_, 0
        )
        self.assertResultIsBOOL(Foundation.NSURLRequest.allowsConstrainedNetworkAccess)
        self.assertArgIsBOOL(
            Foundation.NSMutableURLRequest.setAllowsConstrainedNetworkAccess_, 0
        )

    @min_os_level("11.3")
    def testMethods11_3(self):
        self.assertResultIsBOOL(Foundation.NSURLRequest.assumesHTTP3Capable)
        self.assertArgIsBOOL(Foundation.NSMutableURLRequest.setAssumesHTTP3Capable_, 0)

    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertResultIsBOOL(Foundation.NSURLRequest.requiresDNSSECValidation)
        self.assertArgIsBOOL(
            Foundation.NSMutableURLRequest.setRequiresDNSSECValidation_, 0
        )

    @min_os_level("15.0")
    def testMethods15_0(self):
        self.assertResultIsBOOL(Foundation.NSURLRequest.allowsPersistentDNS)
        self.assertResultIsBOOL(Foundation.NSURLRequest.allowsPersistentDNS)
        self.assertArgIsBOOL(Foundation.NSMutableURLRequest.setAllowsPersistentDNS_, 0)

    @min_sdk_level("10.15")
    def test_protocols(self):
        self.assertProtocolExists("NSURLSessionWebSocketDelegate")
