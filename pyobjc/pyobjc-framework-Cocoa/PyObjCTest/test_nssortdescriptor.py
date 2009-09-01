from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSSortDescriptor (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSSortDescriptor.initWithKey_ascending_, 1)
        self.failUnlessArgIsBOOL(NSSortDescriptor.initWithKey_ascending_selector_, 1)
        self.failUnlessArgIsSEL(NSSortDescriptor.initWithKey_ascending_selector_, 2, 'i@:@')

        self.failUnlessResultIsBOOL(NSSortDescriptor.ascending)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessArgIsBOOL(NSSortDescriptor.sortDescriptorWithKey_ascending_, 1)
        self.failUnlessArgIsBOOL(NSSortDescriptor.sortDescriptorWithKey_ascending_selector_, 1)

        self.failUnlessArgIsBOOL(NSSortDescriptor.sortDescriptorWithKey_ascending_comparator_, 1)
        self.failUnlessArgIsBlock(NSSortDescriptor.sortDescriptorWithKey_ascending_comparator_, 2, 'i@@')
        self.failUnlessArgIsBOOL(NSSortDescriptor.initWithKey_ascending_comparator_, 1)
        self.failUnlessArgIsBlock(NSSortDescriptor.initWithKey_ascending_comparator_, 2, 'i@@')
        self.failUnlessResultIsBlock(NSSortDescriptor.comparator, 'i@@')


if __name__ == "__main__":
    main()
