import objc
import inspect
import warnings
from PyObjCTools.TestSupport import TestCase
from PyObjCTest.test_metadata import OC_MetaDataTest
from .test_metadata import NoObjCClass


NSObject = objc.lookUpClass("NSObject")
NSMutableArray = objc.lookUpClass("NSMutableArray")
NSArray = objc.lookUpClass("NSArray")
NSException = objc.lookUpClass("NSException")


class OC_InstanceMethod(NSObject):
    def instanceMethod(self):
        return 42


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

        with self.assertRaisesRegex(TypeError, "Missing argument: self"):
            m()

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

        o = NSObject.alloc().init()
        i = NSObject.methodForSelector_(b"alloc")
        o2 = i(o).init()
        self.assertIsInstance(o2, NSObject)
        self.assertIsNot(o, o2)

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

    def test_argument_cannot_be_converted(self):
        o = NSArray.arrayWithArray_([1, 2, 3])
        m = o.methodForSelector_(b"objectAtIndex:")
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'type'"
        ):
            m(o, object)

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

    def test_imp_attributes(self):
        o = NSMutableArray.alloc().init()
        imp = o.methodForSelector_(b"addObject:")
        alloc_imp = NSMutableArray.methodForSelector_(b"alloc")
        cls_imp = NSMutableArray.methodForSelector_(b"array")

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=objc.ApiDeprecationWarning)
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

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=objc.ApiDeprecationWarning)
            self.assertFalse(cls_imp.isAlloc)
        self.assertTrue(cls_imp.isClassMethod)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=objc.ApiDeprecationWarning)
            self.assertFalse(alloc_imp.isAlloc)

        with warnings.catch_warnings():
            warnings.simplefilter("error", category=objc.ApiDeprecationWarning)
            with self.assertRaisesRegex(
                objc.ApiDeprecationWarning, "isAlloc is always false"
            ):
                self.assertFalse(alloc_imp.isAlloc)
        self.assertTrue(alloc_imp.isClassMethod)

    def test_class_imp_instance_self(self):
        o = NSObject.alloc().init()

        m = NSObject.methodForSelector_("new")

        v = m(o)
        self.assertIsInstance(v, NSObject)

    def test_class_imp_meta_self(self):
        m = NSObject.methodForSelector_(b"new")
        v = m(type(NSObject))
        self.assertIsInstance(v, NSObject)

    def test_class_imp_invalid_self(self):
        m = NSObject.methodForSelector_("description")
        with self.assertRaisesRegex(
            TypeError,
            "Need objective-C object or class as self, not an instance of 'int'",
        ):
            m(42)

    def test_instance_imp_python_self(self):
        m = NSObject.instanceMethodForSelector_("description")
        self.assertIn("OC_BuiltinPythonDictionary", m({}))

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            m(NoObjCClass())

        with self.assertRaisesRegex(objc.error, "Cannot call methods on 'nil'"):
            m(None)

    def test_instance_imp_raises(self):
        m = NSException.instanceMethodForSelector_(b"raise")

        o = NSException.exceptionWithName_reason_userInfo_("name", "reason", None)
        with self.assertRaisesRegex(objc.error, "name - reason"):
            m(o)

    def test_bad_argcount(self):
        m = NSException.methodForSelector_(b"exceptionWithName:reason:userInfo:")
        with self.assertRaisesRegex(TypeError, "Need 4 arguments, got 1"):
            m(NSException, "hello")


class TestGettingIMPs(TestCase):
    def test_basic(self):
        o = NSObject.alloc().init()
        m = o.methodForSelector_(b"description")
        self.assertEqual(m(o), o.description())

        m = NSObject.instanceMethodForSelector_(b"description")
        self.assertEqual(m(o), o.description())

        m = NSObject.methodForSelector_(b"description")
        self.assertEqual(m(NSObject), NSObject.description())

        # Note: Do not call m with an instance as 'self',
        # that will crash (similarly to how calling an instance
        # method IMP with an incorrect self will fail.

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

        m = o.methodForSelector_("sortUsingSelector:")
        m(o, b"description")

    def test_not_found(self):
        o = NSMutableArray.alloc().init()
        with self.assertRaisesRegex(AttributeError, "No attribute doesnotexist"):
            o.methodForSelector_(b"doesnotexist")

        with self.assertRaisesRegex(AttributeError, "No attribute doesnotexist"):
            NSMutableArray.instanceMethodForSelector_(b"doesnotexist")

        with self.assertRaisesRegex(AttributeError, "No attribute doesnotexist"):
            NSMutableArray.methodForSelector_(b"doesnotexist")

    def test_python_selector(self):
        o = OC_InstanceMethod.alloc().init()
        imp = o.methodForSelector_(b"instanceMethod")
        self.assertEqual(imp, o.instanceMethod.callable)

        imp = OC_InstanceMethod.instanceMethodForSelector_(b"instanceMethod")
        self.assertEqual(imp, o.instanceMethod.callable)
