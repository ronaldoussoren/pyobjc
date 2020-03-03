import AddressBook
from PyObjCTools.TestSupport import TestCase


class TestABGroup(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AddressBook.ABGroup.addMember_)
        self.assertResultIsBOOL(AddressBook.ABGroup.removeMember_)
        self.assertResultIsBOOL(AddressBook.ABGroup.addSubgroup_)
        self.assertResultIsBOOL(AddressBook.ABGroup.removeSubgroup_)
        self.assertResultIsBOOL(
            AddressBook.ABGroup.setDistributionIdentifier_forProperty_person_
        )
