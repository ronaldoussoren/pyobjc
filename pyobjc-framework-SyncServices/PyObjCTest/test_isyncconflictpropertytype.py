import SyncServices
from PyObjCTools.TestSupport import TestCase


class TestISyncConflictPropertyTypeHelper(SyncServices.NSObject):
    def isRelationship(self):
        return 1

    def isToMany(self):
        return 1

    def isRequired(self):
        return 1


class TestISyncConflictPropertyType(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("ISyncConflictPropertyType", SyncServices)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestISyncConflictPropertyTypeHelper.isRelationship)
        self.assertResultIsBOOL(TestISyncConflictPropertyTypeHelper.isToMany)
        self.assertResultIsBOOL(TestISyncConflictPropertyTypeHelper.isRequired)
