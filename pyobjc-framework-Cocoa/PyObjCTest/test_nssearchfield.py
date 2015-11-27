from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSearchField (TestCase):
    @min_os_level('10.10')
    def testMethods(self):
        self.assertResultIsBOOL(NSSearchField.sendsWholeSearchString)
        self.assertArgIsBOOL(NSSearchField.setSendsWholeSearchString_, 0)
        self.assertResultIsBOOL(NSSearchField.sendsSearchStringImmediately)
        self.assertArgIsBOOL(NSSearchField.setSendsSearchStringImmediately_, 0)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertArgIsBOOL(NSSearchField.rectForSearchTextWhenCentered_, 0)
        self.assertArgIsBOOL(NSSearchField.rectForSearchButtonWhenCentered_, 0)
        self.assertArgIsBOOL(NSSearchField.rectForCancelButtonWhenCentered_, 0)
        self.assertResultIsBOOL(NSSearchField.centersPlaceholder)
        self.assertArgIsBOOL(NSSearchField.setCentersPlaceholder_, 0)

    @min_sdk_level('10.11')
    def testProtocols(self):
        objc.protocolNamed('NSSearchFieldDelegate')


if __name__ == "__main__":
    main()
