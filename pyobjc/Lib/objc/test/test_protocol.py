import unittest
import objc
import warnings

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')

MyProto = objc.informal_protocol("MyProto", (
    objc.selector(None, selector="testMethod", signature="v@:", isRequired=1),
    objc.selector(None, selector="testMethod2:", signature="v@:i", isRequired=0)
))

class TestInformalProtocols(unittest.TestCase):


    def testMissingProto(self):
        class ProtoClass1 (NSObject):
            def testMethod(self):
                pass
        self.assertEquals(ProtoClass1.testMethod.signature, "v@:")


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

class TestFormalProtocols (unittest.TestCase):
    # Implement unittests for formal protocols here.
    #

    def testImplementFormalProtocol(self):

        NSLocking = objc.protocolNamed('NSLocking')

        class MyClassNotImplementingLocking(NSObject):
            pass

        self.assert_(not MyClassNotImplementingLocking.pyobjc_classMethods.conformsToProtocol_(NSLocking))

        class MyClassImplementingLocking(NSObject, NSLocking):
            pass

        self.assert_(MyClassImplementingLocking.pyobjc_classMethods.conformsToProtocol_(NSLocking))

    def testImplementAnotherObject(self):
        anObject = NSObject.alloc().init()

        try:
            class MyClassImplementingAnotherObject(NSObject, anObject):
                    pass
            self.fail()
        except TypeError: 
            pass

        try:
            class MyClassImplementingAnotherObject(NSObject, 10):
                    pass
            self.fail()
        except TypeError: 
            pass

        try:
            class MyClassImplementingAnotherObject(NSObject, int):
                    pass
            self.fail()
        except TypeError: 
            pass


if __name__ == '__main__':
    unittest.main()
