from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSMessageConnection(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            FSKit.FSMessageConnection.didCompleteWithError_completionHandler_, 1, b"v@"
        )
