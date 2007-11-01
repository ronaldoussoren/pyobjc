'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
from Quartz import ImageKit

class TestImageKit (unittest.TestCase):
    def testClasses(self):
        pass
        # self.assert_( hasattr(ImageKit, 'CLASSNAME') )
        # self.assert_( isinstance(ImageKit.CLASSNAME, objc.objc_class) )
        # Tollfree CF-type:
        # self.assert_( hasattr(ImageKit, 'CLASSNAMERef') )
        # self.assert_( ImageKit.CLASSNAMERef is ImageKit.CLASSNAME )

        # Not-tollfree CF-type:
        # self.assert_( hasattr(ImageKit, 'CLASSNAMERef') )
        # self.assert_( issubclass(ImageKit.CLASSNAMERef, objc.lookUpClass('NSCFType')) )
        # self.assert_( ImageKit.CLASSNAMERef is not objc.lookUpClass('NSCFType') )

    def testValues(self):
        # Use this to test for a number of enum and #define values
        pass

        # Integer values:
        # self.assert_( hasattr(ImageKit, 'CONSTANT') )
        # self.assert_( isinstance(ImageKit.CONSTANT, (int, long)) )
        # self.assertEquals(ImageKit.CONSTANT, 7)

        # String values:
        # self.assert_( hasattr(ImageKit, 'CONSTANT') )
        # self.assert_( isinstance(ImageKit.CONSTANT, (str, unicode)) )
        # self.assertEquals(ImageKit.CONSTANT, 'value')

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        pass

        # self.assert_( hasattr(ImageKit, 'CONSTANT') )
        # self.assert_( isinstance(ImageKit.CONSTANT, unicode) )

    def testFunctions(self):
        # Use this to test for functions
        pass

        # self.assert_( hasattr(ImageKit, 'FUNCTION') )

    def testOpaque(self):
        # Use this to test for opaque pointers
        pass

        # self.assert_( hasattr(ImageKit, 'OPAQUE') )

    def testProtocols(self):
        # Use this to test if informal protocols  are present
        pass

        # self.assert_( hasattr(ImageKit, 'protocols') )

        # self.assert_( hasattr(ImageKit.protocols, 'PROTOCOL') )
        # self.assert_( isinstance(ImageKit.protocols.PROTOCOL, objc.informal_protocol) )

    def test_structs(self):
        # Use this to test struct wrappers
        pass

        # self.assert_( hasattr(ImageKit, 'STRUCT') )
        # o = ImageKit.STRUCT()
        # self.assert_( hasattr(o, 'FIELD_NAME') )



if __name__ == "__main__":
    unittest.main()

