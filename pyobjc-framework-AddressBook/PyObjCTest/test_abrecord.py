
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABRecord (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(ABRecord.setValue_forProperty_error_)
        self.assertArgIsOut(ABRecord.setValue_forProperty_error_, 2)

    def testMethods(self):
        self.assertResultIsBOOL(ABRecord.setValue_forProperty_)
        self.assertResultIsBOOL(ABRecord.removeValueForProperty_)
        self.assertResultIsBOOL(ABRecord.isReadOnly)

if __name__ == "__main__":
    main()
