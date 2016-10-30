
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSColorList (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSColorListDidChangeNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSColorList.isEditable)
        self.assertResultIsBOOL(NSColorList.writeToFile_)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(NSColorList.writeToURL_error_)
        self.assertArgIsOut(NSColorList.writeToURL_error_, 1)

if __name__ == "__main__":
    main()
