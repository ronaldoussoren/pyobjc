from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSJSONSerialization (TestCase):
    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSJSONReadingMutableContainers, (1 << 0))
        self.assertEqual(NSJSONReadingMutableLeaves, (1 << 1))
        self.assertEqual(NSJSONReadingAllowFragments, (1 << 2))
        self.assertEqual(NSJSONWritingPrettyPrinted, (1 << 0))

    @min_os_level('10.7')
    def testMethod10_7(self):
        self.assertResultIsBOOL(NSJSONSerialization.isValidJSONObject_)
        self.assertArgIsOut(NSJSONSerialization.dataWithJSONObject_options_error_, 2)
        self.assertArgIsOut(NSJSONSerialization.JSONObjectWithData_options_error_, 2)
        self.assertArgIsOut(NSJSONSerialization.writeJSONObject_toStream_options_error_, 3)
        self.assertArgIsOut(NSJSONSerialization.JSONObjectWithStream_options_error_, 2)

if __name__ == "__main__":
    main()
