"""
AddressBook doesn't add 'interesting' behaviour, just check that the
module loaded correctly.
"""

import unittest, sys, os
import objc

class ABTest (unittest.TestCase):

    def testConstants(self):
        import AddressBook

        # Test one string and one integer, to check if the constant-extraction
        # script worked.
        self.assert_(hasattr(AddressBook, 'kABMultiDictionaryProperty'))
        self.assert_(hasattr(AddressBook, 'kABPhoneMainLabel'))

        self.assertEquals(AddressBook.kABMultiDictionaryProperty, 262)
        self.assertEquals(AddressBook.kABPhoneMainLabel, '_$!<Main>!$_')

        # 10.3 and later
        if sys.platform == 'darwin' and os.uname()[2] >= '7.':
            self.assert_(hasattr(AddressBook, 'kABShowAsMask'))
            self.assert_(isinstance(AddressBook.kABShowAsMask, (int, long)))
        

    def testClasses(self):
        import AddressBook

        # Check that we loaded the AddressBook framework by looking for a
        # class that should exist
        self.assert_(hasattr(AddressBook, 'ABPerson'))
        self.assert_(isinstance(AddressBook.ABPerson, objc.objc_class))

if __name__ == "__main__":
    unittest.main()
