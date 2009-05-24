from CoreFoundation import *
from PyObjCTools.TestSupport import *


class TestCFBundle (TestCase):

    def testTypes(self):
        self.failUnlessIsCFType(CFBundleRef)

    def testMainBundle(self):
        bundle = CFBundleGetMainBundle()
        self.failUnless( isinstance(bundle, CFBundleRef) )

    def testBundleLoader(self):
        bundle = CFBundleGetBundleWithIdentifier(u"com.apple.CoreFoundation")
        self.failUnless( isinstance(bundle, CFBundleRef) )

        array = list(CFBundleGetAllBundles())
        self.failUnless(len(array) != 0)
        for b in array:
            self.failUnless( isinstance(b, CFBundleRef) )


        url = CFURLCreateWithFileSystemPath(None, u"/System/Library/Frameworks/Foundation.framework", kCFURLPOSIXPathStyle, True)
        bundle = CFBundleCreate(None, url)
        self.failUnless( isinstance(bundle, CFBundleRef) )

        url = CFURLCreateWithFileSystemPath(None, u"/System/Library/Frameworks", kCFURLPOSIXPathStyle, True)
        array = CFBundleCreateBundlesFromDirectory(None, url, u"frameworkX")
        self.assertEquals(len(array), 0)

        array = CFBundleCreateBundlesFromDirectory(None, url, u"framework")
        self.assertNotEquals(len(array), 0)

        array = CFBundleCreateBundlesFromDirectory(None, url, None)
        self.assertNotEquals(len(array), 0)



    def testTypeID(self):
        v = CFBundleGetTypeID()
        self.failUnless( isinstance(v, (int, long)) )

        
    def testInspection(self):
        bundle = CFBundleGetBundleWithIdentifier(u"com.apple.CoreFoundation")
        self.failUnless( isinstance(bundle, CFBundleRef) )

        url = CFBundleCopyBundleURL(bundle)
        self.failUnless( isinstance(url, CFURLRef) )

        v = CFBundleGetValueForInfoDictionaryKey(bundle, u"CFBundleIdentifier")
        self.failUnless(v == u"com.apple.CoreFoundation")

        v = CFBundleGetInfoDictionary(bundle)
        self.failUnless( isinstance(v, CFDictionaryRef) )
        self.failUnless( v['CFBundleIdentifier'], 'com.apple.CoreFoundation')

        v = CFBundleGetLocalInfoDictionary(bundle)
        self.failUnless( v is None or isinstance(v, CFDictionaryRef) )

        type, creator = CFBundleGetPackageInfo(bundle, None, None)
        self.failUnless(isinstance(type, (int, long)))
        self.failUnless(isinstance(creator, (int, long)))

        identifier = CFBundleGetIdentifier(bundle)
        self.failUnless( identifier == u'com.apple.CoreFoundation')

        v = CFBundleGetVersionNumber(bundle)
        self.failUnless( isinstance(v, (int, long)))

        v = CFBundleGetDevelopmentRegion(bundle)
        self.failUnless( isinstance(v, unicode))

        v = CFBundleCopySupportFilesDirectoryURL(bundle)
        self.failUnless( v is None or isinstance(v, CFURLRef) )

        v = CFBundleCopyResourcesDirectoryURL(bundle)
        self.failUnless( v is None or isinstance(v, CFURLRef) )

        v = CFBundleCopyPrivateFrameworksURL(bundle)
        self.failUnless( v is None or isinstance(v, CFURLRef) )

        v = CFBundleCopySharedFrameworksURL(bundle)
        self.failUnless( v is None or isinstance(v, CFURLRef) )

        v = CFBundleCopySharedSupportURL(bundle)
        self.failUnless( v is None or isinstance(v, CFURLRef) )

        v = CFBundleCopyBuiltInPlugInsURL(bundle)
        self.failUnless( v is None or isinstance(v, CFURLRef) )

    def testDirectAccess(self):
        url = CFURLCreateWithFileSystemPath(None, u"/System/Library/Frameworks/Foundation.framework", kCFURLPOSIXPathStyle, True)

        v = CFBundleCopyInfoDictionaryInDirectory(url)
        self.failUnless( isinstance(v, CFDictionaryRef) )
        self.failUnless( v[u"CFBundleIdentifier"] == u"com.apple.Foundation")

        ok, type, creator = CFBundleGetPackageInfoInDirectory(url, None, None)
        self.failUnless(ok is True)
        self.failUnless(isinstance(type, (int, long)))
        self.failUnless(isinstance(creator, (int, long)))

    def testResources(self):
        url = CFURLCreateWithFileSystemPath(None, u"/System/Library/Frameworks/Foundation.framework", kCFURLPOSIXPathStyle, True)
        bundle = CFBundleCreate(None, url)
        self.failUnless( isinstance(bundle, CFBundleRef) )

        url = CFURLCreateWithFileSystemPath(None, u"/System/Library/Frameworks/Tcl.framework", kCFURLPOSIXPathStyle, True)
        bundle2 = CFBundleCreate(None, url)
        self.failUnless( isinstance(bundle2, CFBundleRef) )


        url = CFBundleCopyResourceURL(bundle, "Formatter", "strings", None)
        self.failUnless( isinstance(url, CFURLRef) )

        url = CFBundleCopyResourceURL(bundle, "Formatter", "strings", "dummy")
        self.failUnless(url is None)

        array = CFBundleCopyResourceURLsOfType(bundle, "strings", None)
        self.failIf(array is None)
        self.failUnless(isinstance(array, CFArrayRef))

        val = CFBundleCopyLocalizedString(bundle, "Err640.f", "value", "FoundationErrors")
        self.failUnless(isinstance(val, unicode))
        self.failIf(val == "value")

        CFCopyLocalizedString("python", "error")
        CFCopyLocalizedStringFromTable("pyobjc", "python", "error")
        CFCopyLocalizedStringFromTableInBundle("pyobjc", "python", bundle, "comment")
        CFCopyLocalizedStringWithDefaultValue("pyobjc", "python", bundle, "default", "comment")

        array = CFBundleCopyBundleLocalizations(bundle)
        self.failIf(array is None)
        self.failUnless(isinstance(array, CFArrayRef))

        arr2 = CFBundleCopyPreferredLocalizationsFromArray(array)
        self.failIf(arr2 is None)
        self.failUnless(isinstance(arr2, CFArrayRef))

        arr2 = CFBundleCopyLocalizationsForPreferences(array, None)
        self.failIf(arr2 is None)
        self.failUnless(isinstance(arr2, CFArrayRef))

        url = CFBundleCopyResourceURLForLocalization(bundle, "Formatter", "strings", None, "Dutch");
        self.failUnless( isinstance(url, CFURLRef) )

        array = CFBundleCopyResourceURLsOfTypeForLocalization(bundle, "strings", None, "Dutch")
        self.failIf(array is None)
        self.failUnless(isinstance(array, CFArrayRef))

        url = CFBundleCopyExecutableURL(bundle)
        self.failUnless( isinstance(url, CFURLRef) )

        array = CFBundleCopyExecutableArchitectures(bundle)
        self.failIf(array is None)
        self.failUnless(isinstance(array, CFArrayRef))

        self.failUnlessArgIsOut(CFBundlePreflightExecutable, 1)
        ok, error = CFBundlePreflightExecutable(bundle, None)
        self.failUnless((ok is True) or (ok is False))
        if ok:
            self.failUnless(error is None)
        else:
            self.failUnless(isinstance(error, CFErrorRef))

        self.failUnlessArgIsOut(CFBundleLoadExecutableAndReturnError, 1)
        ok, error = CFBundleLoadExecutableAndReturnError(bundle2, None)
        self.failUnless((ok is True) or (ok is False))
        if ok:
            self.failUnless(error is None)
        else:
            self.failUnless(isinstance(error, CFErrorRef))

        ok = CFBundleLoadExecutable(bundle2)
        self.failUnless(ok)

        ok = CFBundleIsExecutableLoaded(bundle2)
        self.failUnless(ok)

        CFBundleUnloadExecutable(bundle2)
        ok = CFBundleIsExecutableLoaded(bundle2)
        #self.failIf(ok)
        ok = CFBundleLoadExecutable(bundle2)
        self.failUnless(ok)

        try:
            CFBundleGetFunctionPointerForName
        except NameError:
            pass
        else:
            self.fail("CFBundleGetFunctionPointerForName")

        try:
            CFBundleGetFunctionPointersForNames
        except NameError:
            pass
        else:
            self.fail("CFBundleGetFunctionPointersForNames")

        try:
            CFBundleGetDataPointerForName
        except NameError:
            pass
        else:
            self.fail("CFBundleGetDataPointerForName")

        try:
            CFBundleGetDataPointersForNames
        except NameError:
            pass
        else:
            self.fail("CFBundleGetDataPointersForNames")

        url =  CFBundleCopyAuxiliaryExecutableURL(bundle, "Foundation")
        self.failUnless( isinstance(url, CFURLRef) )

        id = CFBundleOpenBundleResourceMap(bundle)
        self.failUnless(isinstance(id, (int, long)))

        CFBundleCloseBundleResourceMap(bundle, id)

        err,  id1, id2 = CFBundleOpenBundleResourceFiles(bundle, None, None)
        self.failUnless(isinstance(err, (int, long)))
        self.failUnless(isinstance(id1, (int, long)))
        self.failUnless(isinstance(id2, (int, long)))
        if id1 != -1:
            CFBundleCloseBundleResourceMap(bundle, id1)
        if id2 != -1:
            CFBundleCloseBundleResourceMap(bundle, id2)

    def testResourcesDirect(self):
        bundle = CFURLCreateWithFileSystemPath(None, u"/System/Library/Frameworks/Foundation.framework", kCFURLPOSIXPathStyle, True)
        url = CFBundleCopyResourceURLInDirectory(bundle, "Formatter", "strings", None)
        self.failUnless( isinstance(url, CFURLRef) )

        array = CFBundleCopyResourceURLsOfTypeInDirectory(bundle, "strings", None)
        self.failIf(array is None)
        self.failUnless(isinstance(array, CFArrayRef))

        infoDict = CFBundleCopyInfoDictionaryForURL(bundle)
        self.failUnless(isinstance(infoDict, CFDictionaryRef))

        array = CFBundleCopyLocalizationsForURL(bundle)
        self.failUnless(isinstance(array, CFArrayRef))

        array = CFBundleCopyExecutableArchitecturesForURL(bundle)
        self.failUnless(isinstance(array, CFArrayRef))
        for a in array:
            self.failUnless(isinstance(a, (int, long)))
   
    def testPlugin(self):
        url = CFURLCreateWithFileSystemPath(None, u"/System/Library/Components/AppleScript.component", kCFURLPOSIXPathStyle, True)
        bundle = CFBundleCreate(None, url)
        self.failUnless( isinstance(bundle, CFBundleRef) )

        ref = CFBundleGetPlugIn(bundle)
        self.failUnless(ref is None)



    def testConstants(self):
        self.failUnless( isinstance(kCFBundleInfoDictionaryVersionKey, unicode))
        self.failUnless( isinstance(kCFBundleExecutableKey, unicode))
        self.failUnless( isinstance(kCFBundleIdentifierKey, unicode))
        self.failUnless( isinstance(kCFBundleVersionKey, unicode))
        self.failUnless( isinstance(kCFBundleDevelopmentRegionKey, unicode))
        self.failUnless( isinstance(kCFBundleNameKey, unicode))
        self.failUnless( isinstance(kCFBundleLocalizationsKey, unicode))

        self.failUnless( kCFBundleExecutableArchitectureI386     == 0x00000007)
        self.failUnless( kCFBundleExecutableArchitecturePPC      == 0x00000012)
        self.failUnless( kCFBundleExecutableArchitectureX86_64   == 0x01000007)
        self.failUnless( kCFBundleExecutableArchitecturePPC64    == 0x01000012)



if __name__ == "__main__":
    main()
