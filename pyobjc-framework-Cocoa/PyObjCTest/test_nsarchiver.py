from Foundation import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str

class TestArchiver (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSInconsistentArchiveException, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSArchiver.archiveRootObject_toFile_)
        self.assertResultIsBOOL(NSUnarchiver.isAtEnd)


if __name__ == "__main__":
    main()
