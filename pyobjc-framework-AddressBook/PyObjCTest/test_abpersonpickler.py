from PyObjCTools.TestSupport import *
from AddressBook import *

try:
    long
except NameError:
    long = int

try:
    unicode
except NameError:
    unicode = str

class TestABPersonPicker (TestCase):
    @min_os_level('10.9')
    def testMethods_10.9(self):
        m = ABPersonPicker.showRelativeToRect_ofView_preferredEdge_
        self.assertArgHasType(m, 0, NSRect.__typestr__)


if __name__ == "__main__":
    main()
