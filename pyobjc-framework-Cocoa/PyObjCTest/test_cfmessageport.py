from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestMessagePort (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFMessagePortRef)

    def testConstants(self):
        self.assertEqual(kCFMessagePortSuccess, 0)
        self.assertEqual(kCFMessagePortSendTimeout, -1)
        self.assertEqual(kCFMessagePortReceiveTimeout, -2)
        self.assertEqual(kCFMessagePortIsInvalid, -3)
        self.assertEqual(kCFMessagePortTransportError, -4)

    @min_os_level('10.6')
    def testConstants10_6(self):
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
        port, shouldFree = CFMessagePortCreateLocal(None, u"name", callout, context, None)
        self.assertIsInstance(port, CFMessagePortRef)
        self.assertIs(shouldFree is True or shouldFree, False)
        self.assertFalse(CFMessagePortIsRemote(port))
        ctx = CFMessagePortGetContext(port, None)
        self.assertIs(ctx, context)

        port2 = CFMessagePortCreateRemote(None, u"name")
        self.assertIsInstance(port2, CFMessagePortRef)
        self.assertResultIsBOOL(CFMessagePortIsRemote)
        self.assertTrue(CFMessagePortIsRemote(port2))
        self.assertTrue(CFMessagePortGetName(port2), u"name")


        CFMessagePortSetName(port2, "newname")
        self.assertTrue(CFMessagePortGetName(port2), u"newname")

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
            print "callout"
            info.append((port, messageid, data))
            return buffer("hello world")

        port, shouldFree = CFMessagePortCreateLocal(None, u"pyobjc.test", callout, context, None)
        self.assertIsInstance(port, CFMessagePortRef)

        self.assertArgIsOut(CFMessagePortSendRequest, 6)
        rls = CFMessagePortCreateRunLoopSource(None, port, 0)
        err, data = CFMessagePortSendRequest(port, 99, None, 1.0, 1.0, None, None)
        self.assertEqual(err, 0)
        self.assertEqual(data, None)


if __name__ == "__main__":
    main()
