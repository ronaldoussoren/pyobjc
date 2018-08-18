
from PyObjCTools.TestSupport import *
import CoreServices

class TestUTType (TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreServices.kUTExportedTypeDeclarationsKey, unicode)
        self.assertIsInstance(CoreServices.kUTImportedTypeDeclarationsKey, unicode)
        self.assertIsInstance(CoreServices.kUTTypeIdentifierKey, unicode)
        self.assertIsInstance(CoreServices.kUTTypeTagSpecificationKey, unicode)
        self.assertIsInstance(CoreServices.kUTTypeConformsToKey, unicode)
        self.assertIsInstance(CoreServices.kUTTypeDescriptionKey, unicode)
        self.assertIsInstance(CoreServices.kUTTypeIconFileKey, unicode)
        self.assertIsInstance(CoreServices.kUTTypeReferenceURLKey, unicode)
        self.assertIsInstance(CoreServices.kUTTypeVersionKey, unicode)
        self.assertIsInstance(CoreServices.kUTTagClassFilenameExtension, unicode)
        self.assertIsInstance(CoreServices.kUTTagClassMIMEType, unicode)
        self.assertIsInstance(CoreServices.kUTTagClassNSPboardType, unicode)
        self.assertIsInstance(CoreServices.kUTTagClassOSType, unicode)

    def testFunctions(self):
        self.assertResultIsCFRetained(CoreServices.UTTypeCreatePreferredIdentifierForTag)
        v = CoreServices.UTTypeCreatePreferredIdentifierForTag(CoreServices.kUTTagClassFilenameExtension, "py", CoreServices.kUTTypePlainText)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(CoreServices.UTTypeCreateAllIdentifiersForTag)
        v = CoreServices.UTTypeCreateAllIdentifiersForTag(CoreServices.kUTTagClassFilenameExtension, "py", CoreServices.kUTTypePlainText)
        self.assertIsInstance(v, CoreServices.CFArrayRef)
        self.assertGreaterEqual(len(v), 1)
        self.assertIsInstance(v[0], unicode)

        self.assertResultIsCFRetained(CoreServices.UTTypeCopyPreferredTagWithClass)
        v = CoreServices.UTTypeCopyPreferredTagWithClass("public.python-script", CoreServices.kUTTagClassFilenameExtension)
        self.assertIsInstance(v, unicode)

        self.assertResultIsBOOL(CoreServices.UTTypeEqual)
        v = CoreServices.UTTypeEqual("public.python-script", "public.python-script")
        self.assertIs(v, True)

        self.assertResultIsBOOL(CoreServices.UTTypeConformsTo)
        v = CoreServices.UTTypeConformsTo("public.python-script", CoreServices.kUTTypePlainText)
        self.assertIs(v, True)

        self.assertResultIsCFRetained(CoreServices.UTTypeCopyDescription)
        v = CoreServices.UTTypeCopyDescription(CoreServices.kUTTypePlainText)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(CoreServices.UTTypeCopyDeclaration)
        v = CoreServices.UTTypeCopyDeclaration(CoreServices.kUTTypePlainText)
        self.assertIsInstance(v, CoreServices.CFDictionaryRef)

        self.assertResultIsCFRetained(CoreServices.UTTypeCopyDeclaringBundleURL)
        v = CoreServices.UTTypeCopyDeclaringBundleURL(CoreServices.kUTTypePlainText)
        self.assertIsInstance(v, CoreServices.CFURLRef)

        self.assertResultIsCFRetained(CoreServices.UTCreateStringForOSType)
        v = CoreServices.UTCreateStringForOSType(24353)
        self.assertIsInstance(v, unicode)

        v = CoreServices.UTGetOSTypeFromString(v)
        self.assertEqual(v, 24353)

    @min_os_level('10.10')
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(CoreServices.UTTypeCopyAllTagsWithClass)
        v = CoreServices.UTTypeCopyAllTagsWithClass(CoreServices.kUTTypeArchive, CoreServices.kUTTagClassFilenameExtension)
        self.assertIsInstance(v, (CoreServices.CFArrayRef, type(None)))

        self.assertResultIsBOOL(CoreServices.UTTypeConformsTo)
        v = CoreServices.UTTypeIsDeclared("public.python-script")
        self.assertTrue(v in (True, False))

        self.assertResultIsBOOL(CoreServices.UTTypeIsDynamic)
        v = CoreServices.UTTypeIsDynamic("public.python-script")
        self.assertTrue(v in (True, False))


if __name__ == "__main__":
    main()
