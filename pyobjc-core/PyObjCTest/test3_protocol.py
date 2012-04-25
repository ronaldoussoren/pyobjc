from PyObjCTools.TestSupport import *
import objc
import warnings
import sys

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')

MyProto = objc.informal_protocol("MyProto", (
    objc.selector(None, selector=b"testMethod", signature=b"I@:", isRequired=1),
    objc.selector(None, selector=b"testMethod2:", signature=b"v@:i", isRequired=0)
))

class Test3InformalProtocols(TestCase):
    def testOptional(self):
        class ProtoClass3 (NSObject, protocols=MyProto):
            def testMethod(self):
                pass




if __name__ == '__main__':
    main()
