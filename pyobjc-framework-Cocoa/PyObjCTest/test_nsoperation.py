import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSOperation(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSOperationQueuePriority)

    def testConstants(self):
        self.assertEqual(Foundation.NSOperationQueuePriorityVeryLow, -8)
        self.assertEqual(Foundation.NSOperationQueuePriorityLow, -4)
        self.assertEqual(Foundation.NSOperationQueuePriorityNormal, 0)
        self.assertEqual(Foundation.NSOperationQueuePriorityHigh, 4)
        self.assertEqual(Foundation.NSOperationQueuePriorityVeryHigh, 8)

        self.assertIsInstance(Foundation.NSInvocationOperationVoidResultException, str)
        self.assertIsInstance(Foundation.NSInvocationOperationCancelledException, str)
        self.assertEqual(
            Foundation.NSOperationQueueDefaultMaxConcurrentOperationCount, -1
        )

        self.assertEqual(
            Foundation.NSOperationQualityOfServiceUserInteractive,
            Foundation.NSQualityOfServiceUserInteractive,
        )
        self.assertEqual(
            Foundation.NSOperationQualityOfServiceUserInitiated,
            Foundation.NSQualityOfServiceUserInitiated,
        )
        self.assertEqual(
            Foundation.NSOperationQualityOfServiceUtility,
            Foundation.NSQualityOfServiceUtility,
        )
        self.assertEqual(
            Foundation.NSOperationQualityOfServiceBackground,
            Foundation.NSQualityOfServiceBackground,
        )

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSOperation.isCancelled)
        self.assertResultIsBOOL(Foundation.NSOperation.isExecuting)
        self.assertResultIsBOOL(Foundation.NSOperation.isFinished)
        self.assertResultIsBOOL(Foundation.NSOperation.isConcurrent)
        self.assertResultIsBOOL(Foundation.NSOperation.isReady)

        self.assertResultIsBOOL(Foundation.NSOperationQueue.isSuspended)
        self.assertArgIsBOOL(Foundation.NSOperationQueue.setSuspended_, 0)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBlock(Foundation.NSOperation.completionBlock, b"v")
        self.assertArgIsBlock(Foundation.NSOperation.setCompletionBlock_, 0, b"v")

        self.assertArgIsBlock(
            Foundation.NSBlockOperation.blockOperationWithBlock_, 0, b"v"
        )
        self.assertArgIsBlock(Foundation.NSBlockOperation.addExecutionBlock_, 0, b"v")

        self.assertArgIsBOOL(
            Foundation.NSOperationQueue.addOperations_waitUntilFinished_, 1
        )
        self.assertArgIsBlock(
            Foundation.NSOperationQueue.addOperationWithBlock_, 0, b"v"
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(Foundation.NSOperation.isAsynchronous)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(Foundation.NSOperationQueue.addBarrierBlock_, 0, b"v")
