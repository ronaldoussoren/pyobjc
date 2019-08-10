from PyObjCTools.TestSupport import *

import FileProvider


class TestNSFileProviderMaterializedSet(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            FileProvider.NSFileProviderExtension.materializedItemsDidChangeWithCompletionHandler_,
            0,
            b"v",
        )
