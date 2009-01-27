'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import InterfaceBuilderKit

class TestInterfaceBuilderKit (TestCase):
    def testClasses(self):
        self.assert_( hasattr(InterfaceBuilderKit, 'IBDocument') )
        self.assert_( isinstance(InterfaceBuilderKit.IBDocument, objc.objc_class) )
        self.assert_( hasattr(InterfaceBuilderKit, 'IBPlugin') )
        self.assert_( isinstance(InterfaceBuilderKit.IBPlugin, objc.objc_class) )

    def test_protocols(self):

        self.assert_( hasattr(InterfaceBuilderKit, 'protocols') )
        self.assert_( hasattr(InterfaceBuilderKit.protocols, 'IBObjectIntegration') )
        self.assert_( isinstance(InterfaceBuilderKit.protocols.IBObjectIntegration, objc.informal_protocol) )

if __name__ == "__main__":
    main()

