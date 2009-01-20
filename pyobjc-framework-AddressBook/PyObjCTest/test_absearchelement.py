
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABSearchElement (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(ABSearchElement.matchesRecord_)

if __name__ == "__main__":
    main()
