"""
SyncServices doesn't add 'interesting' behaviour, just check that the
module loaded correctly.
"""

import unittest
import objc

class Test (unittest.TestCase):

    def testConstants(self):
        import SyncServices

        self.assert_(hasattr(SyncServices, 'ISyncChangeTypeAdd'))

    def testClasses(self):
        import SyncServices

        self.assert_(hasattr(SyncServices, 'ISyncChange'))
        self.assert_(isinstance(SyncServices.ISyncChange, objc.objc_class))

if __name__ == "__main__":
    unittest.main()
