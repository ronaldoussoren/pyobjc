from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSOperation (TestCase):
    def testConstants(self):
        self.assertEqual(NSOperationQueuePriorityVeryLow, -8)
        self.assertEqual(NSOperationQueuePriorityLow, -4)
        self.assertEqual(NSOperationQueuePriorityNormal, 0)
        self.assertEqual(NSOperationQueuePriorityHigh, 4)
        self.assertEqual(NSOperationQueuePriorityVeryHigh, 8)

        self.assertIsInstance(NSInvocationOperationVoidResultException, unicode)
        self.assertIsInstance(NSInvocationOperationCancelledException, unicode)
        self.assertEqual(NSOperationQueueDefaultMaxConcurrentOperationCount, -1)

    def testMethods(self):
        self.assertResultIsBOOL(NSOperation.isCancelled)
        self.assertResultIsBOOL(NSOperation.isExecuting)
        self.assertResultIsBOOL(NSOperation.isFinished)
        self.assertResultIsBOOL(NSOperation.isConcurrent)
        self.assertResultIsBOOL(NSOperation.isReady)

        self.assertResultIsBOOL(NSOperationQueue.isSuspended)
        self.assertArgIsBOOL(NSOperationQueue.setSuspended_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBlock(NSOperation.completionBlock, b'v')
        self.assertArgIsBlock(NSOperation.setCompletionBlock_, 0, b'v')

        self.assertArgIsBlock(NSBlockOperation.blockOperationWithBlock_, 0, b'v')
        self.assertArgIsBlock(NSBlockOperation.addExecutionBlock_, 0, b'v')

        self.assertArgIsBOOL(NSOperationQueue.addOperations_waitUntilFinished_, 1)
        self.assertArgIsBlock(NSOperationQueue.addOperationWithBlock_, 0, b'v')

if __name__ == "__main__":
    main()
