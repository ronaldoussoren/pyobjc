from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSearchField (TestCase):
    @min_os_level('10.10')
    def testMethods(self):
        self.assertResultIsBOOL(NSSearchField.sendsWholeSearchString)
        self.assertArgIsBOOL(NSSearchField.setSendsWholeSearchString_, 0)
        self.assertResultIsBOOL(NSSearchField.sendsSearchStringImmediately)
        self.assertArgIsBOOL(NSSearchField.setSendsSearchStringImmediately_, 0)

if __name__ == "__main__":
    main()
