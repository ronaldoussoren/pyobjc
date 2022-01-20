import objc
from PyObjCTools.TestSupport import TestCase
from PyObjCTest.test_metadata import OC_MetaDataTest


NSObject = objc.lookUpClass("NSObject")
NSMutableArray = objc.lookUpClass("NSMutableArray")


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

        self.assertEqual(o.description(), o.methodForSelector_(b"description")(o))

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
