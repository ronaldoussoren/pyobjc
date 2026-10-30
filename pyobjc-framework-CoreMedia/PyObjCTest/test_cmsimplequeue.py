import CoreMedia
from PyObjCTools.TestSupport import TestCase


class TestCMSimpleQueue(TestCase):
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

        self.assertArgHasType(CoreMedia.CMSimpleQueueEnqueue, 1, b"@")

        CoreMedia.CMSimpleQueueDequeue
        CoreMedia.CMSimpleQueueGetHead
        CoreMedia.CMSimpleQueueReset
        CoreMedia.CMSimpleQueueGetCapacity
        CoreMedia.CMSimpleQueueGetCount

        err, q = CoreMedia.CMSimpleQueueCreate(None, 4, None)
        self.assertEqual(err, 0)
        self.assertIsNot(q, None)

        self.assertIsInstance(CoreMedia.CMSimpleQueueGetFullness(q), float)
        self.assertEqual(CoreMedia.CMSimpleQueueGetFullness(q), 0.0)

        r = CoreMedia.CMSimpleQueueEnqueue(q, 42)
        self.assertEqual(r, 0)

        self.assertEqual(CoreMedia.CMSimpleQueueGetCount(q), 1)
        self.assertEqual(CoreMedia.CMSimpleQueueGetFullness(q), 0.25)

        r = CoreMedia.CMSimpleQueueDequeue(q)
        self.assertEqual(r, 42)

        self.assertEqual(CoreMedia.CMSimpleQueueGetCount(q), 0)
        self.assertEqual(CoreMedia.CMSimpleQueueGetFullness(q), 0.0)
