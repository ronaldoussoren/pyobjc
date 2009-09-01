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

    def failUnlessChangesEmitted(self, object):
        if not self.areChangesEmitted(object):
            self.fail("Setting 'value' on %r doesn't emit KVO" % object)

    def failIfChangesEmitted(self, object):
        if self.areChangesEmitted(object):
            self.fail("Setting 'value' on %r does emit KVO" % object)

    def testPythonAttr_True(self):
        objc.setUseKVOForSetattr(True)

        class OCTestUseKVO1 (NSObject):
            pass

        self.failUnless(OCTestUseKVO1.__useKVO__)

        obj = OCTestUseKVO1.alloc().init()
        self.failUnlessChangesEmitted(obj)

    def testObjCAttr_True(self):
        objc.setUseKVOForSetattr(True)

        class OCTestUseKVO2 (NSObject):
            value = objc.ivar()

        self.failUnless(OCTestUseKVO2.__useKVO__)

        obj = OCTestUseKVO2.alloc().init()
        self.failUnlessChangesEmitted(obj)


    def testPythonAttr_False(self):
        objc.setUseKVOForSetattr(False)

        class OCTestUseKVO3 (NSObject):
            pass

        self.failIf(OCTestUseKVO3.__useKVO__)
        obj = OCTestUseKVO3.alloc().init()
        self.failIfChangesEmitted(obj)

    def testObjCAttr_False(self):
        objc.setUseKVOForSetattr(False)

        class OCTestUseKVO4 (NSObject):
            value = objc.ivar()

        self.failIf(OCTestUseKVO4.__useKVO__)
        obj = OCTestUseKVO4.alloc().init()
        self.failIfChangesEmitted(obj)


if __name__ == "__main__":
    main()
