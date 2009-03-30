from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSSortDescriptor (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSSortDescriptor.initWithKey_ascending_, 1)
        self.failUnlessArgIsBOOL(NSSortDescriptor.initWithKey_ascending_selector_, 1)
        self.failUnlessArgIsSEL(NSSortDescriptor.initWithKey_ascending_selector_, 2, 'i@:@')

        self.failUnlessResultIsBOOL(NSSortDescriptor.ascending)

if __name__ == "__main__":
    main()
