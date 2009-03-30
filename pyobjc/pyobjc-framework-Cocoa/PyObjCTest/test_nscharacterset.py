from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSCharacterSet (TestCase):
    def testConstants(self):
        self.assertEquals( NSOpenStepUnicodeReservedBase, 0xF400 )

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSCharacterSet.characterIsMember_)
        self.failUnlessResultIsBOOL(NSCharacterSet.longCharacterIsMember_)
        self.failUnlessResultIsBOOL(NSCharacterSet.isSupersetOfSet_)
        self.failUnlessResultIsBOOL(NSCharacterSet.hasMemberInPlane_)

if __name__ == "__main__":
    main()
