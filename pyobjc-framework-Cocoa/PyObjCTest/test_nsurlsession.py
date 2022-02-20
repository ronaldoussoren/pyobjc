import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc

try:
    Foundation.NSURLSessionStreamTask

except AttributeError:
    pass

else:

    class TestNSURLSessionStreamTaskHelper(Foundation.NSURLSessionStreamTask):
        def readDataOfMinLength_maxLength_timeout_completionHandler_(
            self, mn, mx, t, c
        ):
            pass

        def writeData_timeout_completionHandler_(self, d, t, c):
            pass


try:
    Foundation.NSURLSessionConfiguration

except NameError:
    pass

else:

    class TestNSURLSessionConfigurationHelper(Foundation.NSURLSessionConfiguration):
        def shouldUseExtendedBackgroundIdleMode(self):
            return 1

        def setShouldUseExtendedBackgroundIdleMode_(self, v):
            pass

        def isDiscretionary(self):
            return 1

        def setDiscretionary_(self, v):
            pass

        def HTTPShouldUsePipelining(self):
            return 1

        def setHTTPShouldUsePipelining_(self, v):
            pass

        def HTTPShouldSetCookies(self):
            return 1

        def setHTTPShouldSetCookies_(self, v):
            pass

        def waitsForConnectivity(self):
            return 1

        def setWaitsForConnectivity_(self, v):
            pass


class TestNSURLSessionHelper(Foundation.NSObject):
    def URLSession_didReceiveChallenge_completionHandler_(self, a, b, c):
        pass

    def URLSession_task_willPerformHTTPRedirection_newRequest_completionHandler_(
        self, a, b, c, d, e
    ):
        pass

    def URLSession_task_didReceiveChallenge_completionHandler_(self, a, b, c, d):
        pass

    def URLSession_task_needNewBodyStream_(self, a, b, c):
        pass

    def URLSession_task_didSendBodyData_totalBytesSent_totalBytesExpectedToSend_(
        self, a, b, c, d, e
    ):
        pass

    def URLSession_dataTask_didReceiveResponse_completionHandler_(self, a, b, c, d):
        pass

    def URLSession_dataTask_willCacheResponse_completionHandler_(self, a, b, c, d):
        pass

    def URLSession_downloadTask_didWriteData_totalBytesWritten_totalBytesExpectedToWrite_(
        self, a, b, c, d, e
    ):
        pass

    def URLSession_downloadTask_didResumeAtOffset_expectedTotalBytes_(self, a, b, c, d):
        pass

    def URLSession_task_willBeginDelayedRequest_completionHandler_(self, a, b, c, d):
        pass


class TestNSURLSessionWebSocketDelegateHelper(Foundation.NSObject):
    def URLSession_webSocketTask_didCloseWithCode_reason_(self, a, b, c, d):
        pass


class TestNSURLSession(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSURLSessionAuthChallengeDisposition)
        self.assertIsEnumType(Foundation.NSURLSessionDelayedRequestDisposition)
        self.assertIsEnumType(Foundation.NSURLSessionMultipathServiceType)
        self.assertIsEnumType(Foundation.NSURLSessionResponseDisposition)
        self.assertIsEnumType(
            Foundation.NSURLSessionTaskMetricsDomainResolutionProtocol
        )
        self.assertIsEnumType(Foundation.NSURLSessionTaskMetricsResourceFetchType)
        self.assertIsEnumType(Foundation.NSURLSessionTaskState)
        self.assertIsEnumType(Foundation.NSURLSessionWebSocketCloseCode)
        self.assertIsEnumType(Foundation.NSURLSessionWebSocketMessageType)

    def testConstants(self):
        self.assertEqual(Foundation.NSURLSessionMultipathServiceTypeNone, 0)
        self.assertEqual(Foundation.NSURLSessionMultipathServiceTypeHandover, 1)
        self.assertEqual(Foundation.NSURLSessionMultipathServiceTypeInteractive, 2)
        self.assertEqual(Foundation.NSURLSessionMultipathServiceTypeAggregate, 3)

        self.assertEqual(Foundation.NSURLSessionDelayedRequestContinueLoading, 0)
        self.assertEqual(Foundation.NSURLSessionDelayedRequestUseNewRequest, 1)
        self.assertEqual(Foundation.NSURLSessionDelayedRequestCancel, 2)

        self.assertEqual(Foundation.NSURLSessionWebSocketMessageTypeData, 0)
        self.assertEqual(Foundation.NSURLSessionWebSocketMessageTypeString, 1)

        self.assertEqual(Foundation.NSURLSessionWebSocketCloseCodeInvalid, 0)
        self.assertEqual(Foundation.NSURLSessionWebSocketCloseCodeNormalClosure, 1000)
        self.assertEqual(Foundation.NSURLSessionWebSocketCloseCodeGoingAway, 1001)
        self.assertEqual(Foundation.NSURLSessionWebSocketCloseCodeProtocolError, 1002)
        self.assertEqual(Foundation.NSURLSessionWebSocketCloseCodeUnsupportedData, 1003)
        self.assertEqual(
            Foundation.NSURLSessionWebSocketCloseCodeNoStatusReceived, 1005
        )
        self.assertEqual(Foundation.NSURLSessionWebSocketCloseCodeAbnormalClosure, 1006)
        self.assertEqual(
            Foundation.NSURLSessionWebSocketCloseCodeInvalidFramePayloadData, 1007
        )
        self.assertEqual(Foundation.NSURLSessionWebSocketCloseCodePolicyViolation, 1008)
        self.assertEqual(Foundation.NSURLSessionWebSocketCloseCodeMessageTooBig, 1009)
        self.assertEqual(
            Foundation.NSURLSessionWebSocketCloseCodeMandatoryExtensionMissing, 1010
        )
        self.assertEqual(
            Foundation.NSURLSessionWebSocketCloseCodeInternalServerError, 1011
        )
        self.assertEqual(
            Foundation.NSURLSessionWebSocketCloseCodeTLSHandshakeFailure, 1015
        )

        self.assertEqual(
            Foundation.NSURLSessionTaskMetricsDomainResolutionProtocolUnknown, 0
        )
        self.assertEqual(
            Foundation.NSURLSessionTaskMetricsDomainResolutionProtocolUDP, 1
        )
        self.assertEqual(
            Foundation.NSURLSessionTaskMetricsDomainResolutionProtocolTCP, 2
        )
        self.assertEqual(
            Foundation.NSURLSessionTaskMetricsDomainResolutionProtocolTLS, 3
        )
        self.assertEqual(
            Foundation.NSURLSessionTaskMetricsDomainResolutionProtocolHTTPS, 4
        )

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(Foundation.NSURLSessionTransferSizeUnknown, int)

        self.assertEqual(Foundation.NSURLSessionTaskStateRunning, 0)
        self.assertEqual(Foundation.NSURLSessionTaskStateSuspended, 1)
        self.assertEqual(Foundation.NSURLSessionTaskStateCanceling, 2)
        self.assertEqual(Foundation.NSURLSessionTaskStateCompleted, 3)

        self.assertIsInstance(Foundation.NSURLSessionTaskPriorityDefault, float)
        self.assertIsInstance(Foundation.NSURLSessionTaskPriorityLow, float)
        self.assertIsInstance(Foundation.NSURLSessionTaskPriorityHigh, float)

        self.assertEqual(Foundation.NSURLSessionAuthChallengeUseCredential, 0)
        self.assertEqual(Foundation.NSURLSessionAuthChallengePerformDefaultHandling, 1)
        self.assertEqual(
            Foundation.NSURLSessionAuthChallengeCancelAuthenticationChallenge, 2
        )
        self.assertEqual(Foundation.NSURLSessionAuthChallengeRejectProtectionSpace, 3)

        self.assertEqual(Foundation.NSURLSessionResponseCancel, 0)
        self.assertEqual(Foundation.NSURLSessionResponseAllow, 1)
        self.assertEqual(Foundation.NSURLSessionResponseBecomeDownload, 2)
        self.assertEqual(Foundation.NSURLSessionResponseBecomeStream, 3)

        self.assertIsInstance(Foundation.NSURLSessionDownloadTaskResumeData, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertEqual(Foundation.NSURLSessionTaskMetricsResourceFetchTypeUnknown, 0)
        self.assertEqual(
            Foundation.NSURLSessionTaskMetricsResourceFetchTypeNetworkLoad, 1
        )
        self.assertEqual(
            Foundation.NSURLSessionTaskMetricsResourceFetchTypeServerPush, 2
        )
        self.assertEqual(
            Foundation.NSURLSessionTaskMetricsResourceFetchTypeLocalCache, 3
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            Foundation.NSURLSession.resetWithCompletionHandler_, 0, b"v"
        )
        self.assertArgIsBlock(
            Foundation.NSURLSession.flushWithCompletionHandler_, 0, b"v"
        )
        self.assertArgIsBlock(
            Foundation.NSURLSession.getTasksWithCompletionHandler_, 0, b"v@@@"
        )

        self.assertArgIsBlock(
            Foundation.NSURLSession.dataTaskWithRequest_completionHandler_, 1, b"v@@@"
        )
        self.assertArgIsBlock(
            Foundation.NSURLSession.dataTaskWithURL_completionHandler_, 1, b"v@@@"
        )
        self.assertArgIsBlock(
            Foundation.NSURLSession.uploadTaskWithRequest_fromFile_completionHandler_,
            2,
            b"v@@@",
        )
        self.assertArgIsBlock(
            Foundation.NSURLSession.uploadTaskWithRequest_fromData_completionHandler_,
            2,
            b"v@@@",
        )
        self.assertArgIsBlock(
            Foundation.NSURLSession.downloadTaskWithURL_completionHandler_, 1, b"v@@@"
        )
        self.assertArgIsBlock(
            Foundation.NSURLSession.downloadTaskWithResumeData_completionHandler_,
            1,
            b"v@@@",
        )

        self.assertArgIsBlock(
            Foundation.NSURLSessionDownloadTask.cancelByProducingResumeData_, 0, b"v@"
        )

        self.assertResultIsBOOL(
            TestNSURLSessionConfigurationHelper.waitsForConnectivity
        )
        self.assertArgIsBOOL(
            TestNSURLSessionConfigurationHelper.setWaitsForConnectivity_, 0
        )

        self.assertResultIsBOOL(TestNSURLSessionConfigurationHelper.isDiscretionary)
        self.assertArgIsBOOL(TestNSURLSessionConfigurationHelper.setDiscretionary_, 0)

        self.assertResultIsBOOL(
            TestNSURLSessionConfigurationHelper.HTTPShouldUsePipelining
        )
        self.assertArgIsBOOL(
            TestNSURLSessionConfigurationHelper.setHTTPShouldUsePipelining_, 0
        )

        self.assertResultIsBOOL(
            TestNSURLSessionConfigurationHelper.HTTPShouldSetCookies
        )
        self.assertArgIsBOOL(
            TestNSURLSessionConfigurationHelper.setHTTPShouldSetCookies_, 0
        )

        self.assertArgIsBlock(
            TestNSURLSessionHelper.URLSession_didReceiveChallenge_completionHandler_,
            2,
            b"v" + objc._C_NSUInteger + b"@",
        )
        self.assertArgIsBlock(
            TestNSURLSessionHelper.URLSession_task_willPerformHTTPRedirection_newRequest_completionHandler_,  # noqa: B950
            4,
            b"v@",
        )
        self.assertArgIsBlock(
            TestNSURLSessionHelper.URLSession_task_didReceiveChallenge_completionHandler_,
            3,
            b"v" + objc._C_NSUInteger + b"@",
        )
        self.assertArgIsBlock(
            TestNSURLSessionHelper.URLSession_task_needNewBodyStream_, 2, b"v@"
        )

        self.assertArgHasType(
            TestNSURLSessionHelper.URLSession_task_didSendBodyData_totalBytesSent_totalBytesExpectedToSend_,  # noqa: B950
            2,
            objc._C_LNG_LNG,
        )
        self.assertArgHasType(
            TestNSURLSessionHelper.URLSession_task_didSendBodyData_totalBytesSent_totalBytesExpectedToSend_,  # noqa: B950
            3,
            objc._C_LNG_LNG,
        )
        self.assertArgHasType(
            TestNSURLSessionHelper.URLSession_task_didSendBodyData_totalBytesSent_totalBytesExpectedToSend_,  # noqa: B950
            4,
            objc._C_LNG_LNG,
        )

        self.assertArgIsBlock(
            TestNSURLSessionHelper.URLSession_dataTask_didReceiveResponse_completionHandler_,
            3,
            b"v" + objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestNSURLSessionHelper.URLSession_dataTask_willCacheResponse_completionHandler_,
            3,
            b"v@",
        )
        self.assertArgIsBlock(
            TestNSURLSessionHelper.URLSession_dataTask_willCacheResponse_completionHandler_,
            3,
            b"v@",
        )

        self.assertArgHasType(
            TestNSURLSessionHelper.URLSession_downloadTask_didWriteData_totalBytesWritten_totalBytesExpectedToWrite_,  # noqa: B950
            2,
            objc._C_LNG_LNG,
        )
        self.assertArgHasType(
            TestNSURLSessionHelper.URLSession_downloadTask_didWriteData_totalBytesWritten_totalBytesExpectedToWrite_,  # noqa: B950
            3,
            objc._C_LNG_LNG,
        )
        self.assertArgHasType(
            TestNSURLSessionHelper.URLSession_downloadTask_didWriteData_totalBytesWritten_totalBytesExpectedToWrite_,  # noqa: B950
            4,
            objc._C_LNG_LNG,
        )

        self.assertArgHasType(
            TestNSURLSessionHelper.URLSession_downloadTask_didResumeAtOffset_expectedTotalBytes_,  # noqa: B950
            2,
            objc._C_LNG_LNG,
        )
        self.assertArgHasType(
            TestNSURLSessionHelper.URLSession_downloadTask_didResumeAtOffset_expectedTotalBytes_,  # noqa: B950
            3,
            objc._C_LNG_LNG,
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsBlock(
            Foundation.NSURLSession.getAllTasksWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            TestNSURLSessionStreamTaskHelper.readDataOfMinLength_maxLength_timeout_completionHandler_,  # noqa: B950
            3,
            b"v@Z@",
        )
        self.assertArgIsBlock(
            TestNSURLSessionStreamTaskHelper.writeData_timeout_completionHandler_,
            2,
            b"v@",
        )

        self.assertResultIsBOOL(
            TestNSURLSessionConfigurationHelper.shouldUseExtendedBackgroundIdleMode
        )
        self.assertArgIsBOOL(
            TestNSURLSessionConfigurationHelper.setShouldUseExtendedBackgroundIdleMode_,
            0,
        )

    @min_os_level("10.15")
    def testMethods10_12(self):
        self.assertResultIsBOOL(
            Foundation.NSURLSessionTaskTransactionMetrics.isProxyConnection
        )
        self.assertResultIsBOOL(
            Foundation.NSURLSessionTaskTransactionMetrics.isReusedConnection
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            TestNSURLSessionHelper.URLSession_task_willBeginDelayedRequest_completionHandler_,
            3,
            b"v" + objc._C_NSInteger + b"@",
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            Foundation.NSURLSessionWebSocketTask.sendMessage_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            Foundation.NSURLSessionWebSocketTask.receiveMessageWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            Foundation.NSURLSessionWebSocketTask.sendPingWithPongReceiveHandler_,
            0,
            b"v@",
        )

        self.assertResultIsBOOL(
            Foundation.NSURLSessionTaskTransactionMetrics.isCellular
        )
        self.assertResultIsBOOL(
            Foundation.NSURLSessionTaskTransactionMetrics.isExpensive
        )
        self.assertResultIsBOOL(
            Foundation.NSURLSessionTaskTransactionMetrics.isConstrained
        )
        self.assertResultIsBOOL(
            Foundation.NSURLSessionTaskTransactionMetrics.isMultipath
        )

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(
            Foundation.NSURLSessionConfiguration.sessionSendsLaunchEvents
        )
        self.assertArgIsBOOL(
            Foundation.NSURLSessionConfiguration.setSessionSendsLaunchEvents_, 0
        )

    @min_sdk_level("10.12")
    def testProtocols10_12(self):
        objc.protocolNamed("NSURLSessionTaskDelegate")
        objc.protocolNamed("NSURLSessionDataDelegate")
        objc.protocolNamed("NSURLSessionDownloadDelegate")

    @min_sdk_level("10.11")
    def testProtocols10_11(self):
        objc.protocolNamed("NSURLSessionStreamDelegate")

    def test_protocol_methods10_15(self):
        self.assertArgHasType(
            TestNSURLSessionWebSocketDelegateHelper.URLSession_webSocketTask_didCloseWithCode_reason_,  # noqa: B950
            2,
            objc._C_NSInteger,
        )
