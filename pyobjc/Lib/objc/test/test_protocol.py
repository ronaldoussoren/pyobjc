import unittest
import objc
import warnings

warnings.filterwarnings("error", category=objc.ProtocolWarning)

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')

MyProto = objc.informal_protocol("MyProto", (
    objc.selector(None, selector="testMethod", signature="v@:", isRequired=1),
    objc.selector(None, selector="testMethod2:", signature="v@:i", isRequired=0)
))

class TestProtocols(unittest.TestCase):

    def doMissingProto(self):
        class ProtoClass1 (NSObject):
            def testMethod(self):
                pass

    def testMissingProto(self):
        self.assertRaises(objc.ProtocolWarning, self.doMissingProto)


    def doIncompleteClass(self):
        class ProtoClass2 (NSObject, MyProto):
            def testMethod2_(self, x):
                pass

    def testIncompleteClass(self):
        self.assertRaises(TypeError, self.doIncompleteClass)


    def testOptional(self):
        class ProtoClass3 (NSObject, MyProto):
            def testMethod(self):
                pass


if __name__ == '__main__':
    unittest.main()
