
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

if __name__ == "__main__":
    main()
