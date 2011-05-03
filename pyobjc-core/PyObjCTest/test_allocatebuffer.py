from PyObjCTools.TestSupport import *

import objc
import sys

class TestAllocateBuffer(TestCase):
    def testBadLengths(self):
        self.assertRaises(ValueError, objc.allocateBuffer, 0)
        self.assertRaises(ValueError, objc.allocateBuffer, -1000)

    def testBuffer(self):
        b = objc.allocateBuffer(10000)
        self.assertEqual(len(b), 10000)

        if sys.version_info[0] == 2:
            for i in range(0,10000):
                b[i] = chr(i % 256)

            b[5:10] = b[1:6]
            b[5:10] = 'abcde'
            try:
                b[5:10] = 'abcdefghijk'
            except TypeError as r:
                if str(r).find("right operand length must match slice length") is not 0:
                    raise

        else:
            self.assertIsInstance(b, bytearray)

if __name__ == '__main__':
    main()
