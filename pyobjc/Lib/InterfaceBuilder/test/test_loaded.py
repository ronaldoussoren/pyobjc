"""
InterfaceBuilder doesn't add 'interesting' behaviour, just check that the
module loaded correctly.
"""

import unittest
import objc

class IBTest (unittest.TestCase):

    def testConstants(self):
        import InterfaceBuilder

        self.assert_(hasattr(InterfaceBuilder, 'kPaletteResource'))

        self.assertEquals(InterfaceBuilder.kPaletteResource, 2)

    def testClasses(self):
        import InterfaceBuilder

        # Check that we loaded the InterfaceBuilder framework by looking for a
        # class that should exist
        self.assert_(hasattr(InterfaceBuilder, 'IBContainerView'))
        self.assert_(isinstance(InterfaceBuilder.IBContainerView, objc.objc_class))

if __name__ == "__main__":
    unittest.main()
