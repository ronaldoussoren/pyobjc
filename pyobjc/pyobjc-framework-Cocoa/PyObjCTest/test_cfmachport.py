"""
FIXME: None of these tests actually use the MachPort
"""
from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestMachPort (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFMachPortRef)

    def testTypeID(self):
        self.failUnless(isinstance(CFMachPortGetTypeID(), (int, long)))

    def testCreate(self):
        class Context: pass
        context = Context()

        def callout(port, msg, size, info):
            pass

        # This one cannot be tested without bindings to the low-level mach_port API's
        #port, shouldFree = CFMachPortCreateWithPort(None, 1, callout, context, None)
        #self.failUnless(isinstance(port, CFMachPortRef))
        #self.failUnless(shouldFree is True or shouldFree is False)

        port, shouldFree = CFMachPortCreate(None, callout, context, None)
        self.failUnless(isinstance(port, CFMachPortRef))
        self.failUnless(shouldFree is True or shouldFree is False)

        idx = CFMachPortGetPort(port)
        self.failUnless(isinstance(idx, (int, long)))

        ctx = CFMachPortGetContext(port)
        self.failUnless(ctx is context)

        cb = CFMachPortGetInvalidationCallBack(port)
        self.failUnless(cb is None)

        global didInvalidate
        didInvalidate=False
        def invalidate(port, info):
            global didInvalidate
            didInvalidate = True

        CFMachPortSetInvalidationCallBack(port, invalidate)
        cb = CFMachPortGetInvalidationCallBack(port)
        self.failUnless(invalidate is cb)

        rls = CFMachPortCreateRunLoopSource(None, port, 0)
        self.failUnless(isinstance(rls, CFRunLoopSourceRef))

        self.failUnless(CFMachPortIsValid(port))
        CFMachPortInvalidate(port)
        self.failIf(CFMachPortIsValid(port))
        self.failUnless(didInvalidate)

if __name__ == "__main__":
    main()
