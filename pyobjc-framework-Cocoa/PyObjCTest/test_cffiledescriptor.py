"""
FIXME: None of these tests actually use the filedescriptor
"""

from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestFileDescriptor (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFFileDescriptorRef)

    def testTypeID(self):
        self.assertIsInstance(CFFileDescriptorGetTypeID(), (int, long))
    def testConstants(self):
        self.assertEqual(kCFFileDescriptorReadCallBack , 1 << 0)
        self.assertEqual(kCFFileDescriptorWriteCallBack , 1 << 1)
    def testInspection(self):
        def callout(fd, types, context):
            pass
        class Context: 
            pass
        context = Context()
        fd = CFFileDescriptorCreate(None, 0, False, callout, context)
        self.assertIsInstance(fd, CFFileDescriptorRef)
        self.assertEqual(CFFileDescriptorGetNativeDescriptor(fd) , 0)
        ctx = CFFileDescriptorGetContext(fd, None)
        self.assertIs(ctx, context)
        CFFileDescriptorEnableCallBacks(fd, kCFFileDescriptorReadCallBack)
        CFFileDescriptorDisableCallBacks(fd, kCFFileDescriptorReadCallBack|kCFFileDescriptorWriteCallBack)

        rls = CFFileDescriptorCreateRunLoopSource(None, fd, 0)
        self.assertIsInstance(rls, CFRunLoopSourceRef)
        self.assertTrue(CFFileDescriptorIsValid(fd))
        CFFileDescriptorInvalidate(fd)
        self.assertFalse(CFFileDescriptorIsValid(fd))

        self.assertResultIsBOOL(CFFileDescriptorIsValid)


if __name__ == "__main__":
    main()
