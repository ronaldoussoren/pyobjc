from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNSaveRequest(TestCase):
    @min_os_level("12.3")
    def testMethods12_3(self):
        self.assertResultIsBOOL(Contacts.CNSaveRequest.shouldRefetchContacts)
        self.assertArgIsBOOL(Contacts.CNSaveRequest.setShouldRefetchContacts_, 0)
