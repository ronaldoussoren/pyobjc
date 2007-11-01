'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import Collaboration

class TestCollaboration (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(Collaboration, 'CBIdentity') )
        self.assert_( isinstance(Collaboration.CBIdentity, objc.objc_class) )
        self.assert_( hasattr(Collaboration, 'CBGroupIdentity') )
        self.assert_( isinstance(Collaboration.CBGroupIdentity, objc.objc_class) )
        self.assert_( hasattr(Collaboration, 'CBIdentityPicker') )
        self.assert_( isinstance(Collaboration.CBIdentityPicker, objc.objc_class) )




if __name__ == "__main__":
    unittest.main()

