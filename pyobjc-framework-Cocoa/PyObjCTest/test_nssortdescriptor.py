from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSSortDescriptor (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(NSSortDescriptor.initWithKey_ascending_, 1)
        self.assertArgIsBOOL(NSSortDescriptor.initWithKey_ascending_selector_, 1)
        self.assertArgIsSEL(NSSortDescriptor.initWithKey_ascending_selector_, 2, b'i@:@')

        self.assertResultIsBOOL(NSSortDescriptor.ascending)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsBOOL(NSSortDescriptor.sortDescriptorWithKey_ascending_, 1)
        self.assertArgIsBOOL(NSSortDescriptor.sortDescriptorWithKey_ascending_selector_, 1)

        self.assertArgIsBOOL(NSSortDescriptor.sortDescriptorWithKey_ascending_comparator_, 1)
        self.assertArgIsBlock(NSSortDescriptor.sortDescriptorWithKey_ascending_comparator_, 2, b'i@@')
        self.assertArgIsBOOL(NSSortDescriptor.initWithKey_ascending_comparator_, 1)
        self.assertArgIsBlock(NSSortDescriptor.initWithKey_ascending_comparator_, 2, b'i@@')
        self.assertResultIsBlock(NSSortDescriptor.comparator, b'i@@')


if __name__ == "__main__":
    main()
