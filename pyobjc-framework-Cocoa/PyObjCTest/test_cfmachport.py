import Foundation
import objc
import CoreFoundation
from PyObjCTools.TestSupport import TestCase

MachPortClasses = tuple(
    cls for cls in objc.getClassList() if cls.__name__ == "NSMachPort"
)


class TestMachPort(TestCase):
    def test_types(self):
        try:
            if objc.lookUpClass("NSMachPort") is CoreFoundation.CFMachPortRef:
                return
        except objc.error:
            pass
        self.assertIsCFType(CoreFoundation.CFMachPortRef)

    def test_typeid(self):
        self.assertIsInstance(CoreFoundation.CFMachPortGetTypeID(), int)

    def test_create2(self):
        class Context:
            pass

        context = Context()

        def callout(port, msg, size, info):
            pass

        port, shouldFree = CoreFoundation.CFMachPortCreate(None, callout, context, None)

        self.assertIsInstance(port, MachPortClasses)

    def test_create(self):
        class Context:
            pass

        context = Context()

        def callout(port, msg, size, info):
            pass

        # XXX: This one cannot be tested without bindings to the low-level mach_port API's
        # port, shouldFree = CoreFoundation.CFMachPortCreateWithPort(None, 1, callout, context, None)  # noqa: B950
        # self.assertIsInstance(port, CoreFoundation.CFMachPortRef)
        # self.assertTrue(shouldFree is True or shouldFree is False)

        port, shouldFree = CoreFoundation.CFMachPortCreate(None, callout, context, None)

        self.assertIsInstance(port, MachPortClasses)
        self.assertIsInstance(port, Foundation.NSPort)
        self.assertTrue(shouldFree is True or shouldFree is False)
        idx = CoreFoundation.CFMachPortGetPort(port)
        self.assertIsInstance(idx, int)
        ctx = CoreFoundation.CFMachPortGetContext(port, None)
        self.assertIs(ctx, context)
        cb = CoreFoundation.CFMachPortGetInvalidationCallBack(port)
        self.assertIs(cb, None)
        global didInvalidate
        didInvalidate = False

        def invalidate(port, info):
            global didInvalidate
            didInvalidate = True

        CoreFoundation.CFMachPortSetInvalidationCallBack(port, invalidate)
        cb = CoreFoundation.CFMachPortGetInvalidationCallBack(port)
        self.assertIs(invalidate, cb)
        rls = CoreFoundation.CFMachPortCreateRunLoopSource(None, port, 0)
        self.assertIsInstance(rls, CoreFoundation.CFRunLoopSourceRef)
        self.assertTrue(CoreFoundation.CFMachPortIsValid(port))
        CoreFoundation.CFMachPortInvalidate(port)
        self.assertFalse(CoreFoundation.CFMachPortIsValid(port))
        self.assertTrue(didInvalidate)
