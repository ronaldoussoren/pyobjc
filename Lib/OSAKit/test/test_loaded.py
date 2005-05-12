"""
OSAKit doesn't add 'interesting' behaviour, just check that the
module loaded correctly.
"""

import unittest
import objc

class Test (unittest.TestCase):

    def testConstants(self):
        import OSAKit

        self.assert_(hasattr(OSAKit, 'OSASupportsCompiling'))
        self.assert_(isinstance(OSAKit.OSASupportsCompiling, (int, long)))

        self.assert_(hasattr(OSAKit, 'OSAScriptErrorMessage'))
        self.assert_(isinstance(OSAKit.OSAScriptErrorMessage, unicode))

    def testClasses(self):
        import OSAKit

        # Check that we loaded the AddressBook framework by looking for a
        # class that should exist
        self.assert_(hasattr(OSAKit, 'OSAScript'))
        self.assert_(isinstance(OSAKit.OSAScript, objc.objc_class))

if __name__ == "__main__":
    unittest.main()
