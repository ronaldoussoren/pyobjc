from PyObjCTools.TestSupport import *

from Foundation import *

try:
    NSURLSessionStreamTask

except NameError:
    pass

else:
    class TestNSURLSessionStreamTaskHelper (NSURLSessionStreamTask):
        def readDataOfMinLength_maxLength_timeout_completionHandler_(self, mn, mx, t, c): pass
        def writeData_timeout_completionHandler_(self, d, t, c): pass

try:
    NSURLSessionConfiguration

except NameError:
    pass

else:
    class TestNSURLSessionConfigurationHelper (NSURLSessionConfiguration):
        def shouldUseExtendedBackgroundIdleMode(self): return 1
        def setShouldUseExtendedBackgroundIdleMode_(self, v): pass
        def isDiscretionary(self): return 1
        def setDiscretionary_(self, v): pass
        def HTTPShouldUsePipelining(self): return 1
        def setHTTPShouldUsePipelining_(self, v): pass
        def HTTPShouldSetCookies(self): return 1
        def setHTTPShouldSetCookies_(self, v): pass
        def waitsForConnectivity(self): return 1
        def setWaitsForConnectivity_(self, v): pass

class TestNSURLSessionHelper (NSObject):
    def URLSession_didReceiveChallenge_completionHandler_(self, a, b, c): pass
    def URLSession_task_willPerformHTTPRedirection_newRequest_completionHandler_(self, a, b, c, d, e): pass
    def URLSession_task_didReceiveChallenge_completionHandler_(self, a, b, c, d): pass
    def URLSession_task_needNewBodyStream_(self, a, b, c): pass
    def URLSession_task_didSendBodyData_totalBytesSent_totalBytesExpectedToSend_(self, a, b, c, d, e): pass
    def URLSession_dataTask_didReceiveResponse_completionHandler_(self, a, b, c, d): pass
    def URLSession_dataTask_willCacheResponse_completionHandler_(self, a, b, c, d): pass
    def URLSession_downloadTask_didWriteData_totalBytesWritten_totalBytesExpectedToWrite_(self, a, b, c, d, e): pass
    def URLSession_downloadTask_didResumeAtOffset_expectedTotalBytes_(self, a, b, c, d): pass
    def URLSession_task_willBeginDelayedRequest_completionHandler_(self, a, b, c, d): pass

class TestNSURLSession (TestCase):
    def testConstants(self):
        self.assertEqual(NSURLSessionMultipathServiceTypeNone, 0)
        self.assertEqual(NSURLSessionMultipathServiceTypeHandover, 1)
        self.assertEqual(NSURLSessionMultipathServiceTypeInteractive, 2)
        self.assertEqual(NSURLSessionMultipathServiceTypeAggregate, 3)

        self.assertEqual(NSURLSessionDelayedRequestContinueLoading, 0)
        self.assertEqual(NSURLSessionDelayedRequestUseNewRequest, 1)
        self.assertEqual(NSURLSessionDelayedRequestCancel, 2)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(NSURLSessionTransferSizeUnknown, (int, long))

        self.assertEqual(NSURLSessionTaskStateRunning, 0)
        self.assertEqual(NSURLSessionTaskStateSuspended, 1)
        self.assertEqual(NSURLSessionTaskStateCanceling, 2)
        self.assertEqual(NSURLSessionTaskStateCompleted, 3)

        self.assertIsInstance(NSURLSessionTaskPriorityDefault, float)
        self.assertIsInstance(NSURLSessionTaskPriorityLow, float)
        self.assertIsInstance(NSURLSessionTaskPriorityHigh, float)

        self.assertEqual(NSURLSessionAuthChallengeUseCredential, 0)
        self.assertEqual(NSURLSessionAuthChallengePerformDefaultHandling, 1)
        self.assertEqual(NSURLSessionAuthChallengeCancelAuthenticationChallenge, 2)
        self.assertEqual(NSURLSessionAuthChallengeRejectProtectionSpace, 3)

        self.assertEqual(NSURLSessionResponseCancel, 0)
        self.assertEqual(NSURLSessionResponseAllow, 1)
        self.assertEqual(NSURLSessionResponseBecomeDownload, 2)
        self.assertEqual(NSURLSessionResponseBecomeStream, 3)

        self.assertIsInstance(NSURLSessionDownloadTaskResumeData, unicode)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertEqual(NSURLSessionTaskMetricsResourceFetchTypeUnknown, 0)
        self.assertEqual(NSURLSessionTaskMetricsResourceFetchTypeNetworkLoad, 1)
        self.assertEqual(NSURLSessionTaskMetricsResourceFetchTypeServerPush, 2)
        self.assertEqual(NSURLSessionTaskMetricsResourceFetchTypeLocalCache, 3)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsBlock(NSURLSession.resetWithCompletionHandler_, 0, b'v')
        self.assertArgIsBlock(NSURLSession.flushWithCompletionHandler_, 0, b'v')
        self.assertArgIsBlock(NSURLSession.getTasksWithCompletionHandler_, 0, b'v@@@')

        self.assertArgIsBlock(NSURLSession.dataTaskWithRequest_completionHandler_, 1, b'v@@@')
        self.assertArgIsBlock(NSURLSession.dataTaskWithURL_completionHandler_, 1, b'v@@@')
        self.assertArgIsBlock(NSURLSession.uploadTaskWithRequest_fromFile_completionHandler_, 2, b'v@@@')
        self.assertArgIsBlock(NSURLSession.uploadTaskWithRequest_fromData_completionHandler_, 2, b'v@@@')
        self.assertArgIsBlock(NSURLSession.downloadTaskWithURL_completionHandler_, 1, b'v@@@')
        self.assertArgIsBlock(NSURLSession.downloadTaskWithResumeData_completionHandler_, 1, b'v@@@')

        self.assertArgIsBlock(NSURLSessionDownloadTask.cancelByProducingResumeData_, 0, b'v@')

        self.assertResultIsBOOL(TestNSURLSessionConfigurationHelper.waitsForConnectivity)
        self.assertArgIsBOOL(TestNSURLSessionConfigurationHelper.setWaitsForConnectivity_, 0)

        self.assertResultIsBOOL(TestNSURLSessionConfigurationHelper.isDiscretionary)
        self.assertArgIsBOOL(TestNSURLSessionConfigurationHelper.setDiscretionary_, 0)

        self.assertResultIsBOOL(TestNSURLSessionConfigurationHelper.HTTPShouldUsePipelining)
        self.assertArgIsBOOL(TestNSURLSessionConfigurationHelper.setHTTPShouldUsePipelining_, 0)

        self.assertResultIsBOOL(TestNSURLSessionConfigurationHelper.HTTPShouldSetCookies)
        self.assertArgIsBOOL(TestNSURLSessionConfigurationHelper.setHTTPShouldSetCookies_, 0)

        self.assertArgIsBlock(TestNSURLSessionHelper.URLSession_didReceiveChallenge_completionHandler_, 2, b'v' + objc._C_NSUInteger + b'@')
        self.assertArgIsBlock(TestNSURLSessionHelper.URLSession_task_willPerformHTTPRedirection_newRequest_completionHandler_, 4, b'v@')
        self.assertArgIsBlock(TestNSURLSessionHelper.URLSession_task_didReceiveChallenge_completionHandler_, 3, b'v' + objc._C_NSUInteger + b'@')
        self.assertArgIsBlock(TestNSURLSessionHelper.URLSession_task_needNewBodyStream_, 2, b'v@')

        self.assertArgHasType(TestNSURLSessionHelper.URLSession_task_didSendBodyData_totalBytesSent_totalBytesExpectedToSend_, 2, objc._C_LNG_LNG)
        self.assertArgHasType(TestNSURLSessionHelper.URLSession_task_didSendBodyData_totalBytesSent_totalBytesExpectedToSend_, 3, objc._C_LNG_LNG)
        self.assertArgHasType(TestNSURLSessionHelper.URLSession_task_didSendBodyData_totalBytesSent_totalBytesExpectedToSend_, 4, objc._C_LNG_LNG)

        self.assertArgIsBlock(TestNSURLSessionHelper.URLSession_dataTask_didReceiveResponse_completionHandler_, 3, b'v' + objc._C_NSUInteger)
        self.assertArgIsBlock(TestNSURLSessionHelper.URLSession_dataTask_willCacheResponse_completionHandler_, 3, b'v@')
        self.assertArgIsBlock(TestNSURLSessionHelper.URLSession_dataTask_willCacheResponse_completionHandler_, 3, b'v@')

        self.assertArgHasType(TestNSURLSessionHelper.URLSession_downloadTask_didWriteData_totalBytesWritten_totalBytesExpectedToWrite_, 2, objc._C_LNG_LNG)
        self.assertArgHasType(TestNSURLSessionHelper.URLSession_downloadTask_didWriteData_totalBytesWritten_totalBytesExpectedToWrite_, 3, objc._C_LNG_LNG)
        self.assertArgHasType(TestNSURLSessionHelper.URLSession_downloadTask_didWriteData_totalBytesWritten_totalBytesExpectedToWrite_, 4, objc._C_LNG_LNG)

        self.assertArgHasType(TestNSURLSessionHelper.URLSession_downloadTask_didResumeAtOffset_expectedTotalBytes_, 2, objc._C_LNG_LNG)
        self.assertArgHasType(TestNSURLSessionHelper.URLSession_downloadTask_didResumeAtOffset_expectedTotalBytes_, 3, objc._C_LNG_LNG)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertArgIsBlock(NSURLSession.getAllTasksWithCompletionHandler_, 0, b'v@')
        self.assertArgIsBlock(TestNSURLSessionStreamTaskHelper.readDataOfMinLength_maxLength_timeout_completionHandler_, 3, b'v@Z@')
        self.assertArgIsBlock(TestNSURLSessionStreamTaskHelper.writeData_timeout_completionHandler_, 2, b'v@')

        self.assertResultIsBOOL(TestNSURLSessionConfigurationHelper.shouldUseExtendedBackgroundIdleMode)
        self.assertArgIsBOOL(TestNSURLSessionConfigurationHelper.setShouldUseExtendedBackgroundIdleMode_, 0)

    @expectedFailure # For some reason these aren't present on 10.12 after all.
    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSURLSessionTaskTransactionMetrics.isProxyConnection)
        self.assertResultIsBOOL(NSURLSessionTaskTransactionMetrics.isReusedConnection)


    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertArgIsBlock(TestNSURLSessionHelper.URLSession_task_willBeginDelayedRequest_completionHandler_, 3, b'v' + objc._C_NSInteger + b'@')

    @min_sdk_level('10.12')
    def testProtocols10_12(self):
        objc.protocolNamed('NSURLSessionTaskDelegate')
        objc.protocolNamed('NSURLSessionDataDelegate')
        objc.protocolNamed('NSURLSessionDownloadDelegate')

    @min_sdk_level('10.11')
    def testProtocols10_11(self):
        objc.protocolNamed('NSURLSessionStreamDelegate')

if __name__ == "__main__":
    main()
