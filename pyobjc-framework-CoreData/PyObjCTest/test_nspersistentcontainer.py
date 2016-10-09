from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSPersistentContainer (TestCase):
    @min_os_level('10.12')
    def testMethods(self):
        self.assertArgIsBlock(NSPersistentContainer.loadPersistentStoresWithCompletionHandler_, 0, b'v@@')
        self.assertArgIsBlock(NSPersistentContainer.performBackgroundTask_, 0, b'v')


if __name__ == "__main__":
    main()
