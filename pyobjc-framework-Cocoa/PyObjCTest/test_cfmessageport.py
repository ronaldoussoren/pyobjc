import CoreFoundation
from Foundation import NSData
import objc
from PyObjCTools.TestSupport import TestCase, NoObjCClass


class TestMessagePort(TestCase):
    def test_types(self):
        self.assertIsCFType(CoreFoundation.CFMessagePortRef)

    def test_constants(self):
        self.assertEqual(CoreFoundation.kCFMessagePortSuccess, 0)
        self.assertEqual(CoreFoundation.kCFMessagePortSendTimeout, -1)
        self.assertEqual(CoreFoundation.kCFMessagePortReceiveTimeout, -2)
        self.assertEqual(CoreFoundation.kCFMessagePortIsInvalid, -3)
        self.assertEqual(CoreFoundation.kCFMessagePortTransportError, -4)
        self.assertEqual(CoreFoundation.kCFMessagePortBecameInvalidError, -5)

    def test_typeid(self):
        self.assertIsInstance(CoreFoundation.CFMessagePortGetTypeID(), int)

    def test_interaction(self):
        class Context:
            pass

        context = Context()

        def callout(port, messageid, data, info):
            pass

        with self.assertRaisesRegex(TypeError, "expected 5 arguments, got 0"):
            CoreFoundation.CFMessagePortCreateLocal()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFMessagePortCreateLocal(
                NoObjCClass(), "name", callout, context, None
            )

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFMessagePortCreateLocal(
                None, NoObjCClass(), callout, context, None
            )

        with self.assertRaisesRegex(ValueError, "'shouldFree' should be None or NULL"):
            CoreFoundation.CFMessagePortCreateLocal(None, "name", callout, context, 42)

        port, shouldFree = CoreFoundation.CFMessagePortCreateLocal(
            None, "name", callout, context, None
        )
        self.assertIsInstance(port, CoreFoundation.CFMessagePortRef)
        self.assertIs(shouldFree is True or shouldFree, False)
        self.assertFalse(CoreFoundation.CFMessagePortIsRemote(port))

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            CoreFoundation.CFMessagePortGetContext()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFMessagePortGetContext(NoObjCClass(), None)

        with self.assertRaisesRegex(ValueError, "'context' must be None"):
            CoreFoundation.CFMessagePortGetContext(port, 42)

        ctx = CoreFoundation.CFMessagePortGetContext(port, None)
        self.assertIs(ctx, context)

        port2 = CoreFoundation.CFMessagePortCreateRemote(None, "name")
        self.assertIsInstance(port2, CoreFoundation.CFMessagePortRef)
        self.assertResultIsBOOL(CoreFoundation.CFMessagePortIsRemote)
        self.assertTrue(CoreFoundation.CFMessagePortIsRemote(port2))
        self.assertTrue(CoreFoundation.CFMessagePortGetName(port2), "name")

        CoreFoundation.CFMessagePortSetName(port2, "newname")
        self.assertTrue(CoreFoundation.CFMessagePortGetName(port2), "newname")

        cb = CoreFoundation.CFMessagePortGetInvalidationCallBack(port)
        self.assertIs(cb, None)
        global didInvalidate
        didInvalidate = False

        @objc.callbackFor(CoreFoundation.CFMessagePortSetInvalidationCallBack)
        def invalidate(port, info):
            global didInvalidate
            didInvalidate = True

        self.assertArgIsFunction(
            CoreFoundation.CFMessagePortSetInvalidationCallBack,
            1,
            b"v^{__CFMessagePort=}^v",
            True,
        )
        CoreFoundation.CFMessagePortSetInvalidationCallBack(port, invalidate)
        self.assertResultIsFunction(
            CoreFoundation.CFMessagePortGetInvalidationCallBack,
            b"v^{__CFMessagePort=}^v",
        )
        cb = CoreFoundation.CFMessagePortGetInvalidationCallBack(port)

        # XXX: Without writing a custom wrapper we cannot guarantee this
        # self.assertIs(cb, invalidate)
        cb(None, None)
        self.assertIs(didInvalidate, True)
        didInvalidate = False

        rls = CoreFoundation.CFMessagePortCreateRunLoopSource(None, port, 0)
        self.assertIsInstance(rls, CoreFoundation.CFRunLoopSourceRef)
        self.assertResultIsBOOL(CoreFoundation.CFMessagePortIsValid)
        self.assertTrue(CoreFoundation.CFMessagePortIsValid(port))
        CoreFoundation.CFMessagePortInvalidate(port)
        self.assertFalse(CoreFoundation.CFMessagePortIsValid(port))
        self.assertTrue(didInvalidate)

        port, shouldFree = CoreFoundation.CFMessagePortCreateLocal(
            None, "name", callout, context, objc.NULL
        )
        self.assertIsInstance(port, CoreFoundation.CFMessagePortRef)
        self.assertIs(shouldFree, objc.NULL)

        CoreFoundation.CFMessagePortInvalidate(port)

    def test_sending(self):
        curloop = CoreFoundation.CFRunLoopGetCurrent()
        context = []
        should_raise = False
        callback_return = b"hello world"

        def callout(port, messageid, data, info):
            if should_raise:
                raise RuntimeError("callback error")
            info.append((port, messageid, bytes(data), info))
            return callback_return

        port, shouldFree = CoreFoundation.CFMessagePortCreateLocal(
            None, "pyobjc.test", callout, context, None
        )
        self.assertIsInstance(port, CoreFoundation.CFMessagePortRef)

        self.assertArgIsOut(CoreFoundation.CFMessagePortSendRequest, 6)
        rls = CoreFoundation.CFMessagePortCreateRunLoopSource(None, port, 0)
        CoreFoundation.CFRunLoopAddSource(
            curloop, rls, CoreFoundation.kCFRunLoopCommonModes
        )

        try:
            cli = CoreFoundation.CFMessagePortCreateRemote(None, "pyobjc.test")
            self.assertIsInstance(cli, CoreFoundation.CFMessagePortRef)
            self.assertIsNot(rls, None)
            err, data = CoreFoundation.CFMessagePortSendRequest(
                cli,
                99,
                NSData.dataWithData_(b"message"),
                1.0,
                1.0,
                CoreFoundation.kCFRunLoopDefaultMode,
                None,
            )
            self.assertEqual(err, 0)
            self.assertEqual(data, b"hello world")

            should_raise = True
            with self.assertRaisesRegex(RuntimeError, "callback error"):
                err, data = CoreFoundation.CFMessagePortSendRequest(
                    cli,
                    100,
                    NSData.dataWithData_(b"message"),
                    1.0,
                    1.0,
                    CoreFoundation.kCFRunLoopDefaultMode,
                    None,
                )
            should_raise = False

            callback_return = NoObjCClass()
            with self.assertRaisesRegex(TypeError, "Cannot proxy"):
                err, data = CoreFoundation.CFMessagePortSendRequest(
                    cli,
                    101,
                    NSData.dataWithData_(b"message"),
                    1.0,
                    1.0,
                    CoreFoundation.kCFRunLoopDefaultMode,
                    None,
                )

            self.assertEqual(len(context), 2)
            self.assertIs(context[0][0], port)
            self.assertEqual(context[0][1], 99)
            self.assertEqual(bytes(context[0][2]), b"message")
            self.assertIs(context[0][3], context)

        finally:
            CoreFoundation.CFRunLoopRemoveSource(
                curloop, rls, CoreFoundation.kCFRunLoopCommonModes
            )
