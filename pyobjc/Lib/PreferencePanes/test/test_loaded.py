"""
PreferencePanes doesn't add 'interesting' behaviour, just check that the 
module loaded correctly.
"""

import unittest
import objc

class PPTest (unittest.TestCase):


    def testClasses(self):
        import PreferencePanes

        # Check that we loaded the PreferencePanes framework by looking for a
        # class that should exist
        self.assert_(hasattr(PreferencePanes, 'NSPreferencePane'))
        self.assert_(isinstance(PreferencePanes.NSPreferencePane, objc.objc_class))

if __name__ == "__main__":
    unittest.main()
