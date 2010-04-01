
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSEntityDescription (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSEntityDescription.isAbstract)
        self.assertArgIsBOOL(NSEntityDescription.setAbstract_, 0)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(NSEntityDescription.isKindOfEntity_)


if __name__ == "__main__":
    main()
