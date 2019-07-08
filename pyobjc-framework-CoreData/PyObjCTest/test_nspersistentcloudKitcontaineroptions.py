
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSPersistentCloudKitContainerOptions (TestCase):
    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(NSPersistentCloudKitContainerOptions.shouldInitializeSchema)
        self.assertArgIsBOOL(NSPersistentCloudKitContainerOptions.setShouldInitializeSchema_, 0)


if __name__ == "__main__":
    main()
