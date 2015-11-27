from PyObjCTools.TestSupport import *
from InstantMessage import *

class TestIMControl (TestCase):
    @min_os_level('10.6')
    def testMethods(self):
        self.assertArgIsSEL(IMAVControl.setAction_, 0, b'v@:@')
        self.assertResultIsBOOL(IMAVControl.isEnabled)
        self.assertArgIsBOOL(IMAVControl.setEnabled_, 0)

if __name__ == "__main__":
    main()
