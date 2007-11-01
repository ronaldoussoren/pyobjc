'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import QTKit

class TestQTKit (unittest.TestCase):
    def testClasses(self):
        pass
        # self.assert_( hasattr(QTKit, 'CLASSNAME') )
        # self.assert_( isinstance(QTKit.CLASSNAME, objc.objc_class) )
        # Tollfree CF-type:
        # self.assert_( hasattr(QTKit, 'CLASSNAMERef') )
        # self.assert_( QTKit.CLASSNAMERef is QTKit.CLASSNAME )

        # Not-tollfree CF-type:
        # self.assert_( hasattr(QTKit, 'CLASSNAMERef') )
        # self.assert_( issubclass(QTKit.CLASSNAMERef, objc.lookUpClass('NSCFType')) )
        # self.assert_( QTKit.CLASSNAMERef is not objc.lookUpClass('NSCFType') )

    def testValues(self):
        # Use this to test for a number of enum and #define values
        pass

        # Integer values:
        # self.assert_( hasattr(QTKit, 'CONSTANT') )
        # self.assert_( isinstance(QTKit.CONSTANT, (int, long)) )
        # self.assertEquals(QTKit.CONSTANT, 7)

        # String values:
        # self.assert_( hasattr(QTKit, 'CONSTANT') )
        # self.assert_( isinstance(QTKit.CONSTANT, (str, unicode)) )
        # self.assertEquals(QTKit.CONSTANT, 'value')

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        pass

        # self.assert_( hasattr(QTKit, 'CONSTANT') )
        # self.assert_( isinstance(QTKit.CONSTANT, unicode) )

    def testFunctions(self):
        # Use this to test for functions
        pass

        # self.assert_( hasattr(QTKit, 'FUNCTION') )

    def testOpaque(self):
        # Use this to test for opaque pointers
        pass

        # self.assert_( hasattr(QTKit, 'OPAQUE') )

    def testProtocols(self):
        # Use this to test if informal protocols  are present
        pass

        # self.assert_( hasattr(QTKit, 'protocols') )

        # self.assert_( hasattr(QTKit.protocols, 'PROTOCOL') )
        # self.assert_( isinstance(QTKit.protocols.PROTOCOL, objc.informal_protocol) )

    def test_structs(self):
        # Use this to test struct wrappers
        pass

        # self.assert_( hasattr(QTKit, 'STRUCT') )
        # o = QTKit.STRUCT()
        # self.assert_( hasattr(o, 'FIELD_NAME') )



if __name__ == "__main__":
    unittest.main()

