import Foundation, objc
import AppKit
from Foundation import NSLog, NSAutoreleasePool, NSObject
from threading import Thread
import os
import unittest

class ReturnAStruct (NSObject):
    def someRectWithRect_(self, ((x, y), (h, w))):
        return ((x,y),(h,w))
    someRectWithRect_ = objc.selector(someRectWithRect_,
        signature='{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}')


class TestRegr (unittest.TestCase):
    def testFSRepr(self):
        fm = Foundation.NSFileManager.defaultManager()
        self.assertRaises(TypeError, fm.stringWithFileSystemRepresentation_length_, "/var")
        self.assertEquals(u"/var", fm.stringWithFileSystemRepresentation_length_("/var/boo", 4))

    def testStructReturnPy(self):
        # XXX: remove dependency on objc.test!
        from objc.test.structargs import StructArgClass
        o = ReturnAStruct.alloc().init()
        p = StructArgClass.alloc().init()

        v = p.someRectWithObject_X_Y_H_W_(o, 1, 2, 3, 4)
        self.assert_(isinstance(v, Foundation.NSRect))
        self.assertEquals(v, ((1,2),(3,4)))

    def testStructReturn(self):
        from objc.test.structargs import StructArgClass        
        o = StructArgClass.alloc().init()
        v = o.someRect()
        self.assertEquals(v, ((1,2),(3,4)))


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

        self.assertEquals(aList, ["before", "after"])

    def testMemoryInit(self):
        """
        Regression test for bug #814683, that didn't initialize the memory
        space for output parameters correctly.
        """
        if not hasattr(Foundation, 'NSPropertyListSerialization'): return

        plist = 0

        r = Foundation.NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_(plist, Foundation.NSPropertyListXMLFormat_v1_0, None)
        self.assertEquals(r[1], None)
        r = Foundation.NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_(plist, Foundation.NSPropertyListXMLFormat_v1_0, None)
        self.assertEquals(r[1], None)

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
    unittest.main()
