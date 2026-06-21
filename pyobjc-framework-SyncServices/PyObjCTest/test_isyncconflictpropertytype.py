import SyncServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestISyncConflictPropertyTypeHelper(SyncServices.NSObject):
    def isRelationship(self):
        return 1

    def isToMany(self):
        return 1

    def isRequired(self):
        return 1


class TestISyncConflictPropertyType(TestCase):
    def test_protocols(self):
        self.assertResultIsBOOL(TestISyncConflictPropertyTypeHelper.isRelationship)
        self.assertResultIsBOOL(TestISyncConflictPropertyTypeHelper.isToMany)
        self.assertResultIsBOOL(TestISyncConflictPropertyTypeHelper.isRequired)

    @min_os_level("10.7")
    def test_protocols10_7(self):
        self.assertProtocolExists("ISyncConflictPropertyType", SyncServices)
