import CoreMedia
from PyObjCTools.TestSupport import TestCase
import objc


class TestCMAttachment(TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMAttachmentMode_ShouldNotPropagate, 0)
        self.assertEqual(CoreMedia.kCMAttachmentMode_ShouldPropagate, 1)

    def test_functions(self):
        self.assertArgHasType(CoreMedia.CMSetAttachment, 0, objc._C_ID)
        self.assertArgHasType(CoreMedia.CMSetAttachment, 2, objc._C_ID)

        self.assertResultHasType(CoreMedia.CMGetAttachment, objc._C_ID)
        self.assertArgHasType(CoreMedia.CMGetAttachment, 0, objc._C_ID)
        self.assertArgIsOut(CoreMedia.CMGetAttachment, 2, objc._C_ID)

        self.assertArgHasType(CoreMedia.CMRemoveAttachment, 0, objc._C_ID)
        self.assertArgHasType(CoreMedia.CMRemoveAllAttachments, 0, objc._C_ID)
        self.assertArgHasType(CoreMedia.CMCopyDictionaryOfAttachments, 1, objc._C_ID)
        self.assertArgHasType(CoreMedia.CMSetAttachments, 0, objc._C_ID)

        self.assertArgHasType(CoreMedia.CMPropagateAttachments, 0, objc._C_ID)
        self.assertArgHasType(CoreMedia.CMPropagateAttachments, 1, objc._C_ID)
