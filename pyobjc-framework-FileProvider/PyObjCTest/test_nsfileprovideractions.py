from PyObjCTools.TestSupport import *

import FileProvider


class TestNSFileProviderActions(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.performActionWithIdentifier_onItemsWithIdentifiers_completionHandler_,
            2,
            b"v@",
        )
