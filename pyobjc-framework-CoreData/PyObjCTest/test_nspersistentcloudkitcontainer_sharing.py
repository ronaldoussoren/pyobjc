import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPersistentCloudKitContainer_Sharing(TestCase):
    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBlock(
            CoreData.NSPersistentCloudKitContainer.acceptShareInvitationsFromMetadata_intoPersistentStore_completion_,
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            CoreData.NSPersistentCloudKitContainer.purgeObjectsAndRecordsInZoneWithID_inPersistentStore_completion_,
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            CoreData.NSPersistentCloudKitContainer.persistUpdatedShare_inPersistentStore_completion_,
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            CoreData.NSPersistentCloudKitContainer.fetchParticipantsMatchingLookupInfos_intoPersistentStore_completion_,
            2,
            b"v@@",
        )

        self.assertArgIsOut(
            CoreData.NSPersistentCloudKitContainer.fetchSharesMatchingObjectIDs_error_,
            1,
        )
        self.assertArgIsOut(
            CoreData.NSPersistentCloudKitContainer.fetchSharesInPersistentStore_error_,
            1,
        )

        self.assertArgIsBlock(
            CoreData.NSPersistentCloudKitContainer.shareManagedObjects_toShare_completion_,
            2,
            b"v@@@@",
        )
