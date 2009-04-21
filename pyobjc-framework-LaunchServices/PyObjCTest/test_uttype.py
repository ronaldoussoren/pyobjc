
from PyObjCTools.TestSupport import *
from LaunchServices import *

class TestUTType (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kUTExportedTypeDeclarationsKey, unicode)
        self.failUnlessIsInstance(kUTImportedTypeDeclarationsKey, unicode)
        self.failUnlessIsInstance(kUTTypeIdentifierKey, unicode)
        self.failUnlessIsInstance(kUTTypeTagSpecificationKey, unicode)
        self.failUnlessIsInstance(kUTTypeConformsToKey, unicode)
        self.failUnlessIsInstance(kUTTypeDescriptionKey, unicode)
        self.failUnlessIsInstance(kUTTypeIconFileKey, unicode)
        self.failUnlessIsInstance(kUTTypeReferenceURLKey, unicode)
        self.failUnlessIsInstance(kUTTypeVersionKey, unicode)
        self.failUnlessIsInstance(kUTTagClassFilenameExtension, unicode)
        self.failUnlessIsInstance(kUTTagClassMIMEType, unicode)
        self.failUnlessIsInstance(kUTTagClassNSPboardType, unicode)
        self.failUnlessIsInstance(kUTTagClassOSType, unicode)

    def testFunctions(self):
        self.failUnlessResultIsCFRetained(UTTypeCreatePreferredIdentifierForTag)
        v = UTTypeCreatePreferredIdentifierForTag(kUTTagClassFilenameExtension, "py", kUTTypePlainText)
        self.failUnlessIsInstance(v, unicode)

        self.failUnlessResultIsCFRetained(UTTypeCreateAllIdentifiersForTag)
        v = UTTypeCreateAllIdentifiersForTag(kUTTagClassFilenameExtension, "py", kUTTypePlainText)
        self.failUnlessIsInstance(v, CFArrayRef)
        self.failUnless(len(v) >= 1)
        self.failUnlessIsInstance(v[0], unicode)

        self.failUnlessResultIsCFRetained(UTTypeCopyPreferredTagWithClass)
        v = UTTypeCopyPreferredTagWithClass("public.python-script", kUTTagClassFilenameExtension)
        self.failUnlessIsInstance(v, unicode)

        self.failUnlessResultIsBOOL(UTTypeEqual)
        v = UTTypeEqual("public.python-script", "public.python-script")
        self.failUnless(v is True)

        self.failUnlessResultIsBOOL(UTTypeConformsTo)
        v = UTTypeConformsTo("public.python-script", kUTTypePlainText)
        self.failUnless(v is True)

        self.failUnlessResultIsCFRetained(UTTypeCopyDescription)
        v = UTTypeCopyDescription(kUTTypePlainText)
        self.failUnlessIsInstance(v, unicode)

        self.failUnlessResultIsCFRetained(UTTypeCopyDeclaration)
        v = UTTypeCopyDeclaration(kUTTypePlainText)
        self.failUnlessIsInstance(v, CFDictionaryRef)

        self.failUnlessResultIsCFRetained(UTTypeCopyDeclaringBundleURL)
        v = UTTypeCopyDeclaringBundleURL(kUTTypePlainText)
        self.failUnlessIsInstance(v, CFURLRef)

        self.failUnlessResultIsCFRetained(UTCreateStringForOSType)
        v = UTCreateStringForOSType(24353)
        self.failUnlessIsInstance(v, unicode)

        v = UTGetOSTypeFromString(v)
        self.failUnlessEqual(v, 24353)
        




if __name__ == "__main__":
    main()
