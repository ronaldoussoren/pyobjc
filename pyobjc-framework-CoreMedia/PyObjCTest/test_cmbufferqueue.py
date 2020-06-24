import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestCMBufferQueue(TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMBufferQueueError_AllocationFailed, -12760)
        self.assertEqual(CoreMedia.kCMBufferQueueError_RequiredParameterMissing, -12761)
        self.assertEqual(
            CoreMedia.kCMBufferQueueError_InvalidCMBufferCallbacksStruct, -12762
        )
        self.assertEqual(CoreMedia.kCMBufferQueueError_EnqueueAfterEndOfData, -12763)
        self.assertEqual(CoreMedia.kCMBufferQueueError_QueueIsFull, -12764)
        self.assertEqual(CoreMedia.kCMBufferQueueError_BadTriggerDuration, -12765)
        self.assertEqual(
            CoreMedia.kCMBufferQueueError_CannotModifyQueueFromTriggerCallback, -12766
        )
        self.assertEqual(CoreMedia.kCMBufferQueueError_InvalidTriggerCondition, -12767)
        self.assertEqual(CoreMedia.kCMBufferQueueError_InvalidTriggerToken, -12768)
        self.assertEqual(CoreMedia.kCMBufferQueueError_InvalidBuffer, -12769)

        self.assertEqual(CoreMedia.kCMBufferQueueTrigger_WhenDurationBecomesLessThan, 1)
        self.assertEqual(
            CoreMedia.kCMBufferQueueTrigger_WhenDurationBecomesLessThanOrEqualTo, 2
        )
        self.assertEqual(
            CoreMedia.kCMBufferQueueTrigger_WhenDurationBecomesGreaterThan, 3
        )
        self.assertEqual(
            CoreMedia.kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualTo, 4
        )
        self.assertEqual(
            CoreMedia.kCMBufferQueueTrigger_WhenMinPresentationTimeStampChanges, 5
        )
        self.assertEqual(
            CoreMedia.kCMBufferQueueTrigger_WhenMaxPresentationTimeStampChanges, 6
        )
        self.assertEqual(CoreMedia.kCMBufferQueueTrigger_WhenDataBecomesReady, 7)
        self.assertEqual(CoreMedia.kCMBufferQueueTrigger_WhenEndOfDataReached, 8)
        self.assertEqual(CoreMedia.kCMBufferQueueTrigger_WhenReset, 9)
        self.assertEqual(
            CoreMedia.kCMBufferQueueTrigger_WhenBufferCountBecomesLessThan, 10
        )
        self.assertEqual(
            CoreMedia.kCMBufferQueueTrigger_WhenBufferCountBecomesGreaterThan, 11
        )
        self.assertEqual(
            CoreMedia.kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualToAndBufferCountBecomesGreaterThan,
            12,
        )

    def test_cftypes(self):
        self.assertIsCFType(CoreMedia.CMBufferQueueRef)

    def test_opaque(self):
        self.assertIsOpaquePointer(CoreMedia.CMBufferQueueTriggerToken)

    @expectedFailure
    def test_functions_manual(self):
        self.fail("CMBufferQueueGetCallbacksForUnsortedSampleBuffers")
        self.fail("CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS")
        self.fail("CMBufferQueueCreate")

    def test_functions(self):
        CoreMedia.CMBufferQueueGetTypeID
        CoreMedia.CMBufferQueueEnqueue

        self.assertResultIsCFRetained(CoreMedia.CMBufferQueueDequeueAndRetain)
        self.assertResultIsCFRetained(
            CoreMedia.CMBufferQueueDequeueIfDataReadyAndRetain
        )

        CoreMedia.CMBufferQueueGetHead

        self.assertResultIsBOOL(CoreMedia.CMBufferQueueIsEmpty)

        CoreMedia.CMBufferQueueMarkEndOfData

        self.assertResultIsBOOL(CoreMedia.CMBufferQueueContainsEndOfData)
        self.assertResultIsBOOL(CoreMedia.CMBufferQueueIsAtEndOfData)

        CoreMedia.CMBufferQueueReset

        self.assertArgIsFunction(
            CoreMedia.CMBufferQueueResetWithCallback, 1, b"v@^v", False
        )

        CoreMedia.CMBufferQueueGetBufferCount
        CoreMedia.CMBufferQueueGetDuration
        CoreMedia.CMBufferQueueGetMinDecodeTimeStamp
        CoreMedia.CMBufferQueueGetFirstDecodeTimeStamp
        CoreMedia.CMBufferQueueGetMinPresentationTimeStamp
        CoreMedia.CMBufferQueueGetFirstPresentationTimeStamp
        CoreMedia.CMBufferQueueGetMaxPresentationTimeStamp
        CoreMedia.CMBufferQueueGetEndPresentationTimeStamp

        self.assertArgIsFunction(
            CoreMedia.CMBufferQueueInstallTrigger,
            1,
            b"v^v^{opaqueCMBufferQueueTriggerToken=}",
            True,
        )
        self.assertArgIsOut(CoreMedia.CMBufferQueueInstallTrigger, 5)

        self.assertArgIsFunction(
            CoreMedia.CMBufferQueueInstallTriggerWithIntegerThreshold,
            1,
            b"v^v^{opaqueCMBufferQueueTriggerToken=}",
            True,
        )
        self.assertArgIsOut(
            CoreMedia.CMBufferQueueInstallTriggerWithIntegerThreshold, 5
        )

        CoreMedia.CMBufferQueueRemoveTrigger

        self.assertResultIsBOOL(CoreMedia.CMBufferQueueTestTrigger)

        self.assertArgIsFunction(
            CoreMedia.CMBufferQueueCallForEachBuffer, 1, b"i@^v", True
        )

        self.assertArgIsFunction(
            CoreMedia.CMBufferQueueSetValidationCallback,
            1,
            b"i^{opaqueCMBufferQueue=}@^v",
            True,
        )

    @min_os_level("10.10")
    def test_functions10_10(self):
        CoreMedia.CMBufferQueueGetTotalSize

    @min_os_level("10.14.4")
    def test_functions10_14_4(self):
        self.assertNotHasAttr(CoreMedia, "CMBufferQueueCreateWithHandlers")

        self.assertArgIsOut(CoreMedia.CMBufferQueueInstallTriggerHandler, 3)
        self.assertArgIsBlock(
            CoreMedia.CMBufferQueueInstallTriggerHandler,
            4,
            b"v^{opaqueCMBufferQueueTriggerToken=}",
        )

        self.assertArgIsOut(
            CoreMedia.CMBufferQueueInstallTriggerHandlerWithIntegerThreshold, 3
        )
        self.assertArgIsBlock(
            CoreMedia.CMBufferQueueInstallTriggerHandlerWithIntegerThreshold,
            4,
            b"v^{opaqueCMBufferQueueTriggerToken=}",
        )

        self.assertArgIsBlock(CoreMedia.CMBufferQueueSetValidationHandler, 1, b"v@@")
