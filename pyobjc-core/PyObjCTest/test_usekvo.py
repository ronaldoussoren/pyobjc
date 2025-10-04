import objc
from PyObjCTools.TestSupport import TestCase, pyobjc_options

NSObject = objc.lookUpClass("NSObject")


class TestUseKVOObserver(NSObject):
    def init(self):
        self = objc.super(TestUseKVOObserver, self).init()
        if self is None:
            return None

        self.observations = []
        return self

    def observeValueForKeyPath_ofObject_change_context_(
        self, path, value, change, context
    ):
        self.observations.append((path, value))


class TestUseKVO(TestCase):
    def setUp(self):
        self._previous = objc.options.use_kvo
        objc.options.use_kvo = True

    def tearDown(self):
        objc.options.use_kvo = self._previous

    def areChangesEmitted(self, value):
        observer = TestUseKVOObserver.alloc().init()
        value.addObserver_forKeyPath_options_context_(observer, "value", 0, 0)

        try:
            value.value = 42

        finally:
            value.removeObserver_forKeyPath_(observer, "value")

        return len(observer.observations) > 0

    def assertChangesEmitted(self, value):
        if not self.areChangesEmitted(value):
            self.fail("Setting 'value' on %r doesn't emit KVO" % value)

    def assertNoChangesEmitted(self, value):
        if self.areChangesEmitted(value):
            self.fail("Setting 'value' on %r does emit KVO" % value)

    def testPythonAttr_True(self):
        objc.options.use_kvo = True

        class OCTestUseKVO1(NSObject):
            pass

        self.assertTrue(OCTestUseKVO1.__useKVO__)

        obj = OCTestUseKVO1.alloc().init()
        self.assertChangesEmitted(obj)

    def testObjCAttr_True(self):
        objc.options.use_kvo = True

        class OCTestUseKVO2(NSObject):
            value = objc.ivar()

        self.assertTrue(OCTestUseKVO2.__useKVO__)

        obj = OCTestUseKVO2.alloc().init()
        self.assertChangesEmitted(obj)

    def testPythonAttr_False(self):
        objc.options.use_kvo = False

        class OCTestUseKVO3(NSObject):
            pass

        self.assertFalse(OCTestUseKVO3.__useKVO__)
        obj = OCTestUseKVO3.alloc().init()
        self.assertNoChangesEmitted(obj)

    def testObjCAttr_False(self):
        objc.options.use_kvo = False

        class OCTestUseKVO4(NSObject):
            value = objc.ivar()

        self.assertFalse(OCTestUseKVO4.__useKVO__)
        obj = OCTestUseKVO4.alloc().init()
        self.assertNoChangesEmitted(obj)

    def test_update_attr(self):
        objc.options.use_kvo = False

        class OCTestUseKVO5(NSObject):
            value = objc.ivar()

        self.assertFalse(OCTestUseKVO5.__useKVO__)

        OCTestUseKVO5.__useKVO__ = "foo"

        self.assertTrue(OCTestUseKVO5.__useKVO__)

        class NoCompare:
            def __bool__(self):
                raise RuntimeError("no compare")

        with self.assertRaises(RuntimeError):
            OCTestUseKVO5.__useKVO__ = NoCompare()

        OCTestUseKVO5.__useKVO__ = False

        self.assertFalse(OCTestUseKVO5.__useKVO__)

        with self.assertRaisesRegex(TypeError, "Cannot delete __useKVO__ attribute"):
            del OCTestUseKVO5.__useKVO__

    def test_useKVO_in_body(self):
        with pyobjc_options(use_kvo=False):

            class OCTestUseKVO6(NSObject):
                value = objc.ivar()
                __useKVO__ = 42

            self.assertIs(OCTestUseKVO6.__useKVO__, True)
