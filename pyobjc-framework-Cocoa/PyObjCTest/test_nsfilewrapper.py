import AppKit
import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileWrapper(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSFileWrapperReadingOptions)
        self.assertIsEnumType(Foundation.NSFileWrapperWritingOptions)

    def testMethods(self):
        self.assertResultIsBOOL(
            AppKit.NSFileWrapper.writeToFile_atomically_updateFilenames_
        )
        self.assertArgIsBOOL(
            AppKit.NSFileWrapper.writeToFile_atomically_updateFilenames_, 1
        )
        self.assertArgIsBOOL(
            AppKit.NSFileWrapper.writeToFile_atomically_updateFilenames_, 2
        )

        self.assertResultIsBOOL(AppKit.NSFileWrapper.isRegularFile)
        self.assertResultIsBOOL(AppKit.NSFileWrapper.isDirectory)
        self.assertResultIsBOOL(AppKit.NSFileWrapper.isSymbolicLink)
        self.assertResultIsBOOL(AppKit.NSFileWrapper.needsToBeUpdatedFromPath_)
        self.assertResultIsBOOL(AppKit.NSFileWrapper.updateFromPath_)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(AppKit.NSFileWrapperReadingImmediate, 1 << 0)
        self.assertEqual(AppKit.NSFileWrapperReadingWithoutMapping, 1 << 1)
        self.assertEqual(AppKit.NSFileWrapperWritingAtomic, 1 << 0)
        self.assertEqual(AppKit.NSFileWrapperWritingWithNameUpdating, 1 << 1)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsOut(AppKit.NSFileWrapper.initWithURL_options_error_, 2)
        self.assertResultIsBOOL(AppKit.NSFileWrapper.matchesContentsOfURL_)
        self.assertResultIsBOOL(AppKit.NSFileWrapper.readFromURL_options_error_)
        self.assertArgIsOut(AppKit.NSFileWrapper.readFromURL_options_error_, 2)

        self.assertResultIsBOOL(
            AppKit.NSFileWrapper.writeToURL_options_originalContentsURL_error_
        )
        self.assertArgIsOut(
            AppKit.NSFileWrapper.writeToURL_options_originalContentsURL_error_, 3
        )
