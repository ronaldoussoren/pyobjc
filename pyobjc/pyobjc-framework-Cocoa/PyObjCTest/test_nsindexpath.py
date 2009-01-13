from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSIndexPath (TestCase):
    def testPointArguments(self):
        self.fail("indexPathWithIndexes:length:")
        self.fail("initWithIndexes:length:")
        self.fail("getIndexes:")

if __name__ == "__main__":
    main()
