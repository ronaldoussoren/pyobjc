
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABRecord (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(ABRecord.setValue_forProperty_)
        self.assertResultIsBOOL(ABRecord.removeValueForProperty_)
        self.assertResultIsBOOL(ABRecord.isReadOnly)

if __name__ == "__main__":
    main()
