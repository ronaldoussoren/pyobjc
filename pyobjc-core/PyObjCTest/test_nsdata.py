from PyObjCTools.TestSupport import *
import objc
import sys

class TestNSDataSupport (TestCase):
    # XXX: migrate test cases from Cocoa bindings!
    def testEmptyRoBuffer(self):
        cls = objc.lookUpClass('NSData')
        buf = cls.alloc().init()
        self.assertEqual(len(buf), 0)

        if sys.version_info[0] == 3:
            self.assertEqual(buf.bytes(), b"")
        else:
            self.assertEqual(buf.bytes(), buffer(b""))


    def no_testEmptyRwBuffer(self):
        cls = objc.lookUpClass('NSMutableData')
        buf = cls.alloc().init()
        self.assertEqual(len(buf), 0)

        self.assertRaises(ValueError, buf.mutableBytes)

if __name__ == "__main__":
    main()
