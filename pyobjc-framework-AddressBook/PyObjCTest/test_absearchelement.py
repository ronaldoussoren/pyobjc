
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABSearchElement (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(ABSearchElement.matchesRecord_)

if __name__ == "__main__":
    main()
