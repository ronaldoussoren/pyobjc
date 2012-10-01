
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSNib (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSNibOwner, unicode)
        self.assertIsInstance(NSNibTopLevelObjects, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSNib.instantiateNibWithOwner_topLevelObjects_)
        self.assertArgIsOut(NSNib.instantiateNibWithOwner_topLevelObjects_, 1)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(NSNib.instantiateWithOwner_topLevelObjects_)
        self.assertArgIsOut(NSNib.instantiateWithOwner_topLevelObjects_, 1)


if __name__ == "__main__":
    main()
