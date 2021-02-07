import warnings

from PyObjCTools.TestSupport import TestCase, min_os_level

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import LaunchServices


class TestUTType(TestCase):
    def testConstants(self):
        self.assertIsInstance(LaunchServices.kUTExportedTypeDeclarationsKey, str)
        self.assertIsInstance(LaunchServices.kUTImportedTypeDeclarationsKey, str)
        self.assertIsInstance(LaunchServices.kUTTypeIdentifierKey, str)
        self.assertIsInstance(LaunchServices.kUTTypeTagSpecificationKey, str)
        self.assertIsInstance(LaunchServices.kUTTypeConformsToKey, str)
        self.assertIsInstance(LaunchServices.kUTTypeDescriptionKey, str)
        self.assertIsInstance(LaunchServices.kUTTypeIconFileKey, str)
        self.assertIsInstance(LaunchServices.kUTTypeReferenceURLKey, str)
        self.assertIsInstance(LaunchServices.kUTTypeVersionKey, str)
        self.assertIsInstance(LaunchServices.kUTTagClassFilenameExtension, str)
        self.assertIsInstance(LaunchServices.kUTTagClassMIMEType, str)
        self.assertIsInstance(LaunchServices.kUTTagClassNSPboardType, str)
        self.assertIsInstance(LaunchServices.kUTTagClassOSType, str)

    def testFunctions(self):
        self.assertResultIsCFRetained(
            LaunchServices.UTTypeCreatePreferredIdentifierForTag
        )
        v = LaunchServices.UTTypeCreatePreferredIdentifierForTag(
            LaunchServices.kUTTagClassFilenameExtension,
            "py",
            LaunchServices.kUTTypePlainText,
        )
        self.assertIsInstance(v, str)

        self.assertResultIsCFRetained(LaunchServices.UTTypeCreateAllIdentifiersForTag)
        v = LaunchServices.UTTypeCreateAllIdentifiersForTag(
            LaunchServices.kUTTagClassFilenameExtension,
            "py",
            LaunchServices.kUTTypePlainText,
        )
        self.assertIsInstance(v, LaunchServices.CFArrayRef)
        self.assertGreaterEqual(len(v), 1)
        self.assertIsInstance(v[0], str)

        self.assertResultIsCFRetained(LaunchServices.UTTypeCopyPreferredTagWithClass)
        v = LaunchServices.UTTypeCopyPreferredTagWithClass(
            "public.python-script", LaunchServices.kUTTagClassFilenameExtension
        )
        self.assertIsInstance(v, str)

        self.assertResultIsBOOL(LaunchServices.UTTypeEqual)
        v = LaunchServices.UTTypeEqual("public.python-script", "public.python-script")
        self.assertIs(v, True)

        self.assertResultIsBOOL(LaunchServices.UTTypeConformsTo)
        v = LaunchServices.UTTypeConformsTo(
            "public.python-script", LaunchServices.kUTTypePlainText
        )
        self.assertIs(v, True)

        self.assertResultIsCFRetained(LaunchServices.UTTypeCopyDescription)
        v = LaunchServices.UTTypeCopyDescription(LaunchServices.kUTTypePlainText)
        self.assertIsInstance(v, str)

        self.assertResultIsCFRetained(LaunchServices.UTTypeCopyDeclaration)
        v = LaunchServices.UTTypeCopyDeclaration(LaunchServices.kUTTypePlainText)
        self.assertIsInstance(v, LaunchServices.CFDictionaryRef)

        self.assertResultIsCFRetained(LaunchServices.UTTypeCopyDeclaringBundleURL)
        v = LaunchServices.UTTypeCopyDeclaringBundleURL(LaunchServices.kUTTypePlainText)
        self.assertIsInstance(v, LaunchServices.CFURLRef)

        self.assertResultIsCFRetained(LaunchServices.UTCreateStringForOSType)
        v = LaunchServices.UTCreateStringForOSType(24353)
        self.assertIsInstance(v, str)

        v = LaunchServices.UTGetOSTypeFromString(v)
        self.assertEqual(v, 24353)

    @min_os_level("10.10")
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(LaunchServices.UTTypeCopyAllTagsWithClass)
        v = LaunchServices.UTTypeCopyAllTagsWithClass(
            LaunchServices.kUTTypeArchive, LaunchServices.kUTTagClassFilenameExtension
        )
        self.assertIsInstance(v, (LaunchServices.CFArrayRef, type(None)))

        self.assertResultIsBOOL(LaunchServices.UTTypeConformsTo)
        v = LaunchServices.UTTypeIsDeclared("public.python-script")
        self.assertTrue(v in (True, False))

        self.assertResultIsBOOL(LaunchServices.UTTypeIsDynamic)
        v = LaunchServices.UTTypeIsDynamic("public.python-script")
        self.assertTrue(v in (True, False))
