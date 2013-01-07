
from PyObjCTools.TestSupport import *
from LaunchServices import *

try:
    unicode
except NameError:
    unicode = str

class TestUTType (TestCase):
    def testConstants(self):
        self.assertIsInstance(kUTExportedTypeDeclarationsKey, unicode)
        self.assertIsInstance(kUTImportedTypeDeclarationsKey, unicode)
        self.assertIsInstance(kUTTypeIdentifierKey, unicode)
        self.assertIsInstance(kUTTypeTagSpecificationKey, unicode)
        self.assertIsInstance(kUTTypeConformsToKey, unicode)
        self.assertIsInstance(kUTTypeDescriptionKey, unicode)
        self.assertIsInstance(kUTTypeIconFileKey, unicode)
        self.assertIsInstance(kUTTypeReferenceURLKey, unicode)
        self.assertIsInstance(kUTTypeVersionKey, unicode)
        self.assertIsInstance(kUTTagClassFilenameExtension, unicode)
        self.assertIsInstance(kUTTagClassMIMEType, unicode)
        self.assertIsInstance(kUTTagClassNSPboardType, unicode)
        self.assertIsInstance(kUTTagClassOSType, unicode)

    def testFunctions(self):
        self.assertResultIsCFRetained(UTTypeCreatePreferredIdentifierForTag)
        v = UTTypeCreatePreferredIdentifierForTag(kUTTagClassFilenameExtension, "py", kUTTypePlainText)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(UTTypeCreateAllIdentifiersForTag)
        v = UTTypeCreateAllIdentifiersForTag(kUTTagClassFilenameExtension, "py", kUTTypePlainText)
        self.assertIsInstance(v, CFArrayRef)
        self.assertGreaterEqual(len(v), 1)
        self.assertIsInstance(v[0], unicode)

        self.assertResultIsCFRetained(UTTypeCopyPreferredTagWithClass)
        v = UTTypeCopyPreferredTagWithClass("public.python-script", kUTTagClassFilenameExtension)
        self.assertIsInstance(v, unicode)

        self.assertResultIsBOOL(UTTypeEqual)
        v = UTTypeEqual("public.python-script", "public.python-script")
        self.assertIs(v, True)

        self.assertResultIsBOOL(UTTypeConformsTo)
        v = UTTypeConformsTo("public.python-script", kUTTypePlainText)
        self.assertIs(v, True)

        self.assertResultIsCFRetained(UTTypeCopyDescription)
        v = UTTypeCopyDescription(kUTTypePlainText)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(UTTypeCopyDeclaration)
        v = UTTypeCopyDeclaration(kUTTypePlainText)
        self.assertIsInstance(v, CFDictionaryRef)

        self.assertResultIsCFRetained(UTTypeCopyDeclaringBundleURL)
        v = UTTypeCopyDeclaringBundleURL(kUTTypePlainText)
        self.assertIsInstance(v, CFURLRef)

        self.assertResultIsCFRetained(UTCreateStringForOSType)
        v = UTCreateStringForOSType(24353)
        self.assertIsInstance(v, unicode)

        v = UTGetOSTypeFromString(v)
        self.assertEqual(v, 24353)





if __name__ == "__main__":
    main()
