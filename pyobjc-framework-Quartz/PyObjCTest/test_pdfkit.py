'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
from Quartz import PDFKit

class TestPDFKit (unittest.TestCase):
    def testClasses(self):
        pass
        # self.assert_( hasattr(PDFKit, 'CLASSNAME') )
        # self.assert_( isinstance(PDFKit.CLASSNAME, objc.objc_class) )
        # Tollfree CF-type:
        # self.assert_( hasattr(PDFKit, 'CLASSNAMERef') )
        # self.assert_( PDFKit.CLASSNAMERef is PDFKit.CLASSNAME )

        # Not-tollfree CF-type:
        # self.assert_( hasattr(PDFKit, 'CLASSNAMERef') )
        # self.assert_( issubclass(PDFKit.CLASSNAMERef, objc.lookUpClass('NSCFType')) )
        # self.assert_( PDFKit.CLASSNAMERef is not objc.lookUpClass('NSCFType') )

    def testValues(self):
        # Use this to test for a number of enum and #define values
        pass

        # Integer values:
        # self.assert_( hasattr(PDFKit, 'CONSTANT') )
        # self.assert_( isinstance(PDFKit.CONSTANT, (int, long)) )
        # self.assertEquals(PDFKit.CONSTANT, 7)

        # String values:
        # self.assert_( hasattr(PDFKit, 'CONSTANT') )
        # self.assert_( isinstance(PDFKit.CONSTANT, (str, unicode)) )
        # self.assertEquals(PDFKit.CONSTANT, 'value')

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        pass

        # self.assert_( hasattr(PDFKit, 'CONSTANT') )
        # self.assert_( isinstance(PDFKit.CONSTANT, unicode) )

    def testFunctions(self):
        # Use this to test for functions
        pass

        # self.assert_( hasattr(PDFKit, 'FUNCTION') )

    def testOpaque(self):
        # Use this to test for opaque pointers
        pass

        # self.assert_( hasattr(PDFKit, 'OPAQUE') )

    def testProtocols(self):
        # Use this to test if informal protocols  are present
        pass

        # self.assert_( hasattr(PDFKit, 'protocols') )

        # self.assert_( hasattr(PDFKit.protocols, 'PROTOCOL') )
        # self.assert_( isinstance(PDFKit.protocols.PROTOCOL, objc.informal_protocol) )

    def test_structs(self):
        # Use this to test struct wrappers
        pass

        # self.assert_( hasattr(PDFKit, 'STRUCT') )
        # o = PDFKit.STRUCT()
        # self.assert_( hasattr(o, 'FIELD_NAME') )



if __name__ == "__main__":
    unittest.main()

