from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSPropertyList (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSPropertyListSerialization.propertyList_isValidForFormat_)
        self.failUnlessArgIsOut(NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_, 2)
        self.failUnlessArgIsOut(NSPropertyListSerialization.propertyListFromData_mutabilityOption_format_errorDescription_, 3)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessArgIsOut(NSPropertyListSerialization.dataWithPropertyList_format_options_error_, 3)
        self.failUnlessArgIsOut(NSPropertyListSerialization.writePropertyList_toStream_format_options_error_, 4)
        self.failUnlessArgIsOut(NSPropertyListSerialization.propertyListWithData_options_format_error_, 3)
        self.failUnlessArgIsOut(NSPropertyListSerialization.propertyListWithStream_options_format_error_, 3)

if __name__ == "__main__":
    main()
