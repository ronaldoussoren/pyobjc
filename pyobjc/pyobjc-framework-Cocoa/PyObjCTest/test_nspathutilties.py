from PyObjCTools.TestSupport import *

from objc import *
from Foundation import *

class TestNSPathUtilities(TestCase):
    def testSearchPaths(self):
        self.assert_( 
                NSSearchPathForDirectoriesInDomains( NSAllLibrariesDirectory, NSAllDomainsMask, NO ),
                      "NSSearchPathForDirectoriesInDomains() failed to return anything." )

        self.failUnlessArgIsBOOL(NSSearchPathForDirectoriesInDomains, 2)

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
        self.failUnless(isinstance(s, unicode))

        s = NSFullUserName()
        self.failUnless(isinstance(s, unicode))

        s = NSHomeDirectory()
        self.failUnless(isinstance(s, unicode))

        s = NSHomeDirectoryForUser('root')
        self.failUnless(isinstance(s, unicode))

        s = NSTemporaryDirectory()
        self.failUnless(isinstance(s, unicode))

        s = NSOpenStepRootDirectory()
        self.failUnless(isinstance(s, unicode))

    def testConstants(self):
        self.assertEquals(NSApplicationDirectory, 1)
        self.assertEquals(NSDemoApplicationDirectory, 2)
        self.assertEquals(NSDeveloperApplicationDirectory, 3)
        self.assertEquals(NSAdminApplicationDirectory, 4)
        self.assertEquals(NSLibraryDirectory, 5)
        self.assertEquals(NSDeveloperDirectory, 6)
        self.assertEquals(NSUserDirectory, 7)
        self.assertEquals(NSDocumentationDirectory, 8)
        self.assertEquals(NSDocumentDirectory, 9)
        self.assertEquals(NSCoreServiceDirectory, 10)
        self.assertEquals(NSDesktopDirectory, 12)
        self.assertEquals(NSCachesDirectory, 13)
        self.assertEquals(NSApplicationSupportDirectory, 14)
        self.assertEquals(NSDownloadsDirectory, 15)
        self.assertEquals(NSAllApplicationsDirectory, 100)
        self.assertEquals(NSAllLibrariesDirectory, 101)

        self.assertEquals(NSUserDomainMask, 1)
        self.assertEquals(NSLocalDomainMask, 2)
        self.assertEquals(NSNetworkDomainMask, 4)
        self.assertEquals(NSSystemDomainMask, 8)
        self.assertEquals(NSAllDomainsMask, 0x0ffff)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSString.isAbsolutePath)
        self.failUnlessArgIsOut(NSString.completePathIntoString_caseSensitive_matchesIntoArray_filterTypes_, 0)
        self.failUnlessArgIsBOOL(NSString.completePathIntoString_caseSensitive_matchesIntoArray_filterTypes_, 1)
        self.failUnlessArgIsOut(NSString.completePathIntoString_caseSensitive_matchesIntoArray_filterTypes_, 2)
        self.failUnlessResultIsBOOL(NSString.getFileSystemRepresentation_maxLength_)
        self.failUnlessArgHasType(NSString.getFileSystemRepresentation_maxLength_, 0, 'o^' + objc._C_CHAR_AS_TEXT)
        self.failUnlessArgSizeInArg(NSString.getFileSystemRepresentation_maxLength_, 0, 1)

if __name__ == '__main__':
    main( )
