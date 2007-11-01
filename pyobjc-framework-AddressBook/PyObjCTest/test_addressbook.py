import unittest
import objc
import AddressBook

class TestAddressBook (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(AddressBook, 'ABPerson') )
        self.assert_( isinstance(AddressBook.ABPerson, objc.objc_class) )
        self.assert_( hasattr(AddressBook, 'ABPersonRef') )
        self.assert_( AddressBook.ABPersonRef is AddressBook.ABPerson )

        self.assert_( hasattr(AddressBook, 'ABAddressBook') )
        self.assert_( isinstance(AddressBook.ABAddressBook, objc.objc_class) )
        self.assert_( hasattr(AddressBook, 'ABAddressBookRef') )
        self.assert_( AddressBook.ABAddressBookRef is AddressBook.ABAddressBook )

        self.assert_( hasattr(AddressBook, 'ABGroup') )
        self.assert_( isinstance(AddressBook.ABGroup, objc.objc_class) )
        self.assert_( hasattr(AddressBook, 'ABGroupRef') )
        self.assert_( AddressBook.ABGroupRef is AddressBook.ABGroup)

        self.assert_( hasattr(AddressBook, 'ABMultiValue') )
        self.assert_( isinstance(AddressBook.ABMultiValue, objc.objc_class) )
        self.assert_( hasattr(AddressBook, 'ABMultiValueRef') )
        self.assert_( AddressBook.ABMultiValueRef is AddressBook.ABMultiValue)

        self.assert_( hasattr(AddressBook, 'ABMutableMultiValue') )
        self.assert_( isinstance(AddressBook.ABMutableMultiValue, objc.objc_class) )
        self.assert_( hasattr(AddressBook, 'ABMutableMultiValueRef') )
        self.assert_( AddressBook.ABMutableMultiValueRef is AddressBook.ABMutableMultiValue)

        self.assert_( hasattr(AddressBook, 'ABSearchElement') )
        self.assert_( isinstance(AddressBook.ABSearchElement, objc.objc_class) )
        self.assert_( hasattr(AddressBook, 'ABSearchElementRef') )
        self.assert_( AddressBook.ABSearchElementRef is AddressBook.ABSearchElement)

        self.assert_( hasattr(AddressBook, 'ABPeoplePickerView') )
        self.assert_( isinstance(AddressBook.ABPeoplePickerView, objc.objc_class) )
        self.assert_( hasattr(AddressBook, 'ABPickerRef') )
        self.assert_( AddressBook.ABPickerRef is AddressBook.ABPeoplePickerView)

    def testValues(self):
        self.assert_( hasattr(AddressBook, 'kABShowAsMask') )
        self.assert_( isinstance(AddressBook.kABShowAsMask, (int, long)) )
        self.assertEquals(AddressBook.kABShowAsMask, 7)

        self.assert_( hasattr(AddressBook, 'kABPickerSingleValueSelection') )
        self.assert_( isinstance(AddressBook.kABPickerSingleValueSelection, (int, long)) )
        self.assertEquals(AddressBook.kABPickerSingleValueSelection, 1)

        self.assert_( hasattr(AddressBook, 'ABMultipleValueSelection') )
        self.assert_( isinstance(AddressBook.ABMultipleValueSelection, (int, long)) )
        self.assertEquals(AddressBook.ABMultipleValueSelection, 2)

        self.assert_( hasattr(AddressBook, 'kABMultiIntegerProperty') )
        self.assert_( isinstance(AddressBook.kABMultiIntegerProperty, (int, long)) )
        self.assertEquals(AddressBook.kABMultiIntegerProperty, AddressBook.kABMultiValueMask|AddressBook.kABIntegerProperty)

    def testVariables(self):
        self.assert_( hasattr(AddressBook, 'kABUIDProperty') )
        self.assert_( isinstance(AddressBook.kABUIDProperty, unicode) )

        self.assert_( hasattr(AddressBook, 'kABEmailWorkLabel') )
        self.assert_( isinstance(AddressBook.kABEmailWorkLabel, unicode) )

        self.assert_( hasattr(AddressBook, 'kABInsertedRecords') )
        self.assert_( isinstance(AddressBook.kABInsertedRecords, unicode) )

    def testFunctions(self):
        self.assert_( hasattr(AddressBook, 'ABRecordIsReadOnly') )


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
        
    def testFourCharCodes(self):
        self.assert_( hasattr(AddressBook, 'kEventClassABPeoplePicker'))
        self.assert_( isinstance(AddressBook.kEventClassABPeoplePicker, (int, long)))
        # XXX: This is not quite what I had expected, but for some reason 4 
        # character codes are always interpreted as a bigendian number by
        # the compiler.
        self.assertEquals(AddressBook.kEventClassABPeoplePicker, 1633841264)

if __name__ == "__main__":
    unittest.main()
