"""
SecurityInterface doesn't add 'interesting' behaviour, just check that the
module loaded correctly.
"""

import unittest

import os

if os.path.exists('/System/Library/Frameworks/SecurityInterface.framework'):
    import objc


    class SITest (unittest.TestCase):
        def testClasses(self):
            # Check that we loaded the SecurityInterface framework by looking
            # for a class that should exist
            import SecurityInterface

            self.assert_(hasattr(SecurityInterface, 'SFAuthorizationView'))
            self.assert_(hasattr(SecurityInterface, 'SFAuthorizationView'))

            self.assert_(isinstance(SecurityInterface.SFAuthorization, objc.objc_class))

            self.assert_(isinstance(SecurityInterface.SFAuthorization, objc.objc_class))


if __name__ == "__main__":
    unittest.main()
