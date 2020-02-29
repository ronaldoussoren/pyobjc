from Foundation import NSNull
from PyObjCTools.TestSupport import *


class TestNSNull(TestCase):
    def testBool(self):
        v = NSNull.null()
        self.assertFalse(v)
        self.assertIsNot(v, None)


if __name__ == "__main__":
    main()
