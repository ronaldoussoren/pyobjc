"""
AppleScriptKit doesn't add 'interesting' behaviour, just check that the
module loaded correctly.
"""

import unittest
import objc

class Test (unittest.TestCase):

    def testClasses(self):
        import AppleScriptKit

        # Check that we loaded the AddressBook framework by looking for a
        # class that should exist
        self.assert_(hasattr(AppleScriptKit, 'ASKPluginObject'))
        self.assert_(isinstance(AppleScriptKit.ASKPluginObject, objc.objc_class))

if __name__ == "__main__":
    unittest.main()
