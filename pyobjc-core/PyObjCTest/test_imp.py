import objc
import inspect
from PyObjCTools.TestSupport import TestCase
from PyObjCTest.test_metadata import OC_MetaDataTest


NSObject = objc.lookUpClass("NSObject")
NSMutableArray = objc.lookUpClass("NSMutableArray")
NSArray = objc.lookUpClass("NSArray")


class TestBasicIMP(TestCase):
    # Test the basic functionality of IMP's. Imp's are basically unbound
    # selectors if you look at the interface. The implementation refers to
    # the actual functions that implements the method for calling the IMP
    # instead of passing through the usual message sending machinery.
    #
    def testIMPType(self):
        self.assertHasAttr(objc, "IMP")

    def testAlloc(self):
        cls = NSObject
        m = cls.pyobjc_classMethods.methodForSelector_("alloc")
        self.assertIsInstance(m, objc.IMP)
        self.assertTrue(m.__metadata__()["classmethod"])
        self.assertEqual(
            m.__metadata__()["retval"].get("already_retained"),
            cls.alloc.__metadata__()["retval"].get("already_retained"),
        )
        self.assertEqual(m.selector, b"alloc")

        o = m(cls).init()
        self.assertIsInstance(o, cls)

        o = NSArray.alloc()
        m = o.methodForSelector_("init")

        # XXX: Need to recreate the value because
        #      calling a method on a partially
        #      initialed value resets the object
        #      reference (see comment in selector.m)
        o = NSArray.alloc()

        o2 = m(o)
        self.assertEqual(o2, [])
        self.assertIsInstance(o2, NSArray)

        with self.assertRaisesRegex(
            AttributeError, "cannot access attribute 'init' of NIL"
        ):
            o.init()

    def testInit1(self):
        cls = NSObject
        m = cls.instanceMethodForSelector_("init")
        self.assertIsInstance(m, objc.IMP)
        self.assertFalse(m.__metadata__()["classmethod"])
        self.assertEqual(
            m.__metadata__()["retval"].get("already_retained"),
            cls.init.__metadata__()["retval"].get("already_retained"),
        )
        self.assertEqual(m.selector, b"init")

        o = m(cls.alloc())
        self.assertIsInstance(o, cls)

    def testInit2(self):
        cls = NSObject
        o = cls.alloc().init()

        m = o.methodForSelector_("init")
        self.assertIsInstance(m, objc.IMP)
        self.assertFalse(m.__metadata__()["classmethod"])
        self.assertEqual(
            m.__metadata__()["retval"].get("already_retained"),
            cls.init.__metadata__()["retval"].get("already_retained"),
        )
        self.assertEqual(m.selector, b"init")

        o = m(cls.alloc())
        self.assertIsInstance(o, cls)

    def testDescription(self):
        o = NSObject.alloc().init()

        imp = o.methodForSelector_(b"description")
        self.assertEqual(o.description(), imp(o))

        with self.assertRaisesRegex(TypeError, "Missing argument: self"):
            imp()

    def test_repr(self):
        o = NSObject.alloc().init()

        imp = o.methodForSelector_(b"description")

        self.assertRegex(repr(imp), "<IMP description at 0x[0-9a-f]+ for 0x[0-9a-f]+>")

    def test_no_keywords(self):
        o = NSObject.alloc().init()

        imp = o.methodForSelector_(b"description")
        self.assertIsInstance(imp, objc.IMP)

        with self.assertRaisesRegex(
            TypeError,
            "(<IMP description at 0x[0-9a-f]+ for 0x[0-9a-f]+> does not accept keyword arguments)"
            "|(keyword arguments not supported)",
        ):
            imp(self=o)

        o = NSMutableArray.alloc().init()
        imp = o.methodForSelector_(b"addObject:")
        self.assertIsInstance(imp, objc.IMP)

        with self.assertRaisesRegex(
            TypeError,
            "(<IMP addObject: at 0x[0-9a-f]+ for 0x[0-9a-f]+> does not accept keyword arguments)"
            "|(keyword arguments not supported)",
        ):
            imp(o, value=42)

        o = OC_MetaDataTest.alloc().init()
        imp = o.methodForSelector_(b"unknownLengthArray")
        with self.assertRaisesRegex(
            TypeError,
            "(<IMP unknownLengthArray at 0x[0-9a-f]+ for 0x[0-9a-f]+> does not accept keyword arguments)"
            "|(keyword arguments not supported)",
        ):
            imp(o, value=42)

    def test_too_few(self):
        o = NSObject.alloc().init()

        imp = o.methodForSelector_(b"description")

        with self.assertRaisesRegex(TypeError, "Missing argument: self"):
            imp()

        o = NSMutableArray.alloc().init()
        imp = o.methodForSelector_(b"addObject:")
        self.assertIsInstance(imp, objc.IMP)

        with self.assertRaisesRegex(TypeError, "Missing argument: self"):
            imp()

    def test_imp_signature(self):
        o = NSMutableArray.alloc().init()
        imp = o.methodForSelector_(b"addObject:")

        self.assertEqual(imp.signature, o.addObject_.signature)
        self.assertEqual(len(imp.__signature__.parameters), 2)

    def test_imp_no_args(self):
        o = NSMutableArray.alloc().init()
        imp = o.methodForSelector_(b"addObject:")

        with self.assertRaisesRegex(TypeError, "Missing argument: self"):
            imp()

    def test_init_with_imp(self):
        imp = NSMutableArray.instanceMethodForSelector_(b"init")
        o = NSMutableArray.alloc()
        o = imp(o)
        self.assertIsInstance(o, NSMutableArray)

    def test_initArray_with_imp(self):
        imp = NSArray.instanceMethodForSelector_(b"initWithArray:")
        o = NSArray.alloc()
        p = imp(o, [1, 2])
        self.assertIsInstance(p, NSArray)
        self.assertIsNot(o, p)

        # Make sure the pointer to ObjC is cleared:
        with self.assertRaisesRegex(
            AttributeError, "cannot access attribute '__c_void_p__' of NIL "
        ):
            o.__c_void_p__

    def test_imp_attributes(self):
        o = NSMutableArray.alloc().init()
        imp = o.methodForSelector_(b"addObject:")
        alloc_imp = NSMutableArray.methodForSelector_(b"alloc")
        cls_imp = NSMutableArray.methodForSelector_(b"array")

        self.assertFalse(imp.isAlloc)
        self.assertFalse(imp.isClassMethod)
        self.assertEqual(
            objc.splitSignature(imp.signature), objc.splitSignature(b"v@:@")
        )
        self.assertEqual(imp.selector, b"addObject:")
        self.assertEqual(
            imp.__name__, b"addObject:"
        )  # XXX: Shouldn't this be a string?
        sig = inspect.signature(imp)
        self.assertIsInstance(sig, inspect.Signature)
        self.assertEqual(str(sig), "(arg0, arg1, /)")

        self.assertFalse(cls_imp.isAlloc)
        self.assertTrue(cls_imp.isClassMethod)

        self.assertTrue(alloc_imp.isAlloc)
        self.assertTrue(alloc_imp.isClassMethod)


class TestGettingIMPs(TestCase):
    def test_too_few_arguments(self):
        o = NSMutableArray.alloc().init()

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 0"):
            o.methodForSelector_()

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 0"):
            NSMutableArray.instanceMethodForSelector_()

    def test_too_many_arguments(self):
        o = NSMutableArray.alloc().init()

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 2"):
            o.methodForSelector_(b"addObject:", b"bar")

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 2"):
            NSMutableArray.instanceMethodForSelector_(b"addObject:", b"bar")

    def test_not_sel(self):
        o = NSMutableArray.alloc().init()

        with self.assertRaisesRegex(ValueError, "depythonifying 'SEL', got 'int'"):
            o.methodForSelector_(42)

        with self.assertRaisesRegex(ValueError, "depythonifying 'SEL', got 'int'"):
            NSMutableArray.instanceMethodForSelector_(42)
