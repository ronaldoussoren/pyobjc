from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSFileWrapper (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSFileWrapper.writeToFile_atomically_updateFilenames_)
        self.assertArgIsBOOL(NSFileWrapper.writeToFile_atomically_updateFilenames_, 1)
        self.assertArgIsBOOL(NSFileWrapper.writeToFile_atomically_updateFilenames_, 2)

        self.assertResultIsBOOL(NSFileWrapper.isRegularFile)
        self.assertResultIsBOOL(NSFileWrapper.isDirectory)
        self.assertResultIsBOOL(NSFileWrapper.isSymbolicLink)
        self.assertResultIsBOOL(NSFileWrapper.needsToBeUpdatedFromPath_)
        self.assertResultIsBOOL(NSFileWrapper.updateFromPath_)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSFileWrapperReadingImmediate, 1<<0)
        self.assertEqual(NSFileWrapperReadingWithoutMapping, 1<<1)
        self.assertEqual(NSFileWrapperWritingAtomic, 1<<0)
        self.assertEqual(NSFileWrapperWritingWithNameUpdating, 1<<1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsOut(NSFileWrapper.initWithURL_options_error_, 2)
        self.assertResultIsBOOL(NSFileWrapper.matchesContentsOfURL_)
        self.assertResultIsBOOL(NSFileWrapper.readFromURL_options_error_)
        self.assertArgIsOut(NSFileWrapper.readFromURL_options_error_, 2)

        self.assertResultIsBOOL(NSFileWrapper.writeToURL_options_originalContentsURL_error_)
        self.assertArgIsOut(NSFileWrapper.writeToURL_options_originalContentsURL_error_, 3)

if __name__ == "__main__":
    main()
