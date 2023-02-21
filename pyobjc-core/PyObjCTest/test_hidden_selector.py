import objc
from PyObjCTools.TestSupport import TestCase


class hidden_method:
    def __pyobjc_class_setup__(self, name, class_dict, instance_methods, class_methods):
        @objc.selector
        def method(self):
            return 42

        method.isHidden = True

        def clsmethod(self):
            return 99

        clsmethod = objc.selector(clsmethod, isClassMethod=True)
        clsmethod.isHidden = True

        instance_methods.add(method)
        class_methods.add(clsmethod)


class OCTestHidden(objc.lookUpClass("NSObject")):
    m = hidden_method()

    @objc.selector
    def body(self):
        return "BODY"

    body.isHidden = True

    def bodyclass(self):
        return "BODYCLASS"

    bodyclass = objc.selector(bodyclass, isClassMethod=True)
    bodyclass.isHidden = True

    @objc.selector
    def somebody(self):
        return "instance"

    somebody.isHidden = True

    def boolMethod(self):
        return True

    boolMethod = objc.selector(boolMethod, signature=objc._C_NSBOOL + b"@:")
    boolMethod.isHidden = True


class OCTestSubHidden(OCTestHidden):
    def body(self):
        return "BODY2"

    @classmethod
    def bodyclass(self):
        return "BODYCLASS2"

    @classmethod
    def somebody(self):
        return "class"

    def boolMethod(self):
        return False


class TestHiddenSelector(TestCase):
    def testHiddenInClassDef(self):
        o = OCTestHidden.alloc().init()
        with self.assertRaisesRegex(
            AttributeError, "'OCTestHidden' object has no attribute 'body'"
        ):
            o.body()

        v = o.performSelector_(b"body")
        self.assertEqual(v, "BODY")

        v = o.pyobjc_instanceMethods.body()
        self.assertEqual(v, "BODY")

        with self.assertRaisesRegex(AttributeError, "bodyclass"):
            OCTestHidden.bodyclass()
        v = OCTestHidden.performSelector_(b"bodyclass")
        self.assertEqual(v, "BODYCLASS")

        v = OCTestHidden.pyobjc_classMethods.bodyclass()
        self.assertEqual(v, "BODYCLASS")

        o = OCTestHidden.alloc().init()
        with self.assertRaisesRegex(
            AttributeError, "'OCTestHidden' object has no attribute 'boolMethod'"
        ):
            o.boolMethod()
        m = o.pyobjc_instanceMethods.boolMethod
        self.assertIsInstance(m, objc.selector)
        self.assertNotIsInstance(m, objc.native_selector)
        self.assertResultIsBOOL(m)
        v = m()
        self.assertIs(v, True)

    def testHiddenCanBeIntrospected(self):
        # XXX: This test fails, and will also fail in versions
        #      before 9.1. It would be better if the test didn't
        #      fail though...
        o = OCTestHidden.alloc().init()
        m = o.pyobjc_instanceMethods.body
        self.assertIsInstance(m, objc.selector)
        self.assertNotIsInstance(m, objc.native_selector)
        self.assertTrue(m.isHidden)

    def testHiddenInSetupHook(self):
        o = OCTestHidden.alloc().init()

        # Instance method
        with self.assertRaisesRegex(
            AttributeError, "'OCTestHidden' object has no attribute 'method'"
        ):
            o.method()

        v = o.performSelector_(b"method")
        self.assertEqual(v, 42)

        v = o.pyobjc_instanceMethods.method()
        self.assertEqual(v, 42)

        # Class method
        with self.assertRaisesRegex(AttributeError, "clsmethod"):
            OCTestHidden.clsmethod()

        v = OCTestHidden.performSelector_(b"clsmethod")
        self.assertEqual(v, 99)

        v = OCTestHidden.pyobjc_classMethods.clsmethod()
        self.assertEqual(v, 99)

    def testHiddenAddMethods(self):
        @objc.selector
        def addedmethod(self):
            return "NEW"

        addedmethod.isHidden = True

        def addedclass(self):
            return "NEWCLASS"

        addedclass = objc.selector(addedclass, isClassMethod=True)
        addedclass.isHidden = True

        objc.classAddMethods(OCTestHidden, [addedmethod, addedclass])

        o = OCTestHidden.alloc().init()

        # Instance method
        with self.assertRaisesRegex(
            AttributeError, "'OCTestHidden' object has no attribute 'addedmethod'"
        ):
            o.addedmethod()

        v = o.performSelector_(b"addedmethod")
        self.assertEqual(v, "NEW")

        self.assertIn(b"addedmethod", OCTestHidden.pyobjc_hiddenSelectors(False))

        m = o.pyobjc_instanceMethods.addedmethod
        self.assertIsInstance(m, objc.selector)
        self.assertNotIsInstance(m, objc.native_selector)
        v = m()
        self.assertEqual(v, "NEW")

        # Class method
        with self.assertRaisesRegex(AttributeError, "addedclass"):
            OCTestHidden.addedclass()

        v = OCTestHidden.performSelector_(b"addedclass")
        self.assertEqual(v, "NEWCLASS")

        self.assertIn(b"addedclass", OCTestHidden.pyobjc_hiddenSelectors(True))
        v = OCTestHidden.pyobjc_classMethods.addedclass()
        self.assertEqual(v, "NEWCLASS")

    def testClassVsInstance(self):
        o = OCTestHidden.alloc().init()
        with self.assertRaisesRegex(
            AttributeError, "'OCTestHidden' object has no attribute 'sombody'"
        ):
            o.sombody()
        v = o.performSelector_(b"somebody")
        self.assertEqual(v, "instance")

        v = OCTestSubHidden.somebody()
        self.assertEqual(v, "class")

    def testHiddenInSubClass(self):
        # Instance
        o = OCTestSubHidden.alloc().init()
        with self.assertRaisesRegex(
            AttributeError, "'OCTestSubHidden' object has no attribute 'body'"
        ):
            o.body()
        v = o.performSelector_(b"body")
        self.assertEqual(v, "BODY2")

        @objc.selector
        def subclassbody(self):
            return "base"

        subclassbody.isHidden = True

        @objc.selector
        def subclassbody2(self):
            return "base2"

        subclassbody.isHidden = True

        objc.classAddMethods(OCTestHidden, [subclassbody, subclassbody2])

        @objc.selector
        def subclassbody(self):
            return "sub"

        @objc.selector
        def subclassbody2(self):
            return "sub2"

        objc.classAddMethods(OCTestSubHidden, [subclassbody])
        with self.assertRaisesRegex(
            AttributeError, "'OCTestSubHidden' object has no attribute 'subclassbody'"
        ):
            o.subclassbody()
        v = o.performSelector_(b"subclassbody")
        self.assertEqual(v, "sub")

        OCTestSubHidden.subclassbody2 = subclassbody2
        v = o.performSelector_(b"subclassbody2")
        self.assertEqual(v, "sub2")

        with self.assertRaisesRegex(
            AttributeError, "'OCTestSubHidden' object has no attribute 'boolMethod'"
        ):
            o.boolMethod()
        m = o.pyobjc_instanceMethods.boolMethod
        self.assertIsInstance(m, objc.selector)
        self.assertNotIsInstance(m, objc.native_selector)
        self.assertResultIsBOOL(m)
        v = m()
        self.assertIs(v, False)

        # Class
        with self.assertRaisesRegex(AttributeError, "bodyclass"):
            OCTestSubHidden.bodyclass()
        v = OCTestSubHidden.performSelector_(b"bodyclass")
        self.assertEqual(v, "BODYCLASS2")

    def test_hidden_attribute(self):
        @objc.selector
        def method(self):
            return 42

        method.isHidden = True
        self.assertIs(method.isHidden, True)
        method.isHidden = False
        self.assertIs(method.isHidden, False)

        with self.assertRaisesRegex(TypeError, "Cannot delete 'isHidden'"):
            del method.isHidden

        method.isHidden = "foo"
        self.assertIs(method.isHidden, True)
