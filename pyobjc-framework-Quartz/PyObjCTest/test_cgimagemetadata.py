import Quartz
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCGImageMetadata(TestCase):
    @min_os_level("10.8")
    def testTypes10_8(self):
        self.assertIsCFType(Quartz.CGImageMetadataRef)
        self.assertIsCFType(Quartz.CGImageMetadataTagRef)

    @min_os_level("10.8")
    def testFunctions10_8(self):
        self.assertIsInstance(Quartz.CGImageMetadataGetTypeID(), int)
        self.assertIsInstance(Quartz.CGImageMetadataTagGetTypeID(), int)

        self.assertResultIsCFRetained(Quartz.CGImageMetadataCreateMutable)
        m = Quartz.CGImageMetadataCreateMutable()
        self.assertIsInstance(m, Quartz.CGImageMetadataRef)

        self.assertResultIsCFRetained(Quartz.CGImageMetadataCreateMutableCopy)
        m2 = Quartz.CGImageMetadataCreateMutableCopy(m)
        self.assertIsInstance(m2, Quartz.CGImageMetadataRef)

        self.assertResultIsCFRetained(Quartz.CGImageMetadataTagCreate)
        self.assertResultHasType(Quartz.CGImageMetadataTagCopyValue, objc._C_ID)
        t = Quartz.CGImageMetadataTagCreate(
            Quartz.kCGImageMetadataNamespaceExif,
            Quartz.kCGImageMetadataPrefixExif,
            "name",
            Quartz.kCGImageMetadataTypeString,
            "value",
        )
        self.assertIsInstance(t, Quartz.CGImageMetadataTagRef)

        self.assertResultIsCFRetained(Quartz.CGImageMetadataTagCopyNamespace)
        self.assertResultIsCFRetained(Quartz.CGImageMetadataTagCopyPrefix)
        self.assertResultIsCFRetained(Quartz.CGImageMetadataTagCopyName)
        self.assertResultHasType(Quartz.CGImageMetadataTagCopyValue, objc._C_ID)
        self.assertResultIsCFRetained(Quartz.CGImageMetadataTagCopyValue)
        self.assertResultIsCFRetained(Quartz.CGImageMetadataTagCopyQualifiers)
        self.assertResultIsCFRetained(Quartz.CGImageMetadataCopyTags)
        self.assertResultIsCFRetained(Quartz.CGImageMetadataCopyTagWithPath)
        self.assertResultIsCFRetained(Quartz.CGImageMetadataCopyStringValueWithPath)
        self.assertResultHasType(
            Quartz.CGImageMetadataRegisterNamespaceForPrefix, objc._C_BOOL
        )
        self.assertArgIsOut(Quartz.CGImageMetadataRegisterNamespaceForPrefix, 3)
        self.assertResultHasType(Quartz.CGImageMetadataSetTagWithPath, objc._C_BOOL)
        self.assertResultHasType(Quartz.CGImageMetadataSetValueWithPath, objc._C_BOOL)
        self.assertArgHasType(Quartz.CGImageMetadataSetValueWithPath, 3, objc._C_ID)
        self.assertResultHasType(Quartz.CGImageMetadataRemoveTagWithPath, objc._C_BOOL)

        CGImageMetadataTagBlock = objc._C_BOOL + b"@@"
        self.assertArgIsBlock(
            Quartz.CGImageMetadataEnumerateTagsUsingBlock, 3, CGImageMetadataTagBlock
        )

        self.assertResultIsCFRetained(
            Quartz.CGImageMetadataCopyTagMatchingImageProperty
        )
        self.assertResultHasType(
            Quartz.CGImageMetadataSetValueMatchingImageProperty, objc._C_BOOL
        )
        self.assertArgHasType(
            Quartz.CGImageMetadataSetValueMatchingImageProperty, 3, objc._C_ID
        )
        self.assertResultIsCFRetained(Quartz.CGImageMetadataCreateXMPData)
        self.assertResultIsCFRetained(Quartz.CGImageMetadataCreateFromXMPData)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(Quartz.kCGImageMetadataNamespaceExif, str)
        self.assertIsInstance(Quartz.kCGImageMetadataNamespaceExifAux, str)
        self.assertIsInstance(Quartz.kCGImageMetadataNamespaceDublinCore, str)
        self.assertIsInstance(Quartz.kCGImageMetadataNamespaceIPTCCore, str)
        self.assertIsInstance(Quartz.kCGImageMetadataNamespacePhotoshop, str)
        self.assertIsInstance(Quartz.kCGImageMetadataNamespaceTIFF, str)
        self.assertIsInstance(Quartz.kCGImageMetadataNamespaceXMPBasic, str)
        self.assertIsInstance(Quartz.kCGImageMetadataNamespaceXMPRights, str)
        self.assertIsInstance(Quartz.kCGImageMetadataPrefixExif, str)
        self.assertIsInstance(Quartz.kCGImageMetadataPrefixExifAux, str)
        self.assertIsInstance(Quartz.kCGImageMetadataPrefixDublinCore, str)
        self.assertIsInstance(Quartz.kCGImageMetadataPrefixIPTCCore, str)
        self.assertIsInstance(Quartz.kCGImageMetadataPrefixPhotoshop, str)
        self.assertIsInstance(Quartz.kCGImageMetadataPrefixTIFF, str)
        self.assertIsInstance(Quartz.kCGImageMetadataPrefixXMPBasic, str)
        self.assertIsInstance(Quartz.kCGImageMetadataPrefixXMPRights, str)

        self.assertEqual(Quartz.kCGImageMetadataTypeInvalid, -1)
        self.assertEqual(Quartz.kCGImageMetadataTypeDefault, 0)
        self.assertEqual(Quartz.kCGImageMetadataTypeString, 1)
        self.assertEqual(Quartz.kCGImageMetadataTypeArrayUnordered, 2)
        self.assertEqual(Quartz.kCGImageMetadataTypeArrayOrdered, 3)
        self.assertEqual(Quartz.kCGImageMetadataTypeAlternateArray, 4)
        self.assertEqual(Quartz.kCGImageMetadataTypeAlternateText, 5)
        self.assertEqual(Quartz.kCGImageMetadataTypeStructure, 6)

        self.assertIsInstance(Quartz.kCGImageMetadataEnumerateRecursively, str)
        self.assertIsInstance(Quartz.kCFErrorDomainCGImageMetadata, str)

        self.assertEqual(Quartz.kCGImageMetadataErrorUnknown, 0)
        self.assertEqual(Quartz.kCGImageMetadataErrorUnsupportedFormat, 1)
        self.assertEqual(Quartz.kCGImageMetadataErrorBadArgument, 2)
        self.assertEqual(Quartz.kCGImageMetadataErrorConflictingArguments, 3)
        self.assertEqual(Quartz.kCGImageMetadataErrorPrefixConflict, 4)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(Quartz.kCGImageMetadataNamespaceExifEX, str)
        self.assertIsInstance(Quartz.kCGImageMetadataPrefixExifEX, str)

    @min_os_level("10.13.4")
    def testConstants10_13_4(self):
        self.assertIsInstance(Quartz.kCGImageMetadataNamespaceIPTCExtension, str)
        self.assertIsInstance(Quartz.kCGImageMetadataPrefixIPTCExtension, str)
