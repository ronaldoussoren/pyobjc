import unittest
import objc

import AppKit

import os
ON_JAGUAR=((os.uname()[0] == 'Darwin') and (int(os.uname()[2][0]) <= '6'))

class TestNSFont(unittest.TestCase):
    def matrixEquals(self, value1, value2):
        self.assertEquals(len(value1), len(value2))
        for v1, v2 in zip(value1, value2):
            # This should probably be 'assertAlmostEquals'
            self.assertEquals(v1, v2)

    def testConstants(self):
        self.assert_(hasattr(AppKit, 'NSFontIdentityMatrix'))

        if AppKit.NSFontIdentityMatrix is None:
            # MacOSX
            return

        self.assertEquals(AppKit.NSFontIdentityMatrix, (1.0, 0.0, 0.0, 1.0, 0.0, 0.0))

    def testMatrixMethods(self):
        o = AppKit.NSFont.boldSystemFontOfSize_(10);
        m = o.matrix()
        self.assert_(isinstance(m, tuple))
        self.assertEquals(len(m), 6)

        nm = o.fontName()

        if not ON_JAGUAR:
            # Don't test this on Jaguar, see Radar #3421569.
            o = AppKit.NSFont.fontWithName_matrix_(
                    nm, AppKit.NSFontIdentityMatrix)
            self.assert_(o is not None)

            m = o.matrix()
            self.assert_(isinstance(m, tuple))
            self.assertEquals(len(m), 6)

            self.matrixEquals(m, (1.0, 0.0, 0.0, 1.0, 0.0, 0.0))

        # For some reason Tiger transforms this matrix to the one below. The
        # same thing happens in pure ObjC code.
        #o = AppKit.NSFont.fontWithName_matrix_(nm, (1.0, 2.0, 3.0, 4.0, 5.0, 6.0))
        o = AppKit.NSFont.fontWithName_matrix_(nm, (12.0, 0.0, 0.0, 12.0, 0.0, 0.0))
        self.assert_(o is not None)

        m = o.matrix()
        self.assert_(isinstance(m, tuple))
        self.assertEquals(len(m), 6)

        #self.matrixEquals(m, (1.0, 2.0, 3.0, 4.0, 5.0, 6.0))
        self.matrixEquals(m, (12.0, 0.0, 0.0, 12.0, 0.0, 0.0))

        self.assertRaises(ValueError, AppKit.NSFont.fontWithName_matrix_, nm, "foo")
        self.assertRaises(ValueError, AppKit.NSFont.fontWithName_matrix_, nm, (1, 2, 3, 4))
        self.assertRaises(ValueError, AppKit.NSFont.fontWithName_matrix_, nm, (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0))




if __name__ == '__main__':
    unittest.main( )
