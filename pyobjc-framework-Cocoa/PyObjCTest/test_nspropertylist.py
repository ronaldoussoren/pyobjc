from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSPropertyList (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSPropertyListSerialization.propertyList_isValidForFormat_)
        self.failUnlessArgIsOut(NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_, 2)
        self.failUnlessArgIsOut(NSPropertyListSerialization.propertyListFromData_mutabilityOption_format_errorDescription_, 3)

if __name__ == "__main__":
    main()
