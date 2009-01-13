from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSOperation (TestCase):
    def testConstants(self):
        self.assertEquals(NSOperationQueuePriorityVeryLow, -8)
        self.assertEquals(NSOperationQueuePriorityLow, -4)
        self.assertEquals(NSOperationQueuePriorityNormal, 0)
        self.assertEquals(NSOperationQueuePriorityHigh, 4)
        self.assertEquals(NSOperationQueuePriorityVeryHigh, 8)

        self.failUnless(isinstance(NSInvocationOperationVoidResultException, unicode))
        self.failUnless(isinstance(NSInvocationOperationCancelledException, unicode))

        self.assertEquals(NSOperationQueueDefaultMaxConcurrentOperationCount, -1)

if __name__ == "__main__":
    main()
