from PyObjCTools.TestSupport import *
import objc
import AddressBook

class TestAddressBook (TestCase):
    def testNoTypedefs(self):
        # Just in case: the following is a typedef not a function definition
        self.assert_( not hasattr(AddressBook, 'ABActionGetPropertyCallback') )

    def testOpaque(self):
        self.assertTrue(hasattr(AddressBook, 'ABPickerRef'))

        # Supporting this would require C code, but that won't happen as
        # this type basically just C-glue around an Objective-C class which is
        # available:
        self.assertFalse(hasattr(AddressBook, 'ABActionCallbacks'))

    def testProtocols (self):
        self.assertFalse( hasattr(AddressBook, 'protocols') )


if __name__ == "__main__":
    main()
