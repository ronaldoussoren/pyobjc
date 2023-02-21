import copy

import objc
from PyObjCTest.fnd import NSObject
from PyObjCTools.TestSupport import TestCase

objc.registerMetaDataForSelector(
    b"NSObject",
    b"validateValue:forKey:error:",
    {
        "arguments": {
            2: {"type_modifier": objc._C_INOUT},
            4: {"type_modifier": objc._C_OUT},
        }
    },
)


class OCCopy(NSObject):
    def copy(self):
        return self.copyWithZone_(None)

    def copyWithZone_(self, zone):
        v = OCCopy.allocWithZone_(zone).init()
        return v


class OCObserve(NSObject):
    def init(self):
        self = objc.super(OCObserve, self).init()
        self.values = []
        self.registrations = []
        return self

    @property
    def seen(self):
        return {v[1]: v[2]["new"] for v in self.values}

    @objc.python_method
    def register(self, value, keypath):
        value.addObserver_forKeyPath_options_context_(self, keypath, 0x3, None)
        self.registrations.append((value, keypath))

    @objc.python_method
    def unregister(self, value, keypath):
        value.removeObserver_forKeyPath_(self, keypath)

    def observeValueForKeyPath_ofObject_change_context_(
        self, keypath, value, change, context
    ):
        # We don't get to keep the 'change' dictionary, make
        # a copy (it gets reused in future calls)
        new_change = {}
        for k in change:
            v = change[k]
            if isinstance(v, (list, tuple, set)):
                v = copy.copy(v)
            new_change[k] = v
        self.values.append((value, keypath, new_change))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, value, traceback):
        for o, k in self.registrations:
            self.unregister(o, k)
        self.registrations = []


class TestObjectProperty(TestCase):
    def testCreation(self):
        class OCTestObjectProperty1(NSObject):
            p1 = objc.object_property()
            p2 = objc.object_property(copy=True)
            p3 = objc.object_property(read_only=True)
            p4 = objc.object_property(ivar="myp4")
            p5 = objc.object_property(typestr=objc._C_INT)
            p6 = objc.object_property(typestr=objc._C_DBL)

        o = OCTestObjectProperty1.alloc().init()

        self.assertTrue(o.respondsToSelector_(b"p1"))
        self.assertTrue(o.respondsToSelector_(b"setP1:"))

        v = OCCopy.alloc().init()
        o.p1 = v
        self.assertIs(o.p1, v)
        self.assertIs(o._p1, v)

        self.assertTrue(o.respondsToSelector_(b"p2"))
        self.assertTrue(o.respondsToSelector_(b"setP2:"))

        o.p2 = v
        self.assertIsInstance(o.p2, OCCopy)
        self.assertIsNot(o.p2, v)
        self.assertIsNot(o._p2, v)

        self.assertTrue(o.respondsToSelector_(b"p3"))
        self.assertFalse(o.respondsToSelector_(b"setP3:"))

        o._p3 = v
        self.assertIs(o.p3, v)

        self.assertTrue(o.respondsToSelector_(b"p4"))
        self.assertTrue(o.respondsToSelector_(b"setP4:"))

        o.p4 = v
        self.assertIs(o.p4, v)
        self.assertIs(o.myp4, v)

        self.assertTrue(o.respondsToSelector_(b"p5"))
        self.assertTrue(o.respondsToSelector_(b"setP5:"))
        self.assertTrue(o.respondsToSelector_(b"p6"))
        self.assertTrue(o.respondsToSelector_(b"setP6:"))
        s = o.methodSignatureForSelector_(b"p5")
        self.assertEqual(s.methodReturnType(), objc._C_INT)
        s = o.methodSignatureForSelector_(b"p6")
        self.assertEqual(s.methodReturnType(), objc._C_DBL)

    def testDepends(self):
        class OCTestObjectProperty2(NSObject):
            p1 = objc.object_property()
            p2 = objc.object_property()
            p3 = objc.object_property(read_only=True, depends_on=["p1", "p2"])
            p9 = objc.object_property()

            @p3.getter
            def p3(self):
                return (self.p1 or "", self.p2 or "")

        class OCTestObjectProperty2b(OCTestObjectProperty2):
            p4 = objc.object_property()

            @OCTestObjectProperty2.p3.getter
            def p3(self):
                return (self.p4 or "", self.p2 or "", self.p1 or "")

            p3.depends_on("p4")

            p5 = objc.object_property(read_only=True)

            @p5.getter
            def p5(self):
                return f"-{self.p4}-"

            p5.depends_on("p4")

            @OCTestObjectProperty2.p9.getter
            def p9(self):
                return f"+{self.p4}+"

            p9.depends_on("p4")

        observer1 = OCObserve.alloc().init()
        observer2 = OCObserve.alloc().init()
        object1 = OCTestObjectProperty2.alloc().init()
        object2 = OCTestObjectProperty2b.alloc().init()

        v = type(object1).keyPathsForValuesAffectingP3()
        self.assertIsInstance(v, objc.lookUpClass("NSSet"))
        self.assertEqual(v, {"p1", "p2"})

        v = type(object2).keyPathsForValuesAffectingP3()
        self.assertIsInstance(v, objc.lookUpClass("NSSet"))
        self.assertEqual(v, {"p1", "p2", "p4"})

        self.assertTrue(object1.respondsToSelector_("p1"))
        self.assertTrue(object1.respondsToSelector_("setP1:"))
        self.assertTrue(object1.respondsToSelector_("p2"))
        self.assertTrue(object1.respondsToSelector_("setP2:"))
        self.assertTrue(object1.respondsToSelector_("p3"))
        self.assertFalse(object1.respondsToSelector_("setP3:"))
        self.assertTrue(object1.respondsToSelector_("p9"))
        self.assertTrue(object1.respondsToSelector_("setP9:"))

        self.assertTrue(object2.respondsToSelector_("p1"))
        self.assertTrue(object2.respondsToSelector_("setP1:"))
        self.assertTrue(object2.respondsToSelector_("p2"))
        self.assertTrue(object2.respondsToSelector_("setP2:"))
        self.assertTrue(object2.respondsToSelector_("p3"))
        self.assertFalse(object2.respondsToSelector_("setP3:"))
        self.assertTrue(object2.respondsToSelector_("p4"))
        self.assertTrue(object2.respondsToSelector_("setP4:"))
        self.assertTrue(object2.respondsToSelector_("p9"))
        self.assertTrue(object2.respondsToSelector_("setP9:"))

        observer1.register(object1, "p1")
        observer1.register(object1, "p2")
        observer1.register(object1, "p3")

        observer2.register(object2, "p1")
        observer2.register(object2, "p2")
        observer2.register(object2, "p3")
        observer2.register(object2, "p4")
        observer2.register(object2, "p5")
        observer2.register(object2, "p9")

        try:
            self.assertEqual(observer1.values, [])
            self.assertEqual(observer2.values, [])

            object1.p1 = "a"
            object1.p2 = "b"
            self.assertEqual(object1.p3, ("a", "b"))
            self.assertEqual(object1.pyobjc_instanceMethods.p3(), ("a", "b"))

            object2.p1 = "a"
            object2.p2 = "b"
            object2.p4 = "c"
            self.assertEqual(object2.p3, ("c", "b", "a"))
            self.assertEqual(object2.pyobjc_instanceMethods.p3(), ("c", "b", "a"))
            self.assertEqual(object2.pyobjc_instanceMethods.p4(), "c")

            # seen = { v[1]: v[2]['new'] for v in observer1.values }
            self.assertEqual(observer1.seen, {"p1": "a", "p2": "b", "p3": ("a", "b")})

            # seen = { v[1]: v[2]['new'] for v in observer2.values }
            self.assertEqual(
                observer2.seen,
                {
                    "p1": "a",
                    "p2": "b",
                    "p3": ("c", "b", "a"),
                    "p4": "c",
                    "p5": "-c-",
                    "p9": "+c+",
                },
            )

        finally:
            observer1.unregister(object1, "p1")
            observer1.unregister(object1, "p2")
            observer1.unregister(object1, "p3")

            observer2.unregister(object2, "p1")
            observer2.unregister(object2, "p2")
            observer2.unregister(object2, "p3")
            observer2.unregister(object2, "p4")
            observer2.unregister(object2, "p5")
            observer2.unregister(object2, "p9")

    def testDepends2(self):
        class OCTestObjectProperty2B(NSObject):
            p1 = objc.object_property()

            @p1.getter
            def p1(self):
                return self._p1

            @p1.setter
            def p1(self, v):
                self._p1 = v

            p2 = objc.object_property()

            @p2.getter
            def p2(self):
                return self._p2

            @p2.setter
            def p2(self, v):
                self._p2 = v

            p3 = objc.object_property(read_only=True, depends_on=["p1", "p2"])

            @p3.getter
            def p3(self):
                return (self.p1 or "", self.p2 or "")

        class OCTestObjectProperty2Bb(OCTestObjectProperty2B):
            p4 = objc.object_property()

            @OCTestObjectProperty2B.p1.getter
            def p1(self):
                return self._p1

            @OCTestObjectProperty2B.p3.getter
            def p3(self):
                return (self.p4 or "", self.p2 or "", self.p1 or "")

            p3.depends_on("p4")

        observer1 = OCObserve.alloc().init()
        observer2 = OCObserve.alloc().init()
        object1 = OCTestObjectProperty2B.alloc().init()
        object2 = OCTestObjectProperty2Bb.alloc().init()

        v = type(object1).keyPathsForValuesAffectingP3()
        self.assertIsInstance(v, objc.lookUpClass("NSSet"))
        self.assertEqual(v, {"p1", "p2"})

        v = type(object2).keyPathsForValuesAffectingP3()
        self.assertIsInstance(v, objc.lookUpClass("NSSet"))
        self.assertEqual(v, {"p1", "p2", "p4"})

        self.assertTrue(object1.respondsToSelector_("p1"))
        self.assertTrue(object1.respondsToSelector_("setP1:"))
        self.assertTrue(object1.respondsToSelector_("p2"))
        self.assertTrue(object1.respondsToSelector_("setP2:"))
        self.assertTrue(object1.respondsToSelector_("p3"))
        self.assertFalse(object1.respondsToSelector_("setP3:"))

        self.assertTrue(object2.respondsToSelector_("p1"))
        self.assertTrue(object2.respondsToSelector_("setP1:"))
        self.assertTrue(object2.respondsToSelector_("p2"))
        self.assertTrue(object2.respondsToSelector_("setP2:"))
        self.assertTrue(object2.respondsToSelector_("p3"))
        self.assertFalse(object2.respondsToSelector_("setP3:"))
        self.assertTrue(object2.respondsToSelector_("p4"))
        self.assertTrue(object2.respondsToSelector_("setP4:"))

        observer1.register(object1, "p1")
        observer1.register(object1, "p2")
        observer1.register(object1, "p3")

        observer2.register(object2, "p1")
        observer2.register(object2, "p2")
        observer2.register(object2, "p3")
        observer2.register(object2, "p4")

        try:
            self.assertEqual(observer1.values, [])
            self.assertEqual(observer2.values, [])

            object1.p1 = "a"
            object1.p2 = "b"
            self.assertEqual(object1.p3, ("a", "b"))
            self.assertEqual(object1.pyobjc_instanceMethods.p3(), ("a", "b"))

            object2.p1 = "a"
            object2.p2 = "b"
            object2.p4 = "c"
            self.assertEqual(object2.p3, ("c", "b", "a"))
            self.assertEqual(object2.pyobjc_instanceMethods.p3(), ("c", "b", "a"))
            self.assertEqual(object2.pyobjc_instanceMethods.p4(), "c")

            # seen = { v[1]: v[2]['new'] for v in observer1.values }
            self.assertEqual(observer1.seen, {"p1": "a", "p2": "b", "p3": ("a", "b")})

            # seen = { v[1]: v[2]['new'] for v in observer2.values }
            self.assertEqual(
                observer2.seen, {"p1": "a", "p2": "b", "p3": ("c", "b", "a"), "p4": "c"}
            )

        finally:
            observer1.unregister(object1, "p1")
            observer1.unregister(object1, "p2")
            observer1.unregister(object1, "p3")

            observer2.unregister(object2, "p1")
            observer2.unregister(object2, "p2")
            observer2.unregister(object2, "p3")
            observer2.unregister(object2, "p4")

    def testMethods(self):
        lst = []

        class OCTestObjectProperty4(NSObject):
            p1 = objc.object_property()

            @p1.getter
            def p1(self):
                lst.append(("get",))
                return self._p1 + "!"

            @p1.setter
            def p1(self, v):
                lst.append(("set", v))
                self._p1 = v + "?"

            @p1.validate
            def p1(self, value, error):
                if value == 1:
                    return (True, value, None)
                else:
                    return (False, 2, "snake")

        class OCTestObjectProperty4b(OCTestObjectProperty4):
            @OCTestObjectProperty4.p1.validate
            def p1(self, value, error):
                if value == 2:
                    return (True, value, None)
                else:
                    return (False, 2, "monty")

        o = OCTestObjectProperty4.alloc().init()
        o.p1 = "f"
        self.assertEqual(o.p1, "f?!")
        self.assertEqual(o._p1, "f?")
        self.assertEqual(lst, [("set", "f"), ("get",)])

        ok, value, error = o.validateValue_forKey_error_(1, "p1", None)
        self.assertTrue(ok)
        self.assertEqual(value, 1)
        self.assertEqual(error, None)

        ok, value, error = o.validateValue_forKey_error_(9, "p1", None)
        self.assertFalse(ok)
        self.assertEqual(value, 2)
        self.assertEqual(error, "snake")

        lst = []
        o = OCTestObjectProperty4b.alloc().init()
        o.p1 = "f"
        self.assertEqual(o.p1, "f?!")
        self.assertEqual(o._p1, "f?")
        self.assertEqual(lst, [("set", "f"), ("get",)])

        ok, value, error = o.validateValue_forKey_error_(2, "p1", None)
        self.assertTrue(ok)
        self.assertEqual(value, 2)
        self.assertEqual(error, None)

        ok, value, error = o.validateValue_forKey_error_(9, "p1", None)
        self.assertFalse(ok)
        self.assertEqual(value, 2)
        self.assertEqual(error, "monty")

    def testNative(self):
        lst = []

        class OCTestObjectProperty7(NSObject):
            p1 = objc.object_property()

            @p1.getter
            def p1(self):
                lst.append("get")
                return self._p1

            @p1.setter
            def p1(self, value):
                lst.append("set")
                self._p1 = value

        o = OCTestObjectProperty7.alloc().init()
        o.setValue_forKey_(42, "p1")
        self.assertEqual(o._p1, 42)

        o._p1 = "monkey"
        v = o.valueForKey_("p1")
        self.assertEqual(v, "monkey")

        self.assertEqual(lst, ["set", "get"])

    def testDynamic(self):
        class OCTestObjectProperty8(NSObject):
            p1 = objc.object_property(dynamic=True)
            p2 = objc.object_property(dynamic=True, typestr=objc._C_NSBOOL)

        self.assertFalse(OCTestObjectProperty8.instancesRespondToSelector_(b"p1"))
        self.assertFalse(OCTestObjectProperty8.instancesRespondToSelector_(b"setP1:"))
        self.assertFalse(OCTestObjectProperty8.instancesRespondToSelector_(b"isP2"))
        self.assertFalse(OCTestObjectProperty8.instancesRespondToSelector_(b"setP2:"))

        v = [42]

        def getter(self):
            return v[0]

        def setter(self, value):
            v[0] = value

        OCTestObjectProperty8.p1 = getter
        OCTestObjectProperty8.setP1_ = setter

        v2 = [False]

        def getter2(self):
            return v2[0]

        def setter2(self, value):
            v2[0] = bool(value)

        OCTestObjectProperty8.isP2 = getter2
        OCTestObjectProperty8.setP2_ = setter2

        self.assertTrue(OCTestObjectProperty8.instancesRespondToSelector_(b"p1"))
        self.assertTrue(OCTestObjectProperty8.instancesRespondToSelector_(b"setP1:"))
        self.assertTrue(OCTestObjectProperty8.instancesRespondToSelector_(b"isP2"))
        self.assertTrue(OCTestObjectProperty8.instancesRespondToSelector_(b"setP2:"))

        o = OCTestObjectProperty8.alloc().init()
        self.assertIsInstance(OCTestObjectProperty8.p1, objc.object_property)
        self.assertIsInstance(OCTestObjectProperty8.p2, objc.object_property)

        self.assertEqual(o.p1, 42)
        self.assertEqual(o.p2, False)
        o.p1 = 99
        o.p2 = True
        self.assertEqual(o.p1, 99)
        self.assertEqual(v[0], 99)
        self.assertEqual(o.p2, True)
        self.assertEqual(v2[0], True)

    def testReadOnly(self):
        class OCTestObjectProperty3(NSObject):
            p1 = objc.object_property(read_only=True)

        o = OCTestObjectProperty3.alloc().init()

        with self.assertRaisesRegex(ValueError, "setting read-only property p1"):
            o.p1 = 42

    def testSubclass(self):
        class OCTestObjectProperty5(NSObject):
            p1 = objc.object_property(read_only=True)
            p2 = objc.object_property()
            p3 = objc.object_property(read_only=True, typestr=objc._C_NSBOOL)

        class OCTestObjectProperty6(OCTestObjectProperty5):
            @OCTestObjectProperty5.p1.setter
            def p1(self, value):
                self._p1 = value

            @OCTestObjectProperty5.p2.setter
            def p2(self, value):
                self._p2 = value * 2

            @OCTestObjectProperty5.p3.getter
            def p3(self):
                return not objc.super(OCTestObjectProperty6, self).p3

        base = OCTestObjectProperty5.alloc().init()
        with self.assertRaisesRegex(ValueError, "setting read-only property p1"):
            base.p1 = 1
        with self.assertRaisesRegex(ValueError, "setting read-only property p3"):
            base.p3 = 1
        base.p2 = "b"
        self.assertEqual(base.p2, "b")

        sub = OCTestObjectProperty6.alloc().init()
        sub.p1 = 1
        sub.p2 = "a"
        sub._p3 = False
        self.assertEqual(sub.p1, 1)
        self.assertEqual(sub.p2, "aa")
        self.assertEqual(sub.p3, True)

        self.assertTrue(base.respondsToSelector_(b"p2"))
        self.assertFalse(base.respondsToSelector_(b"setP1:"))
        self.assertTrue(base.respondsToSelector_(b"isP3"))
        self.assertFalse(base.respondsToSelector_(b"p3"))

        self.assertTrue(sub.respondsToSelector_(b"p2"))
        self.assertTrue(sub.respondsToSelector_(b"setP1:"))
        self.assertTrue(sub.respondsToSelector_(b"isP3"))
        self.assertFalse(sub.respondsToSelector_(b"p3"))

        try:
            del sub.p3
        except TypeError:
            pass
        else:
            self.fail("Deleting an object_property shouldn't be possible")

    def testDefaultSetterWithoutIvar(self):
        try:

            class OCTestObjectProperty7(NSObject):
                p1 = objc.object_property(ivar=objc.NULL)

        except ValueError:
            pass

        else:
            self.fail("ValueError not raised")

        try:

            class OCTestObjectProperty8(NSObject):
                p1 = objc.object_property(ivar=objc.NULL, read_only=True)

        except ValueError:
            pass

        else:
            self.fail("ValueError not raised")

        try:

            class OCTestObjectProperty9(NSObject):
                p1 = objc.object_property(read_only=True)

                @p1.setter
                def p1(self, v):
                    pass

        except ValueError:
            pass

        else:
            self.fail("ValueError not raised")

        try:

            class OCTestObjectProperty10(NSObject):
                p1 = objc.object_property(read_only=True)

                @p1.validate
                def p1(self, v):
                    pass

        except ValueError:
            pass

        else:
            self.fail("ValueError not raised")


class TestBoolProperty(TestCase):
    def testDefault(self):
        class OCTestBoolProperty1(NSObject):
            p1 = objc.bool_property()

        o = OCTestBoolProperty1.alloc().init()
        self.assertEqual(o.p1, False)

        o.p1 = [1, 2]
        self.assertEqual(o.p1, True)
