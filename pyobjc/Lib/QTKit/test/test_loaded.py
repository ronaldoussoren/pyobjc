"""
QTKit doesn't add 'interesting' behaviour, just check that the
module loaded correctly.
"""

import unittest
import objc

class Test (unittest.TestCase):

    def testConstants(self):
        import QTKit

        self.assert_(hasattr(QTKit, 'kQTTimeIsIndefinite'))
        self.assert_(isinstance(QTKit.kQTTimeIsIndefinite, (int, long)))

        self.assert_(hasattr(QTKit, 'QTMediaTypeVideo'))
        self.assert_(isinstance(QTKit.QTMediaTypeVideo, unicode))

    def testClasses(self):
        import QTKit

        # Check that we loaded the AddressBook framework by looking for a
        # class that should exist
        self.assert_(hasattr(QTKit, 'QTDataReference'))
        self.assert_(isinstance(QTKit.QTDataReference, objc.objc_class))

    def testFunctions(self):
        import QTKit

        self.assert_(hasattr(QTKit, 'QTStringForOSType'))
        self.assert_(callable(QTKit.QTStringForOSType))

if __name__ == "__main__":
    unittest.main()
