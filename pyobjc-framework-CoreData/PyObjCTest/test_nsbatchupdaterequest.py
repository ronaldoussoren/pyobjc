from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSBatchUpdateRequest (TestCase):

    @min_os_level('10.10')
    def testMethods(self):
        self.assertResultIsBOOL(NSBatchUpdateRequest.includesSubentities)
        self.assertArgIsBOOL(NSBatchUpdateRequest.setIncludesSubentities_, 0)

if __name__ == "__main__":
    main()
