"""
ScreenSaver doesn't add 'interesting' behaviour, just check that the 
module loaded correctly.
"""

import unittest
import ScreenSaver
import objc

class SSTest (unittest.TestCase):

    def testClasses(self):
        # Check that we loaded the ScreenSaver framework by looking for a
        # class that should exist
        self.assert_(hasattr(ScreenSaver, 'ScreenSaverView'))
        self.assert_(isinstance(ScreenSaver.ScreenSaverView, objc.objc_class))

if __name__ == "__main__":
    unittest.main()
