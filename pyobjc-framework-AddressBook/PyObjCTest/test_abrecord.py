
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABRecord (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(ABRecord.setValue_forProperty_)
        self.failUnlessResultIsBOOL(ABRecord.removeValueForProperty_)
        self.failUnlessResultIsBOOL(ABRecord.isReadOnly)

if __name__ == "__main__":
    main()
