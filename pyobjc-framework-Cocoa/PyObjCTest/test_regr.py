import os
from threading import Thread

import AppKit
import Foundation
from Foundation import NSAutoreleasePool, NSLog, NSObject
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestRegr(TestCase):
    def testFSRepr(self):
        fm = Foundation.NSFileManager.defaultManager()
        self.assertRaises(
            TypeError, fm.stringWithFileSystemRepresentation_length_, b"/var"
        )
        self.assertEqual(
            "/var", fm.stringWithFileSystemRepresentation_length_(b"/var/boo", 4)
        )

    def testThreadHang(self):

        # Temporarily redirect stderr to a file, this allows us to check
        # that NSLog actually wrote some text.
        fp = os.open("/tmp/pyobjc-thread.txt", os.O_RDWR | os.O_CREAT, 0o666)
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
                    pool = NSAutoreleasePool.alloc().init()  # noqa: F841
                    aList.append("before")
                    NSLog("does this print?")
                    aList.append("after")

            o = ThreadHangObject.alloc().init()
            o.t.join()

        finally:
            os.close(fp)
            os.dup2(dupped, 2)

        with open("/tmp/pyobjc-thread.txt") as fp:
            data = fp.read()
        self.assertTrue("does this print?" in data)

        self.assertEqual(aList, ["before", "after"])

    def testMemoryInit(self):
        """
        Regression test for bug #814683, that didn't initialize the memory
        space for output parameters correctly.
        """
        if not hasattr(Foundation, "NSPropertyListSerialization"):
            return

        plist = 0

        r = Foundation.NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_(  # noqa: B950
            plist, Foundation.NSPropertyListXMLFormat_v1_0, None
        )
        self.assertEqual(r[1], None)
        r = Foundation.NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_(  # noqa: B950
            plist, Foundation.NSPropertyListXMLFormat_v1_0, None
        )
        self.assertEqual(r[1], None)

    def testTypeOverrideProblem(self):
        """
        A bug in the medatata machinery caused a crash.
        """
        cls = AppKit.NSOpenGLPixelFormat
        dir(cls)

        _ = cls.alloc().initWithAttributes_(
            (
                AppKit.NSOpenGLPFAAccelerated,
                AppKit.NSOpenGLPFANoRecovery,
                AppKit.NSOpenGLPFAColorSize,
                32,
            )
        )

    @min_os_level("10.6")
    def testBinaryPlist(self):
        for pl in ({"key": 2**64 - 1}, {"key": 2**16 - 1}):
            with self.subTest(pl):
                (
                    data,
                    error,
                ) = Foundation.NSPropertyListSerialization.dataWithPropertyList_format_options_error_(  # noqa: B950
                    pl, Foundation.NSPropertyListBinaryFormat_v1_0, 0, None
                )
            (
                restored,
                plformat,
                error,
            ) = Foundation.NSPropertyListSerialization.propertyListWithData_options_format_error_(  # noqa: B950
                data, 0, None, None
            )
            self.assertEqual(pl, restored)
