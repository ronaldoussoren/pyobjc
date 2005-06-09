"""
SenTestingKit doesn't add 'interesting' behaviour, just check that the
module loaded correctly.
"""

import unittest

import os
import objc

if os.path.exists('/System/Library/Frameworks/SenTestingKit.framework'):
    class SenTestingKitTests (unittest.TestCase):

        def testConstants(self):
            import SenTestingKit

            self.assert_(hasattr(SenTestingKit, 'SenTestFailureException'))

            self.assert_(isinstance(SenTestingKit.SenTestFailureException, unicode))

        def testClasses(self):
            # Check that we loaded the SenTestingKit framework by looking for a
            # class that should exist
            import SenTestingKit

            self.assert_(hasattr(SenTestingKit, 'SenInterfaceTestCase'))
            self.assert_(isinstance(SenTestingKit.SenInterfaceTestCase, objc.objc_class))


if __name__ == "__main__":
    unittest.main()
