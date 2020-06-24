from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNContactFetchRequest(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(Contacts.CNContactFetchRequest.mutableObjects)
        self.assertArgIsBOOL(Contacts.CNContactFetchRequest.setMutableObjects_, 0)

        self.assertResultIsBOOL(Contacts.CNContactFetchRequest.unifyResults)
        self.assertArgIsBOOL(Contacts.CNContactFetchRequest.setUnifyResults_, 0)
