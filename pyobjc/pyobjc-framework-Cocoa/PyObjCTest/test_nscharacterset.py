from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSCharacterSet (TestCase):
    def testConstants(self):
        self.assertEquals( NSOpenStepUnicodeReservedBase, 0xF400 )

if __name__ == "__main__":
    main()
