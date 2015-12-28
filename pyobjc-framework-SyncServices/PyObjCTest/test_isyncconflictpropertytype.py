
from PyObjCTools.TestSupport import *
import SyncServices

class TestISyncConflictPropertyTypeHelper (SyncServices.NSObject):
    def isRelationship(self): return 1
    def isToMany(self): return 1
    def isRequired(self): return 1

class TestISyncConflictPropertyType (TestCase):
    def testProtocols(self):

        self.assertResultIsBOOL(TestISyncConflictPropertyTypeHelper.isRelationship)
        self.assertResultIsBOOL(TestISyncConflictPropertyTypeHelper.isToMany)
        self.assertResultIsBOOL(TestISyncConflictPropertyTypeHelper.isRequired)

    @min_os_level('10.7')
    def testProtocolObjects(self):
        objc.protocolNamed('ISyncConflictPropertyType')

if __name__ == "__main__":
    main()
