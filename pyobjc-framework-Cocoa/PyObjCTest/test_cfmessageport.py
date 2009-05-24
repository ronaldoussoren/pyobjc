from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestMessagePort (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFMessagePortRef)

    def testConstants(self):
        self.failUnless(kCFMessagePortSuccess == 0)
        self.failUnless(kCFMessagePortSendTimeout == -1)
        self.failUnless(kCFMessagePortReceiveTimeout == -2)
        self.failUnless(kCFMessagePortIsInvalid == -3)
        self.failUnless(kCFMessagePortTransportError == -4)

    def testTypeID(self):
        self.failUnless(isinstance(CFMessagePortGetTypeID(), (int, long)))

    def testInteraction(self):
        class Context: pass
        context = Context()

        def callout(port, messageid, data, info):
            pass

        port, shouldFree = CFMessagePortCreateLocal(None, u"name", callout, context, None)
        self.failUnless(isinstance(port, CFMessagePortRef))
        self.failUnless(shouldFree is True or shouldFree is False)
        
        self.failIf(CFMessagePortIsRemote(port))
        ctx = CFMessagePortGetContext(port)
        self.failUnless(ctx is context)


        port = CFMessagePortCreateRemote(None, u"name")
        self.failUnless(isinstance(port, CFMessagePortRef))

        self.failUnlessResultIsBOOL(CFMessagePortIsRemote)
        self.failUnless(CFMessagePortIsRemote(port))
        self.failUnless(CFMessagePortGetName(port), u"name")

        CFMessagePortSetName(port, "newname")
        self.failUnless(CFMessagePortGetName(port), u"newname")

        cb = CFMessagePortGetInvalidationCallBack(port)
        self.failUnless(cb is None)

        global didInvalidate
        didInvalidate = False

        @objc.callbackFor(CFMessagePortSetInvalidationCallBack)
        def invalidate(port, info):
            global didInvalidate
            didInvalidate = True

        CFMessagePortSetInvalidationCallBack(port, invalidate)
        cb = CFMessagePortGetInvalidationCallBack(port)

        # XXX: Without writing a custom wrapper we cannot guarantee this
        #self.failUnless(cb is invalidate)

        cb(None, None)
        self.failUnless(didInvalidate is True)
        didInvalidate = False

        rls = CFMessagePortCreateRunLoopSource(None, port, 0)
        self.failUnless(isinstance(rls, CFRunLoopSourceRef))

        self.failUnlessResultIsBOOL(CFMessagePortIsValid)
        self.failUnless(CFMessagePortIsValid(port))
        CFMessagePortInvalidate(port)
        self.failIf(CFMessagePortIsValid(port))
        self.failUnless(didInvalidate)

    @min_os_level('10.5')
    def testSending(self):
        # FIXME: Crash on Tiger
        context = []
        def callout(port, messageid, data, info):
            print "callout"
            info.append((port, messageid, data))
            return buffer("hello world")

        port, shouldFree = CFMessagePortCreateLocal(None, u"pyobjc.test", callout, context, None)
        self.failUnlessIsInstance(port, CFMessagePortRef)

        self.failUnlessArgIsOut(CFMessagePortSendRequest, 6)
        rls = CFMessagePortCreateRunLoopSource(None, port, 0)
        err, data = CFMessagePortSendRequest(port, 99, None, 1.0, 1.0, None, None)
        self.failUnlessEqual(err, 0)
        self.failUnlessEqual(data, None)


if __name__ == "__main__":
    main()
