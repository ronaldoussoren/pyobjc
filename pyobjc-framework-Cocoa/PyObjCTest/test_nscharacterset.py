from PyObjCTools.TestSupport import *

from Foundation import *


try:
    long
except NameError:
    long = int

class TestNSCharacterSet (TestCase):
    def testConstants(self):
        self.assertEqual( NSOpenStepUnicodeReservedBase, 0xF400 )

    def testMethods(self):
        self.assertResultIsBOOL(NSCharacterSet.characterIsMember_)
        self.assertResultIsBOOL(NSCharacterSet.longCharacterIsMember_)
        self.assertResultIsBOOL(NSCharacterSet.isSupersetOfSet_)
        self.assertResultIsBOOL(NSCharacterSet.hasMemberInPlane_)

if __name__ == "__main__":
    main()
