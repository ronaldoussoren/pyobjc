import sys
from PyObjCTools.TestSupport import *
from PyObjCTest.voidpointer import OC_TestVoidPointer


class TestVoidPointer(TestCase):
    def testVoidPointerMethods(self):
        o = OC_TestVoidPointer.alloc().init()
        self.assertEqual(o.getvalue(), 0)

        o.setvalue_(523_532)
        self.assertEqual(o.getvalue(), 523_532)

        o.setvalue_(sys.maxsize + 1)
        self.assertEqual(o.getvalue(), sys.maxsize + 1)


if __name__ == "__main__":
    main()
