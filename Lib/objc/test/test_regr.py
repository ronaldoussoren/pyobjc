import unittest

import objc

NSObject = objc.lookUpClass('NSObject')

class TestRegressions(unittest.TestCase):
    def testNSObjectRespondsToCommonMethods(self):
        self.assert_(NSObject.pyobjc_classMethods.respondsToSelector_('alloc'))
        self.assert_(NSObject.instancesRespondToSelector_('init'))
        self.assert_(not NSObject.instancesRespondToSelector_('frodel'))


    def testFSRepr(self):
        import Foundation
        fm = Foundation.NSFileManager.defaultManager()
        self.assertRaises(TypeError, fm.stringWithFileSystemRepresentation_length_, "/var")
        self.assertEquals(u"/var", fm.stringWithFileSystemRepresentation_length_("/var/boo", 4))

    def testMemoryInit(self):
        """
        Regression test for bug #814683, that didn't initialize the memory
        space for output parameters correctly.
        """
        import Foundation
        if not hasattr(Foundation, 'NSPropertyListSerialization'): return

        plist = 0

        r = Foundation.NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_(plist, Foundation.NSPropertyListXMLFormat_v1_0)
        self.assertEquals(r[1], None)
        r = Foundation.NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_(plist, Foundation.NSPropertyListXMLFormat_v1_0)
        self.assertEquals(r[1], None)


    def testDeallocUninit(self):
        import objc

        import warnings
        warnings.filterwarnings('ignore',
            category=objc.UninitializedDeallocWarning)

        try:
            for clsName in [ 'NSURL', 'NSObject', 'NSArray' ]:
                d = objc.lookUpClass(clsName).alloc()
                del d

        finally:
            del warnings.filters[0]

        # Check that we generate a warning for unitialized objects that
        # get deallocated
        import sys
        import StringIO
        warnings.filterwarnings('always',
            category=objc.UninitializedDeallocWarning)
        sys.stderr = io = StringIO.StringIO()
        try:
            d = NSObject.alloc()
            del d

        finally:
            del warnings.filters[0]
            sys.stderr = sys.__stderr__

        # A warning is three lines: location info, source code, empty line
        self.assertEquals(len(io.getvalue().split('\n')), 3)

    def testThreadHang(self):
        from Foundation import NSLog, NSAutoreleasePool, NSObject
        import AppKit
        from threading import Thread
        import os

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
                    NSLog("does this print?")
                    aList.append("after")

            o = ThreadHangObject.alloc().init()
            o.t.join()

            self.assertEquals(aList, ["before", "after"])

        finally:
            os.close(fp)
            os.dup2(dupped, 2)

        data = open('/tmp/pyobjc-thread.txt', 'r').read()
        self.assert_('does this print?' in data)

    def testOneWayMethods(self):
        # This one should be in test_methods*.py
        from objc.test.initialize import OC_TestInitialize

        o = OC_TestInitialize.alloc().init()
        self.assertEquals(objc.splitSignature(o.onewayVoidMethod.signature), (objc._C_ONEWAY + objc._C_VOID, objc._C_ID, objc._C_SEL))

        # Make sure we can call the method
        o.onewayVoidMethod()
        self.assertEquals(o.isInitialized(), -1)


if __name__ == '__main__':
    unittest.main()
