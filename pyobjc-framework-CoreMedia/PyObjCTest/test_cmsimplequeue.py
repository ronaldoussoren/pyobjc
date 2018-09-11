from PyObjCTools.TestSupport import *

import CoreMedia

class TestCMSimpleQueue (TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMSimpleQueueError_AllocationFailed, -12770)
        self.assertEqual(CoreMedia.kCMSimpleQueueError_RequiredParameterMissing, -12771)
        self.assertEqual(CoreMedia.kCMSimpleQueueError_ParameterOutOfRange, -12772)
        self.assertEqual(CoreMedia.kCMSimpleQueueError_QueueIsFull, -12773)

    def test_types(self):
        self.assertIsCFType(CoreMedia.CMSimpleQueueRef)

    def test_functions(self):
        CoreMedia.CMSimpleQueueGetTypeID

        self.assertArgIsOut(CoreMedia.CMSimpleQueueCreate, 2)
        self.assertArgIsCFRetained(CoreMedia.CMSimpleQueueCreate, 2)

        self.assertArgHasType(CoreMedia.CMSimpleQueueEnqueue, 1, b'@')

        CoreMedia.CMSimpleQueueDequeue
        CoreMedia.CMSimpleQueueGetHead
        CoreMedia.CMSimpleQueueReset
        CoreMedia.CMSimpleQueueGetCapacity
        CoreMedia.CMSimpleQueueGetCount

        CoreMedia.CMSimpleQueueGetFullness






if __name__ == "__main__":
    main()
