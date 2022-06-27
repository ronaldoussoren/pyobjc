import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestMTLHeapHelper(Metal.NSObject):
    def storageMode(self):
        return 1

    def cpuCacheMode(self):
        return 1

    def hazardTrackingMode(self):
        return 1

    def resourceOptions(self):
        return 1

    def size(self):
        return 1

    def usedSize(self):
        return 1

    def maxAvailableSizeWithAlignment_(self, a):
        return 1

    def newBufferWithLength_options_(self, a, b):
        return 1

    def setPurgeableState_(self, a):
        return 1

    def type(self):  # noqa: A003
        return 1

    def newBufferWithLength_options_offset_(self, a, b, c):
        return 1

    def newTextureWithDescriptor_offset_(self, a, b):
        return 1

    def newAccelerationStructureWithSize_(self, a):
        return 1

    def newAccelerationStructureWithSize_offset_(self, a, b):
        return 1

    def newAccelerationStructureWithDescriptor_offset_(self, a, b):
        return 1


class TestMTLHeap(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLHeapType)

    def test_constants(self):
        self.assertEqual(Metal.MTLHeapTypeAutomatic, 0)
        self.assertEqual(Metal.MTLHeapTypePlacement, 1)
        self.assertEqual(Metal.MTLHeapTypeSparse, 2)

    @min_os_level("10.15")
    def test_protocols(self):
        self.assertProtocolExists("MTLHeap")

    def test_methods(self):
        self.assertResultHasType(TestMTLHeapHelper.storageMode, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLHeapHelper.cpuCacheMode, objc._C_NSUInteger)
        self.assertResultHasType(
            TestMTLHeapHelper.hazardTrackingMode, objc._C_NSUInteger
        )
        self.assertResultHasType(TestMTLHeapHelper.resourceOptions, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLHeapHelper.size, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLHeapHelper.usedSize, objc._C_NSUInteger)

        self.assertResultHasType(
            TestMTLHeapHelper.maxAvailableSizeWithAlignment_, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLHeapHelper.maxAvailableSizeWithAlignment_, 0, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLHeapHelper.newBufferWithLength_options_, 0, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLHeapHelper.newBufferWithLength_options_, 1, objc._C_NSUInteger
        )

        self.assertResultHasType(
            TestMTLHeapHelper.setPurgeableState_, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLHeapHelper.setPurgeableState_, 0, objc._C_NSUInteger
        )

        self.assertResultHasType(TestMTLHeapHelper.type, objc._C_NSInteger)

        self.assertArgHasType(
            TestMTLHeapHelper.newBufferWithLength_options_offset_, 0, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLHeapHelper.newBufferWithLength_options_offset_, 1, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLHeapHelper.newBufferWithLength_options_offset_, 2, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLHeapHelper.newTextureWithDescriptor_offset_, 1, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLHeapHelper.newAccelerationStructureWithSize_, 0, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLHeapHelper.newAccelerationStructureWithSize_offset_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLHeapHelper.newAccelerationStructureWithSize_offset_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLHeapHelper.newAccelerationStructureWithDescriptor_offset_,
            1,
            objc._C_NSUInteger,
        )
