"""
ExceptionHandling doesn't add 'interesting' behaviour, just check that the
module loaded correctly.
"""

import unittest
import objc

class EHTest (unittest.TestCase):


    def testClasses(self):
        import ExceptionHandling

        # Check that we loaded the PreferencePanes framework by looking for a
        # class that should exist
        self.assert_(hasattr(ExceptionHandling, 'NSExceptionHandler'))
        self.assert_(isinstance(ExceptionHandling.NSExceptionHandler, objc.objc_class))

if __name__ == "__main__":
    unittest.main()
