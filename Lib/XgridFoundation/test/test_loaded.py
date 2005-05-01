"""
XgridFoundation doesn't add 'interesting' behaviour, just check that the
module loaded correctly.
"""

import unittest
import objc

class Test (unittest.TestCase):

    def testConstants(self):
        import XgridFoundation

        # Test one string and one integer, to check if the constant-extraction
        # script worked.
        self.assert_(hasattr(XgridFoundation, 'XGResourceActionSuspend'))
        self.assert_(hasattr(XgridFoundation, 'XGActionMonitorResultsOutputStreamsKey'))

    def testClasses(self):
        import XgridFoundation

        # Check that we loaded the XgridFoundation framework by looking for a
        # class that should exist
        self.assert_(hasattr(XgridFoundation, 'XGActionMonitor'))
        self.assert_(isinstance(XgridFoundation.XGActionMonitor, objc.objc_class))

if __name__ == "__main__":
    unittest.main()
