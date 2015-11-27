"""
FIXME: None of these tests actually use the MachPort
"""
from PyObjCTools.TestSupport import *
from CoreFoundation import *
import Foundation


MachPortClasses = tuple(cls for cls in objc.getClassList() if cls.__name__ == "NSMachPort")


class TestMachPort (TestCase):
    def testTypes(self):
        try:
            if objc.lookUpClass('NSMachPort') is CFMachPortRef:
                return
        except objc.error:
            pass
        self.assertIsCFType(CFMachPortRef)

    def testTypeID(self):
        self.assertIsInstance(CFMachPortGetTypeID(), (int, long))

    @min_os_level('10.8')
    def testCreate10_8(self):
        class Context: pass
        context = Context()

        def callout(port, msg, size, info):
            pass

        port, shouldFree = CFMachPortCreate(None, callout, context, None)

        # On OSX 10.7 or earlier this test passed, on OSX 10.8 it doesn't???
        self.assertIsInstance(port, MachPortClasses)

    def testCreate(self):

        class Context: pass
        context = Context()

        def callout(port, msg, size, info):
            pass

        # XXX: This one cannot be tested without bindings to the low-level mach_port API's
        #port, shouldFree = CFMachPortCreateWithPort(None, 1, callout, context, None)
        #self.assertIsInstance(port, CFMachPortRef)
        #self.assertTrue(shouldFree is True or shouldFree is False)

        port, shouldFree = CFMachPortCreate(None, callout, context, None)

        self.assertIsInstance(port, MachPortClasses)
        self.assertIsInstance(port, Foundation.NSPort)
        self.assertTrue(shouldFree is True or shouldFree is False)
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
