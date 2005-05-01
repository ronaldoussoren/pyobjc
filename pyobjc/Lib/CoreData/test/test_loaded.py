"""
CoreData doesn't add 'interesting' behaviour, just check that the
module loaded correctly.
"""

import unittest
import objc

class Test (unittest.TestCase):

    def testConstants(self):
        import CoreData

        self.assert_(hasattr(CoreData, 'NSCoreDataVersionNumber'))
        self.assert_(hasattr(CoreData, 'NSPersistentStoreInvalidTypeError'))
        self.assert_(hasattr(CoreData, 'NSDetailedErrorsKey'))

    def testClasses(self):
        import CoreData

        self.assert_(hasattr(CoreData, 'NSPropertyDescription'))
        self.assert_(isinstance(CoreData.NSPropertyDescription, objc.objc_class))

if __name__ == "__main__":
    unittest.main()
