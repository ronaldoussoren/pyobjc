from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLResponse (TestCase):
    def testConstants(self):
        self.assertEqual(NSURLResponseUnknownLength, -1)

if __name__ == "__main__":
    main()
