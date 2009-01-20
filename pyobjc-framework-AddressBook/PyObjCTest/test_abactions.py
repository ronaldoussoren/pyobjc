
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABActionHelper (NSObject):
    def shouldEnableActionForPerson_identifier_(self, person, identifier):
        return True

class TestABActions (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(TestABActionHelper.shouldEnableActionForPerson_identifier_)

if __name__ == "__main__":
    main()
