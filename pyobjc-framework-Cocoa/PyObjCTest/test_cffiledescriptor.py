import CoreFoundation
from PyObjCTools.TestSupport import TestCase


class TestFileDescriptor(TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFFileDescriptorRef)

    def testTypeID(self):
        self.assertIsInstance(CoreFoundation.CFFileDescriptorGetTypeID(), int)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFFileDescriptorReadCallBack, 1 << 0)
        self.assertEqual(CoreFoundation.kCFFileDescriptorWriteCallBack, 1 << 1)

    def testInspection(self):
        def callout(fd, types, context):
            pass

        class Context:
            pass

        context = Context()
        fd = CoreFoundation.CFFileDescriptorCreate(None, 0, False, callout, context)
        self.assertIsInstance(fd, CoreFoundation.CFFileDescriptorRef)
        self.assertEqual(CoreFoundation.CFFileDescriptorGetNativeDescriptor(fd), 0)
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
        CoreFoundation.CFFileDescriptorInvalidate(fd)
        self.assertFalse(CoreFoundation.CFFileDescriptorIsValid(fd))

        self.assertResultIsBOOL(CoreFoundation.CFFileDescriptorIsValid)
