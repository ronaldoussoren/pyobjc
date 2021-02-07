import Quartz
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCGImageSource(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kCGImageStatusUnexpectedEOF, -5)
        self.assertEqual(Quartz.kCGImageStatusInvalidData, -4)
        self.assertEqual(Quartz.kCGImageStatusUnknownType, -3)
        self.assertEqual(Quartz.kCGImageStatusReadingHeader, -2)
        self.assertEqual(Quartz.kCGImageStatusIncomplete, -1)
        self.assertEqual(Quartz.kCGImageStatusComplete, 0)

        self.assertIsInstance(Quartz.kCGImageSourceTypeIdentifierHint, str)
        self.assertIsInstance(Quartz.kCGImageSourceShouldCache, str)
        self.assertIsInstance(Quartz.kCGImageSourceShouldAllowFloat, str)
        self.assertIsInstance(
            Quartz.kCGImageSourceCreateThumbnailFromImageIfAbsent, str
        )
        self.assertIsInstance(Quartz.kCGImageSourceCreateThumbnailFromImageAlways, str)
        self.assertIsInstance(Quartz.kCGImageSourceThumbnailMaxPixelSize, str)
        self.assertIsInstance(Quartz.kCGImageSourceCreateThumbnailWithTransform, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(Quartz.kCGImageSourceShouldCacheImmediately, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(Quartz.kCGImageSourceSubsampleFactor, str)

    def testTypes(self):
        self.assertIsCFType(Quartz.CGImageSourceRef)

    def testFunctions(self):
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

    @min_os_level("10.8")
    def testFunctions10_8(self):
        self.assertResultIsCFRetained(Quartz.CGImageSourceCopyMetadataAtIndex)

    @min_os_level("10.9")
    def testFunctions10_9(self):
        Quartz.CGImageSourceRemoveCacheAtIndex

    @min_os_level("10.13")
    def testFunctions10_13(self):
        self.assertResultIsCFRetained(Quartz.CGImageSourceCopyAuxiliaryDataInfoAtIndex)

    @min_os_level("10.14")
    def testFunctions10_14(self):
        Quartz.CGImageSourceGetPrimaryImageIndex
