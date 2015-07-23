from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSPersistentStoreRequest (TestCase):
    def testConstants(self):
        self.assertEqual(NSFetchRequestType, 1)
        self.assertEqual(NSSaveRequestType, 2)
        self.assertEqual(NSBatchUpdateRequestType, 6)
        self.assertEqual(NSBatchDeleteRequestType, 7)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsBlock(NSAsynchronousFetchRequest.initWithFetchRequest_completionBlock_, 1, b'v@')
        self.assertResultIsBlock(NSAsynchronousFetchRequest.completionBlock, b'v@')

if __name__ == "__main__":
    main()
