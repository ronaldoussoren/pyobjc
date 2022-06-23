from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKAttachmentStore(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKAttachmentStore.addAttachmentToObject_name_contentType_URL_metadata_completion_,
            5,
            b"v@@",
        )
        self.assertArgIsBlock(
            HealthKit.HKAttachmentStore.removeAttachment_fromObject_completion_,
            2,
            b"vZ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKAttachmentStore.getAttachmentsForObject_completion_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            HealthKit.HKAttachmentStore.getDataForAttachment_completion_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            HealthKit.HKAttachmentStore.streamDataForAttachment_dataHandler_, 1, b"v@@Z"
        )
