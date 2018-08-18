
from PyObjCTools.TestSupport import *
import LaunchServices

class TestUTType (TestCase):
    def testConstants(self):
        self.assertIsInstance(LaunchServices.kUTExportedTypeDeclarationsKey, unicode)
        self.assertIsInstance(LaunchServices.kUTImportedTypeDeclarationsKey, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeIdentifierKey, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeTagSpecificationKey, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeConformsToKey, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeDescriptionKey, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeIconFileKey, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeReferenceURLKey, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeVersionKey, unicode)
        self.assertIsInstance(LaunchServices.kUTTagClassFilenameExtension, unicode)
        self.assertIsInstance(LaunchServices.kUTTagClassMIMEType, unicode)
        self.assertIsInstance(LaunchServices.kUTTagClassNSPboardType, unicode)
        self.assertIsInstance(LaunchServices.kUTTagClassOSType, unicode)

    def testFunctions(self):
        self.assertResultIsCFRetained(LaunchServices.UTTypeCreatePreferredIdentifierForTag)
        v = LaunchServices.UTTypeCreatePreferredIdentifierForTag(LaunchServices.kUTTagClassFilenameExtension, "py", LaunchServices.kUTTypePlainText)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(LaunchServices.UTTypeCreateAllIdentifiersForTag)
        v = LaunchServices.UTTypeCreateAllIdentifiersForTag(LaunchServices.kUTTagClassFilenameExtension, "py", LaunchServices.kUTTypePlainText)
        self.assertIsInstance(v, LaunchServices.CFArrayRef)
        self.assertGreaterEqual(len(v), 1)
        self.assertIsInstance(v[0], unicode)

        self.assertResultIsCFRetained(LaunchServices.UTTypeCopyPreferredTagWithClass)
        v = LaunchServices.UTTypeCopyPreferredTagWithClass("public.python-script", LaunchServices.kUTTagClassFilenameExtension)
        self.assertIsInstance(v, unicode)

        self.assertResultIsBOOL(LaunchServices.UTTypeEqual)
        v = LaunchServices.UTTypeEqual("public.python-script", "public.python-script")
        self.assertIs(v, True)

        self.assertResultIsBOOL(LaunchServices.UTTypeConformsTo)
        v = LaunchServices.UTTypeConformsTo("public.python-script", LaunchServices.kUTTypePlainText)
        self.assertIs(v, True)

        self.assertResultIsCFRetained(LaunchServices.UTTypeCopyDescription)
        v = LaunchServices.UTTypeCopyDescription(LaunchServices.kUTTypePlainText)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(LaunchServices.UTTypeCopyDeclaration)
        v = LaunchServices.UTTypeCopyDeclaration(LaunchServices.kUTTypePlainText)
        self.assertIsInstance(v, LaunchServices.CFDictionaryRef)

        self.assertResultIsCFRetained(LaunchServices.UTTypeCopyDeclaringBundleURL)
        v = LaunchServices.UTTypeCopyDeclaringBundleURL(LaunchServices.kUTTypePlainText)
        self.assertIsInstance(v, LaunchServices.CFURLRef)

        self.assertResultIsCFRetained(LaunchServices.UTCreateStringForOSType)
        v = LaunchServices.UTCreateStringForOSType(24353)
        self.assertIsInstance(v, unicode)

        v = LaunchServices.UTGetOSTypeFromString(v)
        self.assertEqual(v, 24353)

    @min_os_level('10.10')
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(LaunchServices.UTTypeCopyAllTagsWithClass)
        v = LaunchServices.UTTypeCopyAllTagsWithClass(LaunchServices.kUTTypeArchive, LaunchServices.kUTTagClassFilenameExtension)
        self.assertIsInstance(v, (LaunchServices.CFArrayRef, type(None)))

        self.assertResultIsBOOL(LaunchServices.UTTypeConformsTo)
        v = LaunchServices.UTTypeIsDeclared("public.python-script")
        self.assertTrue(v in (True, False))

        self.assertResultIsBOOL(LaunchServices.UTTypeIsDynamic)
        v = LaunchServices.UTTypeIsDynamic("public.python-script")
        self.assertTrue(v in (True, False))


if __name__ == "__main__":
    main()
