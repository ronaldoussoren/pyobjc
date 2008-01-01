'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import InterfaceBuilderKit

class TestInterfaceBuilderKit (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(InterfaceBuilderKit, 'IBDocument') )
        self.assert_( isinstance(InterfaceBuilderKit.IBDocument, objc.objc_class) )
        self.assert_( hasattr(InterfaceBuilderKit, 'IBPlugin') )
        self.assert_( isinstance(InterfaceBuilderKit.IBPlugin, objc.objc_class) )

    def testValues(self):
        self.assert_( hasattr(InterfaceBuilderKit, 'IBMaxYDirection') )
        self.assert_( isinstance(InterfaceBuilderKit.IBMaxYDirection, (int, long)) )
        self.assertEquals(InterfaceBuilderKit.IBMaxYDirection, 8)

    def testVariables(self):
        pass

    def test_structs(self):
        self.assert_( hasattr(InterfaceBuilderKit, 'IBInset') )

        o = InterfaceBuilderKit.IBInset()
        self.assert_( hasattr(o, 'left') )
        self.assert_( hasattr(o, 'top') )
        self.assert_( hasattr(o, 'right') )
        self.assert_( hasattr(o, 'bottom') )

    def test_protocols(self):

        self.assert_( hasattr(InterfaceBuilderKit, 'protocols') )
        self.assert_( hasattr(InterfaceBuilderKit.protocols, 'IBObjectIntegration') )
        self.assert_( isinstance(InterfaceBuilderKit.protocols.IBObjectIntegration, objc.informal_protocol) )

if __name__ == "__main__":
    unittest.main()

