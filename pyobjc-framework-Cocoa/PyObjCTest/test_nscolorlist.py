
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSColorList (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSColorListDidChangeNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSColorList.isEditable)
        self.assertResultIsBOOL(NSColorList.writeToFile_)

if __name__ == "__main__":
    main()
