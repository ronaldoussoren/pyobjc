from PyObjCTools.TestSupport import *
import objc


objc.registerMetaDataForSelector(
    b"OC_CallbackTest", b"selWithSEL:SEL:andObject:", {
        "arguments": {
            2:  {
                "sel_of_type":  b"q@:q",
            },
            3:  {
                "sel_of_type": b"v@:@@^v",
            }
        }
    }
)

class OC_CallbackTest (objc.lookUpClass("NSObject")):
    @objc.typedSelector(b"v@:" + objc._C_SEL + objc._C_SEL + b"@")
    def selWithSEL_SEL_andObject_(self, s1, s2, o):
        pass

    def selWithoutSEL_(self, o):
        pass


class TestClosure (TestCase):
    # tests for objc._makeClosure
    # (note: as the name indicates _makeClosure is not a public API)
    def testCallbackForUnsupported(self):
        def function(arg):
            pass

        self.assertRaises(TypeError, objc._makeClosure, function, dir, -1)
        self.assertRaises(TypeError, objc._makeClosure, function, function, -1)
        self.assertRaises(TypeError, objc._makeClosure, function, 42, -1)
        self.assertRaises(ValueError, objc._makeClosure, function, OC_CallbackTest.selWithSEL_SEL_andObject_,  -1)
        self.assertRaises(ValueError, objc._makeClosure, function, OC_CallbackTest.selWithoutSEL_,  -1)

    # create and use closure for 
    # - function
    # - selector
    # - different kinds of arguments


class TestCallbackFor (TestCase):
    # tests for objc.callbackFor
    def testCallbackForUnsupported(self):
        def function(arg):
            pass

        self.assertRaises(TypeError, objc.callbackFor(dir), function)
        self.assertRaises(TypeError, objc.callbackFor(function), function)
        self.assertRaises(TypeError, objc.callbackFor(42), function)
        self.assertRaises(ValueError, objc.callbackFor(OC_CallbackTest.selWithSEL_SEL_andObject_), function)
        self.assertRaises(ValueError, objc.callbackFor(OC_CallbackTest.selWithoutSEL_), function)



class TestSelectorFor (TestCase):
    # tests for objc.selectorFor
    def test_consistency(self):
        self.assertEqual(OC_CallbackTest.selWithSEL_SEL_andObject_.signature,
                b"v@:::@")

    def testNotSelector(self):
        self.assertRaises(ValueError, objc.selectorFor, OC_CallbackTest.selWithSEL_SEL_andObject_, 4)
        self.assertRaises(ValueError, objc.selectorFor, OC_CallbackTest.selWithSEL_SEL_andObject_, 8)
        self.assertRaises(ValueError, objc.selectorFor, OC_CallbackTest.selWithoutSEL_)

    def testDefault(self):
        @objc.selectorFor(OC_CallbackTest.selWithSEL_SEL_andObject_)
        def selector(self, a):
            pass

        self.assertEqual(selector.signature, b"q@:q")

    def testExplicit(self):

        @objc.selectorFor(OC_CallbackTest.selWithSEL_SEL_andObject_, 2)
        def selector(self, a):
            pass

        self.assertEqual(selector.signature, b"q@:q")

        @objc.selectorFor(OC_CallbackTest.selWithSEL_SEL_andObject_, 3)
        def selector(self, a):
            pass

        self.assertEqual(selector.signature, b"v@:@@^v")


if __name__ == "__main__":
    main()
