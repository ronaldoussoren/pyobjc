import objc
from PyObjCTools.TestSupport import TestCase

NSObject = objc.lookUpClass("NSObject")


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

        with self.assertRaisesRegex(
            TypeError,
            "(<IMP description at 0x[0-9a-f]+ for 0x[0-9a-f]+> does not accept keyword arguments)"
            "|(keyword arguments not supported)",
        ):
            imp(self=o)

    def test_too_rew(self):
        o = NSObject.alloc().init()

        imp = o.methodForSelector_(b"description")

        with self.assertRaisesRegex(TypeError, "Missing argument: self"):
            imp()
