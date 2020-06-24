import CoreServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestUTType(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreServices.kUTExportedTypeDeclarationsKey, str)
        self.assertIsInstance(CoreServices.kUTImportedTypeDeclarationsKey, str)
        self.assertIsInstance(CoreServices.kUTTypeIdentifierKey, str)
        self.assertIsInstance(CoreServices.kUTTypeTagSpecificationKey, str)
        self.assertIsInstance(CoreServices.kUTTypeConformsToKey, str)
        self.assertIsInstance(CoreServices.kUTTypeDescriptionKey, str)
        self.assertIsInstance(CoreServices.kUTTypeIconFileKey, str)
        self.assertIsInstance(CoreServices.kUTTypeReferenceURLKey, str)
        self.assertIsInstance(CoreServices.kUTTypeVersionKey, str)
        self.assertIsInstance(CoreServices.kUTTagClassFilenameExtension, str)
        self.assertIsInstance(CoreServices.kUTTagClassMIMEType, str)
        self.assertIsInstance(CoreServices.kUTTagClassNSPboardType, str)
        self.assertIsInstance(CoreServices.kUTTagClassOSType, str)

    def testFunctions(self):
        self.assertResultIsCFRetained(
            CoreServices.UTTypeCreatePreferredIdentifierForTag
        )
        v = CoreServices.UTTypeCreatePreferredIdentifierForTag(
            CoreServices.kUTTagClassFilenameExtension,
            "py",
            CoreServices.kUTTypePlainText,
        )
        self.assertIsInstance(v, str)

        self.assertResultIsCFRetained(CoreServices.UTTypeCreateAllIdentifiersForTag)
        v = CoreServices.UTTypeCreateAllIdentifiersForTag(
            CoreServices.kUTTagClassFilenameExtension,
            "py",
            CoreServices.kUTTypePlainText,
        )
        self.assertIsInstance(v, CoreServices.CFArrayRef)
        self.assertGreaterEqual(len(v), 1)
        self.assertIsInstance(v[0], str)

        self.assertResultIsCFRetained(CoreServices.UTTypeCopyPreferredTagWithClass)
        v = CoreServices.UTTypeCopyPreferredTagWithClass(
            "public.python-script", CoreServices.kUTTagClassFilenameExtension
        )
        self.assertIsInstance(v, str)

        self.assertResultIsBOOL(CoreServices.UTTypeEqual)
        v = CoreServices.UTTypeEqual("public.python-script", "public.python-script")
        self.assertIs(v, True)

        self.assertResultIsBOOL(CoreServices.UTTypeConformsTo)
        v = CoreServices.UTTypeConformsTo(
            "public.python-script", CoreServices.kUTTypePlainText
        )
        self.assertIs(v, True)

        self.assertResultIsCFRetained(CoreServices.UTTypeCopyDescription)
        v = CoreServices.UTTypeCopyDescription(CoreServices.kUTTypePlainText)
        self.assertIsInstance(v, str)

        self.assertResultIsCFRetained(CoreServices.UTTypeCopyDeclaration)
        v = CoreServices.UTTypeCopyDeclaration(CoreServices.kUTTypePlainText)
        self.assertIsInstance(v, CoreServices.CFDictionaryRef)

        self.assertResultIsCFRetained(CoreServices.UTTypeCopyDeclaringBundleURL)
        v = CoreServices.UTTypeCopyDeclaringBundleURL(CoreServices.kUTTypePlainText)
        self.assertIsInstance(v, CoreServices.CFURLRef)

        self.assertResultIsCFRetained(CoreServices.UTCreateStringForOSType)
        v = CoreServices.UTCreateStringForOSType(24353)
        self.assertIsInstance(v, str)

        v = CoreServices.UTGetOSTypeFromString(v)
        self.assertEqual(v, 24353)

    @min_os_level("10.10")
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(CoreServices.UTTypeCopyAllTagsWithClass)
        v = CoreServices.UTTypeCopyAllTagsWithClass(
            CoreServices.kUTTypeArchive, CoreServices.kUTTagClassFilenameExtension
        )
        self.assertIsInstance(v, (CoreServices.CFArrayRef, type(None)))

        self.assertResultIsBOOL(CoreServices.UTTypeConformsTo)
        v = CoreServices.UTTypeIsDeclared("public.python-script")
        self.assertTrue(v in (True, False))

        self.assertResultIsBOOL(CoreServices.UTTypeIsDynamic)
        v = CoreServices.UTTypeIsDynamic("public.python-script")
        self.assertTrue(v in (True, False))
