from PyObjCTools.TestSupport import *
import objc
import AddressBook

class TestAddressBook (TestCase):
    def testNoTypedefs(self):
        # Just in case: the following is a typedef not a function definition
        self.assert_( not hasattr(AddressBook, 'ABActionGetPropertyCallback') )

    def testOpaque(self):
        self.assert_( hasattr(AddressBook, 'ABPickerRef') )

        # Supporting this would require C code, but that won't happen as
        # this type basically just C-glue around an Objective-C class which is
        # available:
        self.assert_( not hasattr(AddressBook, 'ABActionCallbacks') )

    def testProtocols (self):
        self.assert_( hasattr(AddressBook, 'protocols') )
        self.assert_( hasattr(AddressBook.protocols, 'ABActionDelegate') )
        self.assert_( isinstance(AddressBook.protocols.ABActionDelegate, objc.informal_protocol) )
        

if __name__ == "__main__":
    main()
