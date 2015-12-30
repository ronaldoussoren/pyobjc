from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABPersonPicker (TestCase):
    @min_os_level('10.9')
    @onlyOn64Bit
    def testMethods_10_9(self):
        m = ABPersonPicker.showRelativeToRect_ofView_preferredEdge_
        self.assertArgHasType(m, 0, NSRect.__typestr__)


if __name__ == "__main__":
    main()
