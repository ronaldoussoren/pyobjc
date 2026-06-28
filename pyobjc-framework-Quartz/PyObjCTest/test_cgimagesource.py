import Quartz
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCGImageSource(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Quartz.CGImageSourceStatus)
        self.assertEqual(Quartz.kCGImageStatusUnexpectedEOF, -5)
        self.assertEqual(Quartz.kCGImageStatusInvalidData, -4)
        self.assertEqual(Quartz.kCGImageStatusUnknownType, -3)
        self.assertEqual(Quartz.kCGImageStatusReadingHeader, -2)
        self.assertEqual(Quartz.kCGImageStatusIncomplete, -1)
        self.assertEqual(Quartz.kCGImageStatusComplete, 0)

    def test_constants(self):
        self.assertIsInstance(Quartz.kCGImageSourceTypeIdentifierHint, str)
        self.assertIsInstance(Quartz.kCGImageSourceShouldCache, str)
        self.assertIsInstance(Quartz.kCGImageSourceShouldAllowFloat, str)
        self.assertIsInstance(
            Quartz.kCGImageSourceCreateThumbnailFromImageIfAbsent, str
        )
        self.assertIsInstance(Quartz.kCGImageSourceCreateThumbnailFromImageAlways, str)
        self.assertIsInstance(Quartz.kCGImageSourceThumbnailMaxPixelSize, str)
        self.assertIsInstance(Quartz.kCGImageSourceCreateThumbnailWithTransform, str)
        self.assertIsInstance(Quartz.kCGImageSourceShouldCacheImmediately, str)

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(Quartz.kCGImageSourceSubsampleFactor, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(Quartz.kCGImageSourceDecodeRequest, str)
        self.assertIsInstance(Quartz.kCGImageSourceDecodeToHDR, str)
        self.assertIsInstance(Quartz.kCGImageSourceDecodeToSDR, str)
        self.assertIsInstance(Quartz.kCGImageSourceDecodeRequestOptions, str)

    @min_os_level("15.0")
    def test_constants15_0(self):
        self.assertIsInstance(
            Quartz.kCGImageSourceGenerateImageSpecificLumaScaling, str
        )

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(Quartz.kCGComputeHDRStats, str)

    @min_os_level("27.0")
    def test_constants27_0(self):
        self.assertIsInstance(Quartz.kCGImageSourceAllowableTypes, str)

    def test_types(self):
        self.assertIsCFType(Quartz.CGImageSourceRef)

    def test_functions(self):
        self.assertIsInstance(Quartz.CGImageSourceGetTypeID(), int)

        self.assertResultIsCFRetained(Quartz.CGImageSourceCopyTypeIdentifiers)
        self.assertResultIsCFRetained(Quartz.CGImageSourceCreateWithDataProvider)
        self.assertResultIsCFRetained(Quartz.CGImageSourceCreateWithData)
        self.assertResultIsCFRetained(Quartz.CGImageSourceCreateWithURL)

        Quartz.CGImageSourceGetType
        Quartz.CGImageSourceGetCount

        self.assertResultIsCFRetained(Quartz.CGImageSourceCopyProperties)
        self.assertResultIsCFRetained(Quartz.CGImageSourceCopyPropertiesAtIndex)
        self.assertResultIsCFRetained(Quartz.CGImageSourceCreateImageAtIndex)
        self.assertResultIsCFRetained(Quartz.CGImageSourceCreateThumbnailAtIndex)
        self.assertResultIsCFRetained(Quartz.CGImageSourceCreateIncremental)
        self.assertArgHasType(Quartz.CGImageSourceUpdateData, 2, objc._C_BOOL)
        self.assertArgHasType(Quartz.CGImageSourceUpdateDataProvider, 2, objc._C_BOOL)

        Quartz.CGImageSourceGetStatus
        Quartz.CGImageSourceGetStatusAtIndex

        self.assertResultIsCFRetained(Quartz.CGImageSourceCopyMetadataAtIndex)

        Quartz.CGImageSourceRemoveCacheAtIndex

    @min_os_level("10.13")
    def test_functions10_13(self):
        self.assertResultIsCFRetained(Quartz.CGImageSourceCopyAuxiliaryDataInfoAtIndex)

    @min_os_level("10.14")
    def test_functions10_14(self):
        Quartz.CGImageSourceGetPrimaryImageIndex

    @min_os_level("14.2")
    def test_functions14_2(self):
        Quartz.CGImageSourceSetAllowableTypes
