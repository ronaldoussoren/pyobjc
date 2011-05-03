"""
FIXME: None of these tests actually use the MachPort
"""
from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestMachPort (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFMachPortRef)

    def testTypeID(self):
        self.assertIsInstance(CFMachPortGetTypeID(), (int, long))
    def testCreate(self):
        class Context: pass
        context = Context()

        def callout(port, msg, size, info):
            pass

        # This one cannot be tested without bindings to the low-level mach_port API's
        #port, shouldFree = CFMachPortCreateWithPort(None, 1, callout, context, None)
        #self.assertIsInstance(port, CFMachPortRef)
        #self.assertIs(shouldFree is True or shouldFree, False)
        port, shouldFree = CFMachPortCreate(None, callout, context, None)
        self.assertIsInstance(port, CFMachPortRef)
        self.assertIs(shouldFree is True or shouldFree, False)
        idx = CFMachPortGetPort(port)
        self.assertIsInstance(idx, (int, long))
        ctx = CFMachPortGetContext(port, None)
        self.assertIs(ctx, context)
        cb = CFMachPortGetInvalidationCallBack(port)
        self.assertIs(cb, None)
        global didInvalidate
        didInvalidate=False
        def invalidate(port, info):
            global didInvalidate
            didInvalidate = True

        CFMachPortSetInvalidationCallBack(port, invalidate)
        cb = CFMachPortGetInvalidationCallBack(port)
        self.assertIs(invalidate, cb)
        rls = CFMachPortCreateRunLoopSource(None, port, 0)
        self.assertIsInstance(rls, CFRunLoopSourceRef)
        self.assertTrue(CFMachPortIsValid(port))
        CFMachPortInvalidate(port)
        self.assertFalse(CFMachPortIsValid(port))
        self.assertTrue(didInvalidate)

if __name__ == "__main__":
    main()
