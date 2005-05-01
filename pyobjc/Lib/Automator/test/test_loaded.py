"""
Automator doesn't add 'interesting' behaviour, just check that the
module loaded correctly.
"""

import unittest
import objc

class Test (unittest.TestCase):

    def testClasses(self):
        import Automator

        # Check that we loaded the AddressBook framework by looking for a
        # class that should exist
        self.assert_(hasattr(Automator, 'AMAction'))
        self.assert_(isinstance(Automator.AMAction, objc.objc_class))

if __name__ == "__main__":
    unittest.main()
