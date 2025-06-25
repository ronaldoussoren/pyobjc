import CoreMedia
from PyObjCTools.TestSupport import TestCase, expectedFailure
import objc


class TestCMBlockBuffer(TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMBlockBufferNoErr, 0)
        self.assertEqual(CoreMedia.kCMBlockBufferStructureAllocationFailedErr, -12700)
        self.assertEqual(CoreMedia.kCMBlockBufferBlockAllocationFailedErr, -12701)
        self.assertEqual(CoreMedia.kCMBlockBufferBadCustomBlockSourceErr, -12702)
        self.assertEqual(CoreMedia.kCMBlockBufferBadOffsetParameterErr, -12703)
        self.assertEqual(CoreMedia.kCMBlockBufferBadLengthParameterErr, -12704)
        self.assertEqual(CoreMedia.kCMBlockBufferBadPointerParameterErr, -12705)
        self.assertEqual(CoreMedia.kCMBlockBufferEmptyBBufErr, -12706)
        self.assertEqual(CoreMedia.kCMBlockBufferUnallocatedBlockErr, -12707)
        self.assertEqual(CoreMedia.kCMBlockBufferInsufficientSpaceErr, -12708)

        self.assertEqual(CoreMedia.kCMBlockBufferAssureMemoryNowFlag, 1 << 0)
        self.assertEqual(CoreMedia.kCMBlockBufferAlwaysCopyDataFlag, 1 << 1)
        self.assertEqual(CoreMedia.kCMBlockBufferDontOptimizeDepthFlag, 1 << 2)
        self.assertEqual(CoreMedia.kCMBlockBufferPermitEmptyReferenceFlag, 1 << 3)

        self.assertEqual(CoreMedia.kCMBlockBufferCustomBlockSourceVersion, 0)

    def test_cftypes(self):
        self.assertIsCFType(CoreMedia.CMBlockBufferRef)

    def test_functions(self):
        self.assertArgIsOut(CoreMedia.CMBlockBufferCreateEmpty, 3)
        self.assertArgIsCFRetained(CoreMedia.CMBlockBufferCreateEmpty, 3)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferCreateEmpty, 0)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferCreateEmpty, 3)

        self.assertArgIsIn(CoreMedia.CMBlockBufferCreateWithMemoryBlock, 1)
        self.assertArgSizeInArg(CoreMedia.CMBlockBufferCreateWithMemoryBlock, 1, 2)
        self.assertArgIsIn(CoreMedia.CMBlockBufferCreateWithMemoryBlock, 4)
        self.assertArgIsOut(CoreMedia.CMBlockBufferCreateWithMemoryBlock, 8)
        self.assertArgIsCFRetained(CoreMedia.CMBlockBufferCreateWithMemoryBlock, 8)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferCreateWithMemoryBlock, 0)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferCreateWithMemoryBlock, 3)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferCreateWithMemoryBlock, 8)

        self.assertArgIsOut(CoreMedia.CMBlockBufferCreateWithBufferReference, 5)
        self.assertArgIsCFRetained(CoreMedia.CMBlockBufferCreateWithBufferReference, 5)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferCreateWithBufferReference, 0)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferCreateWithBufferReference, 1)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferCreateWithBufferReference, 5)

        self.assertArgIsIn(CoreMedia.CMBlockBufferCreateContiguous, 3)
        self.assertArgIsOut(CoreMedia.CMBlockBufferCreateContiguous, 7)
        self.assertArgIsCFRetained(CoreMedia.CMBlockBufferCreateContiguous, 7)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferCreateContiguous, 0)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferCreateContiguous, 1)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferCreateContiguous, 2)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferCreateContiguous, 7)

        self.assertIsInstance(CoreMedia.CMBlockBufferGetTypeID(), int)

        self.assertArgIsIn(CoreMedia.CMBlockBufferAppendMemoryBlock, 1)
        self.assertArgSizeInArg(CoreMedia.CMBlockBufferAppendMemoryBlock, 1, 2)
        self.assertArgIsIn(CoreMedia.CMBlockBufferAppendMemoryBlock, 4)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferAppendMemoryBlock, 0)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferAppendMemoryBlock, 3)

        self.assertArgIsIDLike(CoreMedia.CMBlockBufferAppendBufferReference, 0)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferAppendBufferReference, 1)

        self.assertArgIsIDLike(CoreMedia.CMBlockBufferAssureBlockMemory, 0)

        self.assertArgIsOut(CoreMedia.CMBlockBufferCopyDataBytes, 3)
        self.assertArgSizeInArg(CoreMedia.CMBlockBufferCopyDataBytes, 3, 2)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferCopyDataBytes, 0)

        self.assertArgIsIn(CoreMedia.CMBlockBufferReplaceDataBytes, 0)
        self.assertArgSizeInArg(CoreMedia.CMBlockBufferReplaceDataBytes, 0, 3)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferReplaceDataBytes, 1)

        self.assertArgIsIDLike(CoreMedia.CMBlockBufferFillDataBytes, 1)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferGetDataLength, 0)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferIsRangeContiguous, 0)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferIsEmpty, 0)

    @expectedFailure
    def test_functions_manual(self):
        # XXX: Need manual wrappers for these to support custom block sources:
        self.assertNotIsInstance(
            CoreMedia.CMBlockBufferCreateWithMemoryBlock, objc.function
        )
        self.assertNotIsInstance(CoreMedia.CMBlockBufferCreateContiguous, objc.function)
        self.assertNotIsInstance(CoreMedia.CMBlockBufferAppendMemoryBlock, objc.function)

        # XXX: Need manual wrapper to expose this function
        self.assertNotIsInstance(CoreMedia.CMBlockBufferAccessDataBytes, objc.function)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferAccessDataBytes, 0)
        self.assertNotIsInstance(CoreMedia.CMBlockBufferGetDataPointer, objc.function)
        self.assertArgIsIDLike(CoreMedia.CMBlockBufferGetDataPointer, 0)
