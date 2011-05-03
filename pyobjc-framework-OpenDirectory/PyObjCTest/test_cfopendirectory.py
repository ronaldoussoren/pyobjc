'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import CFOpenDirectory

class TestCFOpenDirectory (unittest.TestCase):
    def testClasses(self):
        pass
        # self.assert_( hasattr(CFOpenDirectory, 'CLASSNAME') )
        # self.assert_( isinstance(CFOpenDirectory.CLASSNAME, objc.objc_class) )
        # Tollfree CF-type:
        # self.assert_( hasattr(CFOpenDirectory, 'CLASSNAMERef') )
        # self.assert_( CFOpenDirectory.CLASSNAMERef is CFOpenDirectory.CLASSNAME )

        # Not-tollfree CF-type:
        # self.assert_( hasattr(CFOpenDirectory, 'CLASSNAMERef') )
        # self.assert_( issubclass(CFOpenDirectory.CLASSNAMERef, objc.lookUpClass('NSCFType')) )
        # self.assert_( CFOpenDirectory.CLASSNAMERef is not objc.lookUpClass('NSCFType') )

    def testValues(self):
        # Use this to test for a number of enum and #define values
        pass

        # Integer values:
        # self.assert_( hasattr(CFOpenDirectory, 'CONSTANT') )
        # self.assert_( isinstance(CFOpenDirectory.CONSTANT, (int, long)) )
        # self.assertEquals(CFOpenDirectory.CONSTANT, 7)

        # String values:
        # self.assert_( hasattr(CFOpenDirectory, 'CONSTANT') )
        # self.assert_( isinstance(CFOpenDirectory.CONSTANT, (str, unicode)) )
        # self.assertEquals(CFOpenDirectory.CONSTANT, 'value')

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        pass

        # self.assert_( hasattr(CFOpenDirectory, 'CONSTANT') )
        # self.assert_( isinstance(CFOpenDirectory.CONSTANT, unicode) )

    def testFunctions(self):
        # Use this to test for functions
        pass

        # self.assert_( hasattr(CFOpenDirectory, 'FUNCTION') )

    def testOpaque(self):
        # Use this to test for opaque pointers
        pass

        # self.assert_( hasattr(CFOpenDirectory, 'OPAQUE') )

    def testProtocols(self):
        # Use this to test if informal protocols  are present
        pass

        # self.assert_( hasattr(CFOpenDirectory, 'protocols') )

        # self.assert_( hasattr(CFOpenDirectory.protocols, 'PROTOCOL') )
        # self.assert_( isinstance(CFOpenDirectory.protocols.PROTOCOL, objc.informal_protocol) )

    def test_structs(self):
        # Use this to test struct wrappers
        pass

        # self.assert_( hasattr(CFOpenDirectory, 'STRUCT') )
        # o = CFOpenDirectory.STRUCT()
        # self.assert_( hasattr(o, 'FIELD_NAME') )



if __name__ == "__main__":
    unittest.main()

