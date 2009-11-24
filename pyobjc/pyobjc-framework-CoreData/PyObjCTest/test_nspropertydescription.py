
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSPropertyDescription (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSPropertyDescription.isOptional)
        self.failUnlessArgIsBOOL(NSPropertyDescription.setOptional_, 0)

        self.failUnlessResultIsBOOL(NSPropertyDescription.isTransient)
        self.failUnlessArgIsBOOL(NSPropertyDescription.setTransient_, 0)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessResultIsBOOL(NSPropertyDescription.isIndexed)
        self.failUnlessArgIsBOOL(NSPropertyDescription.setIndexed_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(NSPropertyDescription.isIndexedBySpotlight)
        self.failUnlessArgIsBOOL(NSPropertyDescription.setIndexedBySpotlight_, 0)
        self.failUnlessResultIsBOOL(NSPropertyDescription.isStoredInExternalRecord)
        self.failUnlessArgIsBOOL(NSPropertyDescription.setStoredInExternalRecord_, 0)

if __name__ == "__main__":
    main()
