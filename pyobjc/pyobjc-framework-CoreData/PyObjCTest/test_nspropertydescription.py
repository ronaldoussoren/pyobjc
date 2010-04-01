
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSPropertyDescription (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSPropertyDescription.isOptional)
        self.assertArgIsBOOL(NSPropertyDescription.setOptional_, 0)

        self.assertResultIsBOOL(NSPropertyDescription.isTransient)
        self.assertArgIsBOOL(NSPropertyDescription.setTransient_, 0)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertResultIsBOOL(NSPropertyDescription.isIndexed)
        self.assertArgIsBOOL(NSPropertyDescription.setIndexed_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSPropertyDescription.isIndexedBySpotlight)
        self.assertArgIsBOOL(NSPropertyDescription.setIndexedBySpotlight_, 0)
        self.assertResultIsBOOL(NSPropertyDescription.isStoredInExternalRecord)
        self.assertArgIsBOOL(NSPropertyDescription.setStoredInExternalRecord_, 0)

if __name__ == "__main__":
    main()
