from PyObjCTools.TestSupport import *

from objc import *
from Foundation import *

try:
    unicode
except NameError:
    unicode = str

class TestNSPathUtilities(TestCase):
    def testSearchPaths(self):
        self.assert_(
                NSSearchPathForDirectoriesInDomains( NSAllLibrariesDirectory, NSAllDomainsMask, NO ),
                      "NSSearchPathForDirectoriesInDomains() failed to return anything." )

        self.assertArgIsBOOL(NSSearchPathForDirectoriesInDomains, 2)

    def testTrue(self):
        for boolVal in (1, 1==1, YES, -1):
            self.assert_(
                NSSearchPathForDirectoriesInDomains(NSLibraryDirectory,NSUserDomainMask, boolVal)[0][0] == '/', boolVal)

    def testFalse(self):
        for boolVal in (0, 1!=1, NO):
            self.assert_(
                NSSearchPathForDirectoriesInDomains(NSLibraryDirectory,NSUserDomainMask, boolVal)[0][0] != '/', boolVal)

    def testFunctions(self):
        s = NSUserName()
        self.assertIsInstance(s, unicode)
        s = NSFullUserName()
        self.assertIsInstance(s, unicode)
        s = NSHomeDirectory()
        self.assertIsInstance(s, unicode)
        s = NSHomeDirectoryForUser('root')
        self.assertIsInstance(s, unicode)
        s = NSTemporaryDirectory()
        self.assertIsInstance(s, unicode)
        s = NSOpenStepRootDirectory()
        self.assertIsInstance(s, unicode)

    def testConstants(self):
        self.assertEqual(NSApplicationDirectory, 1)
        self.assertEqual(NSDemoApplicationDirectory, 2)
        self.assertEqual(NSDeveloperApplicationDirectory, 3)
        self.assertEqual(NSAdminApplicationDirectory, 4)
        self.assertEqual(NSLibraryDirectory, 5)
        self.assertEqual(NSDeveloperDirectory, 6)
        self.assertEqual(NSUserDirectory, 7)
        self.assertEqual(NSDocumentationDirectory, 8)
        self.assertEqual(NSDocumentDirectory, 9)
        self.assertEqual(NSCoreServiceDirectory, 10)
        self.assertEqual(NSDesktopDirectory, 12)
        self.assertEqual(NSCachesDirectory, 13)
        self.assertEqual(NSApplicationSupportDirectory, 14)
        self.assertEqual(NSDownloadsDirectory, 15)
        self.assertEqual(NSAllApplicationsDirectory, 100)
        self.assertEqual(NSAllLibrariesDirectory, 101)

        self.assertEqual(NSUserDomainMask, 1)
        self.assertEqual(NSLocalDomainMask, 2)
        self.assertEqual(NSNetworkDomainMask, 4)
        self.assertEqual(NSSystemDomainMask, 8)
        self.assertEqual(NSAllDomainsMask, 0x0ffff)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSAutosavedInformationDirectory, 11)

        self.assertEqual(NSInputMethodsDirectory, 16)
        self.assertEqual(NSMoviesDirectory, 17)
        self.assertEqual(NSMusicDirectory, 18)
        self.assertEqual(NSPicturesDirectory, 19)
        self.assertEqual(NSPrinterDescriptionDirectory, 20)
        self.assertEqual(NSSharedPublicDirectory, 21)
        self.assertEqual(NSPreferencePanesDirectory, 22)
        self.assertEqual(NSItemReplacementDirectory, 99)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(NSApplicationScriptsDirectory, 23)
        self.assertEqual(NSTrashDirectory, 102)

    def testMethods(self):
        self.assertResultIsBOOL(NSString.isAbsolutePath)
        self.assertArgIsOut(NSString.completePathIntoString_caseSensitive_matchesIntoArray_filterTypes_, 0)
        self.assertArgIsBOOL(NSString.completePathIntoString_caseSensitive_matchesIntoArray_filterTypes_, 1)
        self.assertArgIsOut(NSString.completePathIntoString_caseSensitive_matchesIntoArray_filterTypes_, 2)
        self.assertResultIsBOOL(NSString.getFileSystemRepresentation_maxLength_)
        self.assertArgHasType(NSString.getFileSystemRepresentation_maxLength_, 0, b'o^' + objc._C_CHAR_AS_TEXT)
        self.assertArgSizeInArg(NSString.getFileSystemRepresentation_maxLength_, 0, 1)

if __name__ == '__main__':
    main( )
