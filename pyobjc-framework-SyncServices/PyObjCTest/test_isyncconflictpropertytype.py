
from PyObjCTools.TestSupport import *
import SyncServices

class TestISyncConflictPropertyTypeHelper (SyncServices.NSObject):
    def isRelationship(self): return 1
    def isToMany(self): return 1
    def isRequired(self): return 1

class TestISyncConflictPropertyType (TestCase):
    def testProtocols(self):
        objc.protocolNamed('ISyncConflictPropertyType')

        self.assertResultIsBOOL(TestISyncConflictPropertyTypeHelper.isRelationship)
        self.assertResultIsBOOL(TestISyncConflictPropertyTypeHelper.isToMany)
        self.assertResultIsBOOL(TestISyncConflictPropertyTypeHelper.isRequired)

if __name__ == "__main__":
    main()
