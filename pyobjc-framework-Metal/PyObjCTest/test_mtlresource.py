import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestMTLResourceHelper(Metal.NSObject):
    def cpuCacheMode(self):
        return 1

    def storageMode(self):
        return 1

    def hazardTrackingMode(self):
        return 1

    def resourceOptions(self):
        return 1

    def setPurgeableState_(self, a):
        return 1

    def heapOffset(self):
        return 1

    def allocatedSize(self):
        return 1

    def isAliasable(self):
        return 1

    def setOwnerWithIdentity_(self, a):
        return 1


class TestMTLResource(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLCPUCacheMode)
        self.assertIsEnumType(Metal.MTLHazardTrackingMode)
        self.assertIsEnumType(Metal.MTLPurgeableState)
        self.assertIsEnumType(Metal.MTLResourceOptions)
        self.assertIsEnumType(Metal.MTLStorageMode)

    def test_constants(self):
        self.assertEqual(Metal.MTLPurgeableStateKeepCurrent, 1)
        self.assertEqual(Metal.MTLPurgeableStateNonVolatile, 2)
        self.assertEqual(Metal.MTLPurgeableStateVolatile, 3)
        self.assertEqual(Metal.MTLPurgeableStateEmpty, 4)

        self.assertEqual(Metal.MTLCPUCacheModeDefaultCache, 0)
        self.assertEqual(Metal.MTLCPUCacheModeWriteCombined, 1)

        self.assertEqual(Metal.MTLStorageModeShared, 0)
        self.assertEqual(Metal.MTLStorageModeManaged, 1)
        self.assertEqual(Metal.MTLStorageModePrivate, 2)

        self.assertEqual(Metal.MTLHazardTrackingModeDefault, 0)
        self.assertEqual(Metal.MTLHazardTrackingModeUntracked, 1)
        self.assertEqual(Metal.MTLHazardTrackingModeTracked, 2)

        self.assertEqual(Metal.MTLResourceCPUCacheModeShift, 0)
        self.assertEqual(
            Metal.MTLResourceCPUCacheModeMask, 0xF << Metal.MTLResourceCPUCacheModeShift
        )

        self.assertEqual(Metal.MTLResourceStorageModeShift, 4)
        self.assertEqual(
            Metal.MTLResourceStorageModeMask, 0xF << Metal.MTLResourceStorageModeShift
        )

        self.assertEqual(Metal.MTLResourceHazardTrackingModeShift, 8)
        self.assertEqual(
            Metal.MTLResourceHazardTrackingModeMask,
            0x3 << Metal.MTLResourceHazardTrackingModeShift,
        )

        self.assertEqual(
            Metal.MTLResourceCPUCacheModeDefaultCache,
            Metal.MTLCPUCacheModeDefaultCache << Metal.MTLResourceCPUCacheModeShift,
        )
        self.assertEqual(
            Metal.MTLResourceCPUCacheModeWriteCombined,
            Metal.MTLCPUCacheModeWriteCombined << Metal.MTLResourceCPUCacheModeShift,
        )

        self.assertEqual(
            Metal.MTLResourceStorageModeShared,
            Metal.MTLStorageModeShared << Metal.MTLResourceStorageModeShift,
        )
        self.assertEqual(
            Metal.MTLResourceStorageModeManaged,
            Metal.MTLStorageModeManaged << Metal.MTLResourceStorageModeShift,
        )
        self.assertEqual(
            Metal.MTLResourceStorageModePrivate,
            Metal.MTLStorageModePrivate << Metal.MTLResourceStorageModeShift,
        )
        self.assertEqual(
            Metal.MTLResourceStorageModeMemoryless,
            Metal.MTLStorageModeMemoryless << Metal.MTLResourceStorageModeShift,
        )

        self.assertEqual(
            Metal.MTLResourceHazardTrackingModeDefault,
            Metal.MTLHazardTrackingModeDefault
            << Metal.MTLResourceHazardTrackingModeShift,
        )
        self.assertEqual(
            Metal.MTLResourceHazardTrackingModeUntracked,
            Metal.MTLHazardTrackingModeUntracked
            << Metal.MTLResourceHazardTrackingModeShift,
        )
        self.assertEqual(
            Metal.MTLResourceHazardTrackingModeTracked,
            Metal.MTLHazardTrackingModeTracked
            << Metal.MTLResourceHazardTrackingModeShift,
        )

        self.assertEqual(
            Metal.MTLResourceOptionCPUCacheModeDefault,
            Metal.MTLResourceCPUCacheModeDefaultCache,
        )
        self.assertEqual(
            Metal.MTLResourceOptionCPUCacheModeWriteCombined,
            Metal.MTLResourceCPUCacheModeWriteCombined,
        )

    @min_sdk_level("10.11")
    def test_protocols(self):
        self.assertProtocolExists("MTLResource")

    def test_methods(self):
        self.assertResultHasType(
            Metal.TestMTLResourceHelper.cpuCacheMode, objc._C_NSUInteger
        )
        self.assertResultHasType(
            Metal.TestMTLResourceHelper.storageMode, objc._C_NSUInteger
        )
        self.assertResultHasType(
            Metal.TestMTLResourceHelper.hazardTrackingMode, objc._C_NSUInteger
        )
        self.assertResultHasType(
            Metal.TestMTLResourceHelper.resourceOptions, objc._C_NSUInteger
        )

        self.assertResultHasType(
            Metal.TestMTLResourceHelper.setPurgeableState_, objc._C_NSUInteger
        )
        self.assertArgHasType(
            Metal.TestMTLResourceHelper.setPurgeableState_, 0, objc._C_NSUInteger
        )

        self.assertResultHasType(
            Metal.TestMTLResourceHelper.heapOffset, objc._C_NSUInteger
        )
        self.assertResultHasType(
            Metal.TestMTLResourceHelper.allocatedSize, objc._C_NSUInteger
        )

        self.assertResultIsBOOL(Metal.TestMTLResourceHelper.isAliasable)

        self.assertResultHasType(
            Metal.TestMTLResourceHelper.setOwnerWithIdentity_, objc._C_INT
        )
        self.assertArgHasType(
            Metal.TestMTLResourceHelper.setOwnerWithIdentity_, 0, objc._C_UINT
        )
