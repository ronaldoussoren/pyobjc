from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSPropertyList (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSPropertyListSerialization.propertyList_isValidForFormat_)
        self.assertArgIsOut(NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_, 2)
        self.assertArgIsOut(NSPropertyListSerialization.propertyListFromData_mutabilityOption_format_errorDescription_, 3)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsOut(NSPropertyListSerialization.dataWithPropertyList_format_options_error_, 3)
        self.assertArgIsOut(NSPropertyListSerialization.writePropertyList_toStream_format_options_error_, 4)
        self.assertArgIsOut(NSPropertyListSerialization.propertyListWithData_options_format_error_, 3)
        self.assertArgIsOut(NSPropertyListSerialization.propertyListWithStream_options_format_error_, 3)

if __name__ == "__main__":
    main()
