from Foundation import *
from PyObjCTools.TestSupport import *

class TestArchiver (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSInconsistentArchiveException, unicode))

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSArchiver.archiveRootObject_toFile_)
        self.failUnlessResultIsBOOL(NSUnarchiver.isAtEnd)


if __name__ == "__main__":
    main()
