from PyObjCTools.TestSupport import *
import AddressBook
import objc

class TestABImageClientHelper (AddressBook.NSObject):
    def consumeImageData_forTag_(self, a, b): pass

class TestABImageLoading (TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AddressBook.ABPerson.setImageData_)
        self.assertArgHasType(TestABImageClientHelper.consumeImageData_forTag_, 1, objc._C_NSInteger)

    def testProtocols(self):
        objc.protocolNamed('ABImageClient')



if __name__ == "__main__":
    main()
