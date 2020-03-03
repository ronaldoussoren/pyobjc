import AddressBook
import objc
from PyObjCTools.TestSupport import TestCase


class TestABImageClientHelper(AddressBook.NSObject):
    def consumeImageData_forTag_(self, a, b):
        pass


class TestABImageLoading(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AddressBook.ABPerson.setImageData_)
        self.assertArgHasType(
            TestABImageClientHelper.consumeImageData_forTag_, 1, objc._C_NSInteger
        )

    def testProtocols(self):
        objc.protocolNamed("ABImageClient")
