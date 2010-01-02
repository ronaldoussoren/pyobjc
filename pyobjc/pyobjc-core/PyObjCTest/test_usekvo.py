from PyObjCTools.TestSupport import *
import objc

NSObject = objc.lookUpClass('NSObject')

class TestUseKVOObserver (NSObject):
    def init(self):
        self = super(TestUseKVOObserver, self).init()
        if self is None:
            return None

        self.observations = []
        return self

    def observeValueForKeyPath_ofObject_change_context_(self, path, object, change, context):
        self.observations.append((path, object))


class TestUseKVO (TestCase):
    def setUp(self):
        self._previous = objc.setUseKVOForSetattr(True)

    def tearDown(self):
        objc.setUseKVOForSetattr(self._previous)

    def areChangesEmitted(self, object):
        observer = TestUseKVOObserver.alloc().init()
        object.addObserver_forKeyPath_options_context_(
                observer, "value", 0, 0)

        try:
            object.value = 42

        finally:
            object.removeObserver_forKeyPath_(observer, "value")

        return len(observer.observations) > 0

    def assertChangesEmitted(self, object):
        if not self.areChangesEmitted(object):
            self.fail("Setting 'value' on %r doesn't emit KVO" % object)

    def assertNoChangesEmitted(self, object):
        if self.areChangesEmitted(object):
            self.fail("Setting 'value' on %r does emit KVO" % object)

    def testPythonAttr_True(self):
        objc.setUseKVOForSetattr(True)

        class OCTestUseKVO1 (NSObject):
            pass

        self.assertTrue(OCTestUseKVO1.__useKVO__)

        obj = OCTestUseKVO1.alloc().init()
        self.assertChangesEmitted(obj)

    def testObjCAttr_True(self):
        objc.setUseKVOForSetattr(True)

        class OCTestUseKVO2 (NSObject):
            value = objc.ivar()

        self.assertTrue(OCTestUseKVO2.__useKVO__)

        obj = OCTestUseKVO2.alloc().init()
        self.assertChangesEmitted(obj)


    def testPythonAttr_False(self):
        objc.setUseKVOForSetattr(False)

        class OCTestUseKVO3 (NSObject):
            pass

        self.assertFalse(OCTestUseKVO3.__useKVO__)
        obj = OCTestUseKVO3.alloc().init()
        self.assertNoChangesEmitted(obj)

    def testObjCAttr_False(self):
        objc.setUseKVOForSetattr(False)

        class OCTestUseKVO4 (NSObject):
            value = objc.ivar()

        self.assertFalse(OCTestUseKVO4.__useKVO__)
        obj = OCTestUseKVO4.alloc().init()
        self.assertNoChangesEmitted(obj)


if __name__ == "__main__":
    main()
