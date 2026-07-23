import CoreFoundation
from PyObjCTools.TestSupport import TestCase, NoObjCClass, NotBool
import tempfile
from .runloophelper import check_cfrunloop_side_effects


class TestFileDescriptor(TestCase):
    def test_types(self):
        self.assertIsCFType(CoreFoundation.CFFileDescriptorRef)

    def test_typeid(self):
        self.assertIsInstance(CoreFoundation.CFFileDescriptorGetTypeID(), int)

    def test_constants(self):
        self.assertEqual(CoreFoundation.kCFFileDescriptorReadCallBack, 1 << 0)
        self.assertEqual(CoreFoundation.kCFFileDescriptorWriteCallBack, 1 << 1)

    @check_cfrunloop_side_effects
    def test_inspect(self):
        with tempfile.TemporaryFile() as stream:
            stream.write(b"hello world\n")
            stream.flush()
            stream.seek(0)

            lst = []

            def callout(fd, types, context):
                lst.append((fd, types, context))

            context = object()

            with self.assertRaisesRegex(TypeError, "expected 5 arguments, got 1"):
                CoreFoundation.CFFileDescriptorCreate(None)

            with self.assertRaisesRegex(TypeError, "Cannot proxy"):
                CoreFoundation.CFFileDescriptorCreate(
                    NoObjCClass(), 0, False, callout, context
                )

            with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
                CoreFoundation.CFFileDescriptorCreate(
                    None, "stdin", False, callout, context
                )

            with self.assertRaisesRegex(TypeError, "this is not a bool"):
                CoreFoundation.CFFileDescriptorCreate(
                    None, 0, NotBool(), callout, context
                )

            fd = CoreFoundation.CFFileDescriptorCreate(
                None, stream.fileno(), False, callout, context
            )
            self.assertIsInstance(fd, CoreFoundation.CFFileDescriptorRef)
            self.assertEqual(
                CoreFoundation.CFFileDescriptorGetNativeDescriptor(fd), stream.fileno()
            )

            with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 1"):
                CoreFoundation.CFFileDescriptorGetContext(None)

            with self.assertRaisesRegex(TypeError, "Cannot proxy"):
                CoreFoundation.CFFileDescriptorGetContext(NoObjCClass(), None)

            with self.assertRaisesRegex(ValueError, "'context' must be None"):
                CoreFoundation.CFFileDescriptorGetContext(fd, 42)

            ctx = CoreFoundation.CFFileDescriptorGetContext(fd, None)
            self.assertIs(ctx, context)
            CoreFoundation.CFFileDescriptorEnableCallBacks(
                fd, CoreFoundation.kCFFileDescriptorReadCallBack
            )
            CoreFoundation.CFFileDescriptorDisableCallBacks(
                fd,
                CoreFoundation.kCFFileDescriptorReadCallBack
                | CoreFoundation.kCFFileDescriptorWriteCallBack,
            )

            rls = CoreFoundation.CFFileDescriptorCreateRunLoopSource(None, fd, 0)
            self.assertIsInstance(rls, CoreFoundation.CFRunLoopSourceRef)
            self.assertTrue(CoreFoundation.CFFileDescriptorIsValid(fd))

            self.assertResultIsBOOL(CoreFoundation.CFFileDescriptorIsValid)

            CoreFoundation.CFFileDescriptorEnableCallBacks(
                fd, CoreFoundation.kCFFileDescriptorReadCallBack
            )

            self.assertEqual(lst, [])

            rl = CoreFoundation.CFRunLoopGetCurrent()
            CoreFoundation.CFRunLoopAddSource(
                rl, rls, CoreFoundation.kCFRunLoopDefaultMode
            )
            CoreFoundation.CFRunLoopRunInMode(
                CoreFoundation.kCFRunLoopDefaultMode, 0.5, False
            )

            self.assertEqual(len(lst), 1)
            self.assertEqual(
                lst[0], (fd, CoreFoundation.kCFFileDescriptorReadCallBack, context)
            )

            CoreFoundation.CFFileDescriptorEnableCallBacks(
                fd, CoreFoundation.kCFFileDescriptorWriteCallBack
            )
            lst = None

            with self.assertRaisesRegex(
                AttributeError, "'NoneType' object has no attribute 'append'"
            ):
                CoreFoundation.CFRunLoopRunInMode(
                    CoreFoundation.kCFRunLoopDefaultMode, 0.5, False
                )

            CoreFoundation.CFRunLoopRemoveSource(
                rl, rls, CoreFoundation.kCFRunLoopDefaultMode
            )

            CoreFoundation.CFFileDescriptorInvalidate(fd)
            self.assertFalse(CoreFoundation.CFFileDescriptorIsValid(fd))
