from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit

CKSharePreparationCompletionHandler = b"v@@"
CKSharePreparationHandler = b"v@@?"  # XXX: Block has type ^^^


class TestNSItemProvider_CKSharingSupport(TestCase):
    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertArgIsBlock(
            CloudKit.NSItemProvider.registerCKShareWithContainer_allowedSharingOptions_preparationHandler_,
            2,
            CKSharePreparationHandler,
        )
