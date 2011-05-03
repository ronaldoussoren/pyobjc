import Foundation, objc
import AppKit
from Foundation import NSLog, NSAutoreleasePool, NSObject
from threading import Thread
import os
from PyObjCTools.TestSupport import *

class TestRegr (TestCase):
    def testFSRepr(self):
        fm = Foundation.NSFileManager.defaultManager()
        self.assertRaises(TypeError, fm.stringWithFileSystemRepresentation_length_, b"/var")
        self.assertEqual(u"/var", fm.stringWithFileSystemRepresentation_length_(b"/var/boo", 4))

    def testThreadHang(self):

        # Temporarily redirect stderr to a file, this allows us to check
        # that NSLog actually wrote some text.
        fp = os.open('/tmp/pyobjc-thread.txt', os.O_RDWR|os.O_CREAT, 0666)
        dupped = os.dup(2)
        os.dup2(fp, 2)

        try:

            class ThreadHangObject(NSObject):
                def init(self):
                    self.t = MyThread()
                    self.t.start()
                    return self

            aList = []
            class MyThread(Thread):
                def run(self):
                    pool = NSAutoreleasePool.alloc().init()
                    aList.append("before")
                    NSLog(u"does this print?")
                    aList.append("after")

            o = ThreadHangObject.alloc().init()
            o.t.join()


        finally:
            os.close(fp)
            os.dup2(dupped, 2)

        data = open('/tmp/pyobjc-thread.txt', 'r').read()
        self.assert_('does this print?' in data)

        self.assertEqual(aList, ["before", "after"])

    def testMemoryInit(self):
        """
        Regression test for bug #814683, that didn't initialize the memory
        space for output parameters correctly.
        """
        if not hasattr(Foundation, 'NSPropertyListSerialization'): return

        plist = 0

        r = Foundation.NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_(plist, Foundation.NSPropertyListXMLFormat_v1_0, None)
        self.assertEqual(r[1], None)
        r = Foundation.NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_(plist, Foundation.NSPropertyListXMLFormat_v1_0, None)
        self.assertEqual(r[1], None)

    def testTypeOverrideProblem(self):
        """
        A bug in the medatata machinery caused a crash.
        """
        cls = AppKit.NSOpenGLPixelFormat
        dir (cls)

        o = cls.alloc().initWithAttributes_(
                (AppKit.NSOpenGLPFAAccelerated,
                AppKit.NSOpenGLPFANoRecovery, AppKit.NSOpenGLPFAColorSize, 32))

if __name__ == "__main__":
    main()
