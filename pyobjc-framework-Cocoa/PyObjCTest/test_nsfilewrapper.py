from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSFileWrapper (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSFileWrapper.writeToFile_atomically_updateFilenames_)
        self.failUnlessArgIsBOOL(NSFileWrapper.writeToFile_atomically_updateFilenames_, 1)
        self.failUnlessArgIsBOOL(NSFileWrapper.writeToFile_atomically_updateFilenames_, 2)

        self.failUnlessResultIsBOOL(NSFileWrapper.isRegularFile)
        self.failUnlessResultIsBOOL(NSFileWrapper.isDirectory)
        self.failUnlessResultIsBOOL(NSFileWrapper.isSymbolicLink)
        self.failUnlessResultIsBOOL(NSFileWrapper.needsToBeUpdatedFromPath_)
        self.failUnlessResultIsBOOL(NSFileWrapper.updateFromPath_)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(NSFileWrapperReadingImmediate, 1<<0)
        self.failUnlessEqual(NSFileWrapperReadingWithoutMapping, 1<<1)
        self.failUnlessEqual(NSFileWrapperWritingAtomic, 1<<0)
        self.failUnlessEqual(NSFileWrapperWritingWithNameUpdating, 1<<1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessArgIsOut(NSFileWrapper.initWithURL_options_error_, 2)
        self.failUnlessResultIsBOOL(NSFileWrapper.matchesContentsOfURL_)
        self.failUnlessResultIsBOOL(NSFileWrapper.readFromURL_options_error_)
        self.failUnlessArgIsOut(NSFileWrapper.readFromURL_options_error_, 2)

        self.failUnlessResultIsBOOL(NSFileWrapper.writeToURL_options_originalContentsURL_error_)
        self.failUnlessArgIsOut(NSFileWrapper.writeToURL_options_originalContentsURL_error_, 3)

if __name__ == "__main__":
    main()
