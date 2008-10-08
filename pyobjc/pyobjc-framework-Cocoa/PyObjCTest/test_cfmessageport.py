import unittest
from CoreFoundation import *


class TestMessagePort (unittest.TestCase):
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

        self.failUnless(CFMessagePortIsValid(port))
        CFMessagePortInvalidate(port)
        self.failIf(CFMessagePortIsValid(port))
        self.failUnless(didInvalidate)

    def dont_testSending(self):
        context = []
        def callout(port, messageid, data, info):
            print "callout"
            info.append((port, messageid, data))
            return buffer("hello world")

        port, shouldFree = CFMessagePortCreateLocal(None, u"name", callout, context, None)

        err, data = CFMessagePortSendRequest(port, 42, buffer("hello moon"), 1.0, 1.0, kCFRunLoopDefaultMode, None)
        print err, data




if __name__ == "__main__":
    unittest.main()
