import IOSurface
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestIOSurfaceObjC(TestCase):
    def testEnum(self):
        self.assertIsEnumType(IOSurface.IOSurfaceComponentName)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameUnknown, 0)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameAlpha, 1)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameRed, 2)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameGreen, 3)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameBlue, 4)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameLuma, 5)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameChromaRed, 6)
        self.assertEqual(IOSurface.kIOSurfaceComponentNameChromaBlue, 7)

        self.assertIsEnumType(IOSurface.IOSurfaceComponentType)
        self.assertEqual(IOSurface.kIOSurfaceComponentTypeUnknown, 0)
        self.assertEqual(IOSurface.kIOSurfaceComponentTypeUnsignedInteger, 1)
        self.assertEqual(IOSurface.kIOSurfaceComponentTypeSignedInteger, 2)
        self.assertEqual(IOSurface.kIOSurfaceComponentTypeFloat, 3)
        self.assertEqual(IOSurface.kIOSurfaceComponentTypeSignedNormalized, 4)

        self.assertIsEnumType(IOSurface.IOSurfaceComponentRange)
        self.assertEqual(IOSurface.kIOSurfaceComponentRangeUnknown, 0)
        self.assertEqual(IOSurface.kIOSurfaceComponentRangeFullRange, 1)
        self.assertEqual(IOSurface.kIOSurfaceComponentRangeVideoRange, 2)
        self.assertEqual(IOSurface.kIOSurfaceComponentRangeWideRange, 3)

        self.assertIsEnumType(IOSurface.IOSurfaceSubsampling)
        self.assertEqual(IOSurface.kIOSurfaceSubsamplingUnknown, 0)
        self.assertEqual(IOSurface.kIOSurfaceSubsamplingNone, 1)
        self.assertEqual(IOSurface.kIOSurfaceSubsampling422, 2)
        self.assertEqual(IOSurface.kIOSurfaceSubsampling420, 3)
        self.assertEqual(IOSurface.kIOSurfaceSubsampling411, 4)

        self.assertIsEnumType(IOSurface.IOSurfaceMemoryLedgerTags)
        self.assertEqual(IOSurface.kIOSurfaceMemoryLedgerTagDefault, 0x00000001)
        self.assertEqual(IOSurface.kIOSurfaceMemoryLedgerTagNetwork, 0x00000002)
        self.assertEqual(IOSurface.kIOSurfaceMemoryLedgerTagMedia, 0x00000003)
        self.assertEqual(IOSurface.kIOSurfaceMemoryLedgerTagGraphics, 0x00000004)
        self.assertEqual(IOSurface.kIOSurfaceMemoryLedgerTagNeural, 0x00000005)

        self.assertIsEnumType(IOSurface.IOSurfaceMemoryLedgerFlags)
        self.assertEqual(IOSurface.kIOSurfaceMemoryLedgerFlagNoFootprint, 1 << 0)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertIsInstance(IOSurface.kIOSurfaceAllocSize, str)
        self.assertIsInstance(IOSurface.kIOSurfaceWidth, str)
        self.assertIsInstance(IOSurface.kIOSurfaceHeight, str)
        self.assertIsInstance(IOSurface.kIOSurfaceBytesPerRow, str)
        self.assertIsInstance(IOSurface.kIOSurfaceBytesPerElement, str)
        self.assertIsInstance(IOSurface.kIOSurfaceElementWidth, str)
        self.assertIsInstance(IOSurface.kIOSurfaceElementHeight, str)
        self.assertIsInstance(IOSurface.kIOSurfaceOffset, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneInfo, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneWidth, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneHeight, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneBytesPerRow, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneOffset, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneSize, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneBase, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneBitsPerElement, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneBytesPerElement, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneElementWidth, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneElementHeight, str)
        self.assertIsInstance(IOSurface.kIOSurfaceCacheMode, str)
        self.assertIsInstance(IOSurface.kIOSurfaceIsGlobal, str)
        self.assertIsInstance(IOSurface.kIOSurfacePixelFormat, str)
        self.assertIsInstance(IOSurface.kIOSurfaceColorSpace, str)
        self.assertIsInstance(IOSurface.kIOSurfaceICCProfile, str)

    @min_os_level("10.12")
    def test_constants10_12(self):
        self.assertIsInstance(IOSurface.kIOSurfacePixelSizeCastingAllowed, str)

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(IOSurface.kIOSurfacePlaneComponentBitDepths, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneComponentBitOffsets, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneComponentNames, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneComponentTypes, str)
        self.assertIsInstance(IOSurface.kIOSurfacePlaneComponentRanges, str)
        self.assertIsInstance(IOSurface.kIOSurfaceSubsampling, str)

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(IOSurface.kIOSurfaceName, str)

    def test_funtions(self):
        IOSurface.IOSurfaceGetTypeID
        self.assertResultIsCFRetained(IOSurface.IOSurfaceCreate)
        self.assertResultIsCFRetained(IOSurface.IOSurfaceLookup)
        IOSurface.IOSurfaceGetID
        self.assertArgIsOut(IOSurface.IOSurfaceLock, 2)
        self.assertArgIsOut(IOSurface.IOSurfaceUnlock, 2)
        IOSurface.IOSurfaceGetAllocSize
        IOSurface.IOSurfaceGetWidth
        IOSurface.IOSurfaceGetHeight
        IOSurface.IOSurfaceGetBytesPerElement
        IOSurface.IOSurfaceGetBytesPerRow
        IOSurface.IOSurfaceGetBaseAddress
        IOSurface.IOSurfaceGetElementWidth
        IOSurface.IOSurfaceGetElementHeight
        IOSurface.IOSurfaceGetPixelFormat
        IOSurface.IOSurfaceGetSeed
        IOSurface.IOSurfaceGetPlaneCount
        IOSurface.IOSurfaceGetWidthOfPlane
        IOSurface.IOSurfaceGetHeightOfPlane
        IOSurface.IOSurfaceGetBytesPerElementOfPlane
        IOSurface.IOSurfaceGetBytesPerRowOfPlane
        IOSurface.IOSurfaceGetBaseAddressOfPlane
        IOSurface.IOSurfaceGetElementWidthOfPlane
        IOSurface.IOSurfaceGetElementHeightOfPlane
        IOSurface.IOSurfaceGetNumberOfComponentsOfPlane
        IOSurface.IOSurfaceSetValue
        self.assertResultIsCFRetained(IOSurface.IOSurfaceCopyValue)
        IOSurface.IOSurfaceRemoveValue
        IOSurface.IOSurfaceSetValues
        self.assertResultIsCFRetained(IOSurface.IOSurfaceCopyAllValues)
        IOSurface.IOSurfaceRemoveAllValues
        IOSurface.IOSurfaceCreateMachPort
        self.assertResultIsCFRetained(IOSurface.IOSurfaceLookupFromMachPort)
        IOSurface.IOSurfaceGetPropertyMaximum
        IOSurface.IOSurfaceGetPropertyAlignment
        IOSurface.IOSurfaceAlignProperty
        IOSurface.IOSurfaceIncrementUseCount
        IOSurface.IOSurfaceDecrementUseCount
        IOSurface.IOSurfaceGetUseCount
        IOSurface.IOSurfaceIsInUse

    @min_os_level("10.12")
    def test_funtions10_12(self):
        IOSurface.IOSurfaceAllowsPixelSizeCasting
        IOSurface.IOSurfaceSetPurgeable
        self.assertArgIsOut(IOSurface.IOSurfaceSetPurgeable, 2)

    @min_os_level("10.13")
    def test_funtions10_13(self):
        IOSurface.IOSurfaceGetNameOfComponentOfPlane
        IOSurface.IOSurfaceGetTypeOfComponentOfPlane
        IOSurface.IOSurfaceGetRangeOfComponentOfPlane
        IOSurface.IOSurfaceGetBitDepthOfComponentOfPlane
        IOSurface.IOSurfaceGetBitOffsetOfComponentOfPlane
        IOSurface.IOSurfaceGetSubsampling

    @min_os_level("14.4")
    def test_funtions14_4(self):
        IOSurface.IOSurfaceSetOwnershipIdentity
