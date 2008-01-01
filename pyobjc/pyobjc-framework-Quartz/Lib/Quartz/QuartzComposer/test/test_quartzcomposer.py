'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import QuartzComposer

class TestQuartzComposer (unittest.TestCase):
    def testClasses(self):
        pass
        # self.assert_( hasattr(QuartzComposer, 'CLASSNAME') )
        # self.assert_( isinstance(QuartzComposer.CLASSNAME, objc.objc_class) )
        # Tollfree CF-type:
        # self.assert_( hasattr(QuartzComposer, 'CLASSNAMERef') )
        # self.assert_( QuartzComposer.CLASSNAMERef is QuartzComposer.CLASSNAME )

        # Not-tollfree CF-type:
        # self.assert_( hasattr(QuartzComposer, 'CLASSNAMERef') )
        # self.assert_( issubclass(QuartzComposer.CLASSNAMERef, objc.lookUpClass('NSCFType')) )
        # self.assert_( QuartzComposer.CLASSNAMERef is not objc.lookUpClass('NSCFType') )

    def testValues(self):
        # Use this to test for a number of enum and #define values
        pass

        # Integer values:
        # self.assert_( hasattr(QuartzComposer, 'CONSTANT') )
        # self.assert_( isinstance(QuartzComposer.CONSTANT, (int, long)) )
        # self.assertEquals(QuartzComposer.CONSTANT, 7)

        # String values:
        # self.assert_( hasattr(QuartzComposer, 'CONSTANT') )
        # self.assert_( isinstance(QuartzComposer.CONSTANT, (str, unicode)) )
        # self.assertEquals(QuartzComposer.CONSTANT, 'value')

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        pass

        # self.assert_( hasattr(QuartzComposer, 'CONSTANT') )
        # self.assert_( isinstance(QuartzComposer.CONSTANT, unicode) )

    def testFunctions(self):
        # Use this to test for functions
        pass

        # self.assert_( hasattr(QuartzComposer, 'FUNCTION') )

    def testOpaque(self):
        # Use this to test for opaque pointers
        pass

        # self.assert_( hasattr(QuartzComposer, 'OPAQUE') )

    def testProtocols(self):
        # Use this to test if informal protocols  are present
        pass

        # self.assert_( hasattr(QuartzComposer, 'protocols') )

        # self.assert_( hasattr(QuartzComposer.protocols, 'PROTOCOL') )
        # self.assert_( isinstance(QuartzComposer.protocols.PROTOCOL, objc.informal_protocol) )

    def test_structs(self):
        # Use this to test struct wrappers
        pass

        # self.assert_( hasattr(QuartzComposer, 'STRUCT') )
        # o = QuartzComposer.STRUCT()
        # self.assert_( hasattr(o, 'FIELD_NAME') )



if __name__ == "__main__":
    unittest.main()

