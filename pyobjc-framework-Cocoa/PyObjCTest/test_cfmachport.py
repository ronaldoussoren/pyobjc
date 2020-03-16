import Foundation
import objc
import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level

MachPortClasses = tuple(
    cls for cls in objc.getClassList() if cls.__name__ == "NSMachPort"
)


class TestMachPort(TestCase):
    def testTypes(self):
        try:
            if objc.lookUpClass("NSMachPort") is CoreFoundation.CFMachPortRef:
                return
        except objc.error:
            pass
        self.assertIsCFType(CoreFoundation.CFMachPortRef)

    def testTypeID(self):
        self.assertIsInstance(CoreFoundation.CFMachPortGetTypeID(), int)

    @min_os_level("10.8")
    def testCreate10_8(self):
        class Context:
            pass

        context = Context()

        def callout(port, msg, size, info):
            pass

        port, shouldFree = CoreFoundation.CFMachPortCreate(None, callout, context, None)

        # On OSX 10.7 or earlier this test passed, on OSX 10.8 it doesn't???
        self.assertIsInstance(port, MachPortClasses)

    def testCreate(self):
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
