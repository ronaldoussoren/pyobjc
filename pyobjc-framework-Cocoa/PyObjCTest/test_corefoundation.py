'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import CoreFoundation

class TestCoreFoundation (TestCase):
    def testClasses(self):
        pass
        # self.assert_( hasattr(CoreFoundation, 'CLASSNAME') )
        # self.assert_( isinstance(CoreFoundation.CLASSNAME, objc.objc_class) )
        # Tollfree CF-type:
        # self.assert_( hasattr(CoreFoundation, 'CLASSNAMERef') )
        # self.assert_( CoreFoundation.CLASSNAMERef is CoreFoundation.CLASSNAME )

        # Not-tollfree CF-type:
        # self.assert_( hasattr(CoreFoundation, 'CLASSNAMERef') )
        # self.assert_( issubclass(CoreFoundation.CLASSNAMERef, objc.lookUpClass('NSCFType')) )
        # self.assert_( CoreFoundation.CLASSNAMERef is not objc.lookUpClass('NSCFType') )

    def testValues(self):
        # Use this to test for a number of enum and #define values
        pass

        # Integer values:
        # self.assert_( hasattr(CoreFoundation, 'CONSTANT') )
        # self.assert_( isinstance(CoreFoundation.CONSTANT, (int, long)) )
        # self.assertEquals(CoreFoundation.CONSTANT, 7)

        # String values:
        # self.assert_( hasattr(CoreFoundation, 'CONSTANT') )
        # self.assert_( isinstance(CoreFoundation.CONSTANT, (str, unicode)) )
        # self.assertEquals(CoreFoundation.CONSTANT, 'value')

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        pass

        # self.assert_( hasattr(CoreFoundation, 'CONSTANT') )
        # self.assert_( isinstance(CoreFoundation.CONSTANT, unicode) )

    def testFunctions(self):
        # Use this to test for functions
        pass

        # self.assert_( hasattr(CoreFoundation, 'FUNCTION') )

    def testOpaque(self):
        # Use this to test for opaque pointers
        pass

        # self.assert_( hasattr(CoreFoundation, 'OPAQUE') )

    def testProtocols(self):
        # Use this to test if informal protocols  are present
        pass

        # self.assert_( hasattr(CoreFoundation, 'protocols') )

        # self.assert_( hasattr(CoreFoundation.protocols, 'PROTOCOL') )
        # self.assert_( isinstance(CoreFoundation.protocols.PROTOCOL, objc.informal_protocol) )

    def test_structs(self):
        # Use this to test struct wrappers
        pass

        # self.assert_( hasattr(CoreFoundation, 'STRUCT') )
        # o = CoreFoundation.STRUCT()
        # self.assert_( hasattr(o, 'FIELD_NAME') )



if __name__ == "__main__":
    main()

