'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import QuickLookUI

class TestQuickLookUI (unittest.TestCase):
    def testClasses(self):
        pass
        # self.assert_( hasattr(QuickLookUI, 'CLASSNAME') )
        # self.assert_( isinstance(QuickLookUI.CLASSNAME, objc.objc_class) )
        # Tollfree CF-type:
        # self.assert_( hasattr(QuickLookUI, 'CLASSNAMERef') )
        # self.assert_( QuickLookUI.CLASSNAMERef is QuickLookUI.CLASSNAME )

        # Not-tollfree CF-type:
        # self.assert_( hasattr(QuickLookUI, 'CLASSNAMERef') )
        # self.assert_( issubclass(QuickLookUI.CLASSNAMERef, objc.lookUpClass('NSCFType')) )
        # self.assert_( QuickLookUI.CLASSNAMERef is not objc.lookUpClass('NSCFType') )

    def testValues(self):
        # Use this to test for a number of enum and #define values
        pass

        # Integer values:
        # self.assert_( hasattr(QuickLookUI, 'CONSTANT') )
        # self.assert_( isinstance(QuickLookUI.CONSTANT, (int, long)) )
        # self.assertEquals(QuickLookUI.CONSTANT, 7)

        # String values:
        # self.assert_( hasattr(QuickLookUI, 'CONSTANT') )
        # self.assert_( isinstance(QuickLookUI.CONSTANT, (str, unicode)) )
        # self.assertEquals(QuickLookUI.CONSTANT, 'value')

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        pass

        # self.assert_( hasattr(QuickLookUI, 'CONSTANT') )
        # self.assert_( isinstance(QuickLookUI.CONSTANT, unicode) )

    def testFunctions(self):
        # Use this to test for functions
        pass

        # self.assert_( hasattr(QuickLookUI, 'FUNCTION') )

    def testOpaque(self):
        # Use this to test for opaque pointers
        pass

        # self.assert_( hasattr(QuickLookUI, 'OPAQUE') )

    def testProtocols(self):
        # Use this to test if informal protocols  are present
        pass

        # self.assert_( hasattr(QuickLookUI, 'protocols') )

        # self.assert_( hasattr(QuickLookUI.protocols, 'PROTOCOL') )
        # self.assert_( isinstance(QuickLookUI.protocols.PROTOCOL, objc.informal_protocol) )

    def test_structs(self):
        # Use this to test struct wrappers
        pass

        # self.assert_( hasattr(QuickLookUI, 'STRUCT') )
        # o = QuickLookUI.STRUCT()
        # self.assert_( hasattr(o, 'FIELD_NAME') )



if __name__ == "__main__":
    unittest.main()
