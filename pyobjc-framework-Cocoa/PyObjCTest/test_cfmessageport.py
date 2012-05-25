from PyObjCTools.TestSupport import *
from CoreFoundation import *


try:
    long
except NameError:
    long = int


class TestMessagePort (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFMessagePortRef)

    def testConstants(self):
        self.assertEqual(kCFMessagePortSuccess, 0)
        self.assertEqual(kCFMessagePortSendTimeout, -1)
        self.assertEqual(kCFMessagePortReceiveTimeout, -2)
        self.assertEqual(kCFMessagePortIsInvalid, -3)
        self.assertEqual(kCFMessagePortTransportError, -4)
        self.assertEqual(kCFMessagePortBecameInvalidError, -5)

    @min_os_level('10.6')
    @expectedFailure
    def testFunctions10_6(self):
        self.fail('CFMessagePortSetDispatchQueue: dispatch_queue_t not wrapped yet')

    def testTypeID(self):
        self.assertIsInstance(CFMessagePortGetTypeID(), (int, long))

    def testInteraction(self):
        class Context: pass
        context = Context()

        def callout(port, messageid, data, info):
            pass
        port, shouldFree = CFMessagePortCreateLocal(None, b"name".decode('ascii'), callout, context, None)
        self.assertIsInstance(port, CFMessagePortRef)
        self.assertIs(shouldFree is True or shouldFree, False)
        self.assertFalse(CFMessagePortIsRemote(port))
        ctx = CFMessagePortGetContext(port, None)
        self.assertIs(ctx, context)

        port2 = CFMessagePortCreateRemote(None, b"name".decode('ascii'))
        self.assertIsInstance(port2, CFMessagePortRef)
        self.assertResultIsBOOL(CFMessagePortIsRemote)
        self.assertTrue(CFMessagePortIsRemote(port2))
        self.assertTrue(CFMessagePortGetName(port2), b"name".decode('ascii'))


        CFMessagePortSetName(port2, "newname")
        self.assertTrue(CFMessagePortGetName(port2), b"newname".decode('ascii'))

        cb = CFMessagePortGetInvalidationCallBack(port)
        self.assertIs(cb, None)
        global didInvalidate
        didInvalidate = False

        @objc.callbackFor(CFMessagePortSetInvalidationCallBack)
        def invalidate(port, info):
            global didInvalidate
            didInvalidate = True

        CFMessagePortSetInvalidationCallBack(port, invalidate)
        cb = CFMessagePortGetInvalidationCallBack(port)

        # XXX: Without writing a custom wrapper we cannot guarantee this
        #self.assertIs(cb, invalidate)
        cb(None, None)
        self.assertIs(didInvalidate, True)
        didInvalidate = False

        rls = CFMessagePortCreateRunLoopSource(None, port, 0)
        self.assertIsInstance(rls, CFRunLoopSourceRef)
        self.assertResultIsBOOL(CFMessagePortIsValid)
        self.assertTrue(CFMessagePortIsValid(port))
        CFMessagePortInvalidate(port)
        self.assertFalse(CFMessagePortIsValid(port))
        self.assertTrue(didInvalidate)

    @min_os_level('10.5')
    def testSending(self):
        # FIXME: Crash on Tiger
        context = []
        def callout(port, messageid, data, info):
            info.append((port, messageid, data))
            return buffer("hello world")

        port, shouldFree = CFMessagePortCreateLocal(None, b"pyobjc.test".decode('ascii'), callout, context, None)
        self.assertIsInstance(port, CFMessagePortRef)

        self.assertArgIsOut(CFMessagePortSendRequest, 6)
        rls = CFMessagePortCreateRunLoopSource(None, port, 0)
        err, data = CFMessagePortSendRequest(port, 99, None, 1.0, 1.0, None, None)
        self.assertEqual(err, 0)
        self.assertEqual(data, None)


if __name__ == "__main__":
    main()
