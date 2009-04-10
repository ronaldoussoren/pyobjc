"""
FIXME: None of these tests actually use the filedescriptor
"""

from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestFileDescriptor (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFFileDescriptorRef)

    def testTypeID(self):
        self.failUnless(isinstance(CFFileDescriptorGetTypeID(), (int, long)))

    def testConstants(self):
        self.failUnless(kCFFileDescriptorReadCallBack == 1 << 0)
        self.failUnless(kCFFileDescriptorWriteCallBack == 1 << 1)


    def testInspection(self):
        def callout(fd, types, context):
            pass
        class Context: 
            pass
        context = Context()
        fd = CFFileDescriptorCreate(None, 0, False, callout, context)
        self.failUnless(isinstance(fd, CFFileDescriptorRef))

        self.failUnless(CFFileDescriptorGetNativeDescriptor(fd) == 0)

        ctx = CFFileDescriptorGetContext(fd)
        self.failUnless(ctx is context)

        CFFileDescriptorEnableCallBacks(fd, kCFFileDescriptorReadCallBack)
        CFFileDescriptorDisableCallBacks(fd, kCFFileDescriptorReadCallBack|kCFFileDescriptorWriteCallBack)

        rls = CFFileDescriptorCreateRunLoopSource(None, fd, 0)
        self.failUnless(isinstance(rls, CFRunLoopSourceRef))

        self.failUnless(CFFileDescriptorIsValid(fd))
        CFFileDescriptorInvalidate(fd)
        self.failIf(CFFileDescriptorIsValid(fd))

        self.failUnlessResultIsBOOL(CFFileDescriptorIsValid)


if __name__ == "__main__":
    main()
