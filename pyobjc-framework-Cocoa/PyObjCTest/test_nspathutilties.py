import Foundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPathUtilities(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSSearchPathDirectory)
        self.assertIsEnumType(Foundation.NSSearchPathDomainMask)

    def testSearchPaths(self):
        self.assertTrue(
            Foundation.NSSearchPathForDirectoriesInDomains(
                Foundation.NSAllLibrariesDirectory, Foundation.NSAllDomainsMask, objc.NO
            ),
            "NSSearchPathForDirectoriesInDomains() failed to return anything.",
        )

        self.assertArgIsBOOL(Foundation.NSSearchPathForDirectoriesInDomains, 2)

    def testTrue(self):
        for boolVal in (1, 1 == 1, objc.YES, -1):
            self.assertEqual(
                Foundation.NSSearchPathForDirectoriesInDomains(
                    Foundation.NSLibraryDirectory, Foundation.NSUserDomainMask, boolVal
                )[0][0],
                "/",
                boolVal,
            )

    def testFalse(self):
        for boolVal in (0, 1 != 1, objc.NO):
            self.assertNotEqual(
                Foundation.NSSearchPathForDirectoriesInDomains(
                    Foundation.NSLibraryDirectory, Foundation.NSUserDomainMask, boolVal
                )[0][0],
                "/",
                boolVal,
            )

    def testFunctions(self):
        s = Foundation.NSUserName()
        self.assertIsInstance(s, str)
        s = Foundation.NSFullUserName()
        self.assertIsInstance(s, str)
        s = Foundation.NSHomeDirectory()
        self.assertIsInstance(s, str)
        s = Foundation.NSHomeDirectoryForUser("root")
        self.assertIsInstance(s, str)
        s = Foundation.NSTemporaryDirectory()
        self.assertIsInstance(s, str)
        s = Foundation.NSOpenStepRootDirectory()
        self.assertIsInstance(s, str)

    def testConstants(self):
        self.assertEqual(Foundation.NSApplicationDirectory, 1)
        self.assertEqual(Foundation.NSDemoApplicationDirectory, 2)
        self.assertEqual(Foundation.NSDeveloperApplicationDirectory, 3)
        self.assertEqual(Foundation.NSAdminApplicationDirectory, 4)
        self.assertEqual(Foundation.NSLibraryDirectory, 5)
        self.assertEqual(Foundation.NSDeveloperDirectory, 6)
        self.assertEqual(Foundation.NSUserDirectory, 7)
        self.assertEqual(Foundation.NSDocumentationDirectory, 8)
        self.assertEqual(Foundation.NSDocumentDirectory, 9)
        self.assertEqual(Foundation.NSCoreServiceDirectory, 10)
        self.assertEqual(Foundation.NSDesktopDirectory, 12)
        self.assertEqual(Foundation.NSCachesDirectory, 13)
        self.assertEqual(Foundation.NSApplicationSupportDirectory, 14)
        self.assertEqual(Foundation.NSDownloadsDirectory, 15)
        self.assertEqual(Foundation.NSAllApplicationsDirectory, 100)
        self.assertEqual(Foundation.NSAllLibrariesDirectory, 101)

        self.assertEqual(Foundation.NSUserDomainMask, 1)
        self.assertEqual(Foundation.NSLocalDomainMask, 2)
        self.assertEqual(Foundation.NSNetworkDomainMask, 4)
        self.assertEqual(Foundation.NSSystemDomainMask, 8)
        self.assertEqual(Foundation.NSAllDomainsMask, 0x0FFFF)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Foundation.NSAutosavedInformationDirectory, 11)

        self.assertEqual(Foundation.NSInputMethodsDirectory, 16)
        self.assertEqual(Foundation.NSMoviesDirectory, 17)
        self.assertEqual(Foundation.NSMusicDirectory, 18)
        self.assertEqual(Foundation.NSPicturesDirectory, 19)
        self.assertEqual(Foundation.NSPrinterDescriptionDirectory, 20)
        self.assertEqual(Foundation.NSSharedPublicDirectory, 21)
        self.assertEqual(Foundation.NSPreferencePanesDirectory, 22)
        self.assertEqual(Foundation.NSItemReplacementDirectory, 99)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(Foundation.NSApplicationScriptsDirectory, 23)
        self.assertEqual(Foundation.NSTrashDirectory, 102)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSString.isAbsolutePath)
        self.assertArgIsOut(
            Foundation.NSString.completePathIntoString_caseSensitive_matchesIntoArray_filterTypes_,  # noqa: B950
            0,
        )
        self.assertArgIsBOOL(
            Foundation.NSString.completePathIntoString_caseSensitive_matchesIntoArray_filterTypes_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            Foundation.NSString.completePathIntoString_caseSensitive_matchesIntoArray_filterTypes_,  # noqa: B950
            2,
        )
        self.assertResultIsBOOL(
            Foundation.NSString.getFileSystemRepresentation_maxLength_
        )
        self.assertArgHasType(
            Foundation.NSString.getFileSystemRepresentation_maxLength_,
            0,
            b"o^" + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgSizeInArg(
            Foundation.NSString.getFileSystemRepresentation_maxLength_, 0, 1
        )
