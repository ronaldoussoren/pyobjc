from PyObjCTools.TestSupport import TestCase, min_os_level

import FSKit


class TestFSTask(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBlock(FSKit.FSTask.cancellationHandler, b"@")
        self.assertArgIsBlock(FSKit.FSTask.setCancellationHandler_, 0, b"@")
