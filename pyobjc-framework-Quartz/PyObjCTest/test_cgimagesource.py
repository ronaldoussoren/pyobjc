from PyObjCTools.TestSupport import *

import Quartz

try:
    unicode
except NameError:
    unicode = str

try:
    long
except NameError:
    long = int

class TestCGImageSource (TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kCGImageStatusUnexpectedEOF, -5)
        self.assertEqual(Quartz.kCGImageStatusInvalidData, -4)
        self.assertEqual(Quartz.kCGImageStatusUnknownType, -3)
        self.assertEqual(Quartz.kCGImageStatusReadingHeader, -2)
        self.assertEqual(Quartz.kCGImageStatusIncomplete, -1)
        self.assertEqual(Quartz.kCGImageStatusComplete, 0)

        self.assertIsInstance(Quartz.kCGImageSourceTypeIdentifierHint, unicode)
        self.assertIsInstance(Quartz.kCGImageSourceShouldCache, unicode)
        self.assertIsInstance(Quartz.kCGImageSourceShouldAllowFloat, unicode)
        self.assertIsInstance(Quartz.kCGImageSourceCreateThumbnailFromImageIfAbsent, unicode)
        self.assertIsInstance(Quartz.kCGImageSourceThumbnailMaxPixelSize, unicode)
        self.assertIsInstance(Quartz.kCGImageSourceCreateThumbnailWithTransform, unicode)

    def testTypes(self):
        self.assertIsCFType(Quartz.CGImageSourceRef)

    def testFunctions(self):
        self.assertIsInstance(Quartz.CGImageSourceGetTypeID(), (int, long))

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

    @min_os_level('10.8')
    def testFunctions10_8(self):
        self.assertResultIsCFRetained(Quartz.CGImageSourceCopyMetadataAtIndex)

if __name__ == "__main__":
    main()
