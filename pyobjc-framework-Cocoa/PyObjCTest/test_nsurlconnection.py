import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSURLConnectionHelper(Foundation.NSObject):
    def connection_canAuthenticateAgainstProtectionSpace_(self, a, b):
        return 1

    def connectionShouldUseCredentialStorage_(self, a):
        return 1

    def connection_didSendBodyData_totalBytesWritten_totalBytesExpectedToWrite_(
        self, a, b, c, d
    ):
        return 1

    def connection_didWriteData_totalBytesWritten_expectedTotalBytes_(self, a, b, c, d):
        return 1

    def connectionDidResumeDownloading_totalBytesWritten_expectedTotalBytes_(
        self, a, b, c
    ):
        return 1


class TestNSURLConnection(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSURLConnection.canHandleRequest_)

        self.assertArgIsBOOL(
            Foundation.NSURLConnection.initWithRequest_delegate_startImmediately_, 2
        )

        self.assertArgIsOut(
            Foundation.NSURLConnection.sendSynchronousRequest_returningResponse_error_,
            1,
        )
        self.assertArgIsOut(
            Foundation.NSURLConnection.sendSynchronousRequest_returningResponse_error_,
            2,
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(
            TestNSURLConnectionHelper.connection_canAuthenticateAgainstProtectionSpace_
        )
        self.assertResultIsBOOL(
            TestNSURLConnectionHelper.connectionShouldUseCredentialStorage_
        )
        self.assertArgHasType(
            TestNSURLConnectionHelper.connection_didSendBodyData_totalBytesWritten_totalBytesExpectedToWrite_,  # noqa: B950
            1,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSURLConnectionHelper.connection_didSendBodyData_totalBytesWritten_totalBytesExpectedToWrite_,  # noqa: B950
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSURLConnectionHelper.connection_didSendBodyData_totalBytesWritten_totalBytesExpectedToWrite_,  # noqa: B950
            3,
            objc._C_NSInteger,
        )

        self.assertArgHasType(
            TestNSURLConnectionHelper.connection_didWriteData_totalBytesWritten_expectedTotalBytes_,  # noqa: B950
            1,
            objc._C_LNG_LNG,
        )
        self.assertArgHasType(
            TestNSURLConnectionHelper.connection_didWriteData_totalBytesWritten_expectedTotalBytes_,  # noqa: B950
            2,
            objc._C_LNG_LNG,
        )
        self.assertArgHasType(
            TestNSURLConnectionHelper.connection_didWriteData_totalBytesWritten_expectedTotalBytes_,  # noqa: B950
            3,
            objc._C_LNG_LNG,
        )

        self.assertArgHasType(
            TestNSURLConnectionHelper.connectionDidResumeDownloading_totalBytesWritten_expectedTotalBytes_,  # noqa: B950
            1,
            objc._C_LNG_LNG,
        )
        self.assertArgHasType(
            TestNSURLConnectionHelper.connectionDidResumeDownloading_totalBytesWritten_expectedTotalBytes_,  # noqa: B950
            2,
            objc._C_LNG_LNG,
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBlock(
            Foundation.NSURLConnection.sendAsynchronousRequest_queue_completionHandler_,
            2,
            b"v@@",
        )

    @min_sdk_level("10.7")
    def testProtocolObjects(self):
        self.assertProtocolExists("NSURLConnectionDelegate")

    @min_sdk_level("10.10")
    def testProtocolObjects10_10(self):
        self.assertProtocolExists("NSURLConnectionDataDelegate")
        self.assertProtocolExists("NSURLConnectionDownloadDelegate")
