from AddressBook import *
from PyObjCTools.TestSupport import *


class TestABActionHelper(NSObject):
    def shouldEnableActionForPerson_identifier_(self, person, identifier):
        return True


class TestABActions(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(
            TestABActionHelper.shouldEnableActionForPerson_identifier_
        )


if __name__ == "__main__":
    main()
