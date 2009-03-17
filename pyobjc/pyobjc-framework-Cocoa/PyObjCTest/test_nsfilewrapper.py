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

if __name__ == "__main__":
    main()
