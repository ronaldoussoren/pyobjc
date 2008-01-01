'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import CoreText

class TestCoreText (unittest.TestCase):
    def testClasses(self):
        pass
        # self.assert_( hasattr(CoreText, 'CLASSNAME') )
        # self.assert_( isinstance(CoreText.CLASSNAME, objc.objc_class) )
        # Tollfree CF-type:
        # self.assert_( hasattr(CoreText, 'CLASSNAMERef') )
        # self.assert_( CoreText.CLASSNAMERef is CoreText.CLASSNAME )

        # Not-tollfree CF-type:
        # self.assert_( hasattr(CoreText, 'CLASSNAMERef') )
        # self.assert_( issubclass(CoreText.CLASSNAMERef, objc.lookUpClass('NSCFType')) )
        # self.assert_( CoreText.CLASSNAMERef is not objc.lookUpClass('NSCFType') )

    def testValues(self):
        # Use this to test for a number of enum and #define values
        pass

        # Integer values:
        # self.assert_( hasattr(CoreText, 'CONSTANT') )
        # self.assert_( isinstance(CoreText.CONSTANT, (int, long)) )
        # self.assertEquals(CoreText.CONSTANT, 7)

        # String values:
        # self.assert_( hasattr(CoreText, 'CONSTANT') )
        # self.assert_( isinstance(CoreText.CONSTANT, (str, unicode)) )
        # self.assertEquals(CoreText.CONSTANT, 'value')

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        pass

        # self.assert_( hasattr(CoreText, 'CONSTANT') )
        # self.assert_( isinstance(CoreText.CONSTANT, unicode) )

    def testFunctions(self):
        # Use this to test for functions
        pass

        # self.assert_( hasattr(CoreText, 'FUNCTION') )

    def testOpaque(self):
        # Use this to test for opaque pointers
        pass

        # self.assert_( hasattr(CoreText, 'OPAQUE') )

    def testProtocols(self):
        # Use this to test if informal protocols  are present
        pass

        # self.assert_( hasattr(CoreText, 'protocols') )

        # self.assert_( hasattr(CoreText.protocols, 'PROTOCOL') )
        # self.assert_( isinstance(CoreText.protocols.PROTOCOL, objc.informal_protocol) )

    def test_structs(self):
        # Use this to test struct wrappers
        pass

        # self.assert_( hasattr(CoreText, 'STRUCT') )
        # o = CoreText.STRUCT()
        # self.assert_( hasattr(o, 'FIELD_NAME') )



if __name__ == "__main__":
    unittest.main()

