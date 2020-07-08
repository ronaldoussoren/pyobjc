from PyObjCTools.TestSupport import TestCase

import ReplayKit
import objc


class TestRPBroadcast(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            ReplayKit.RPBroadcastActivityController.showBroadcastPickerAtPoint_fromWindow_preferredExtensionIdentifier_completionHandler_,  # noqa: B950
            3,
            b"v@@",
        )

        self.assertResultIsBOOL(ReplayKit.RPBroadcastController.isBroadcasting)
        self.assertResultIsBOOL(ReplayKit.RPBroadcastController.isPaused)

        self.assertArgIsBlock(
            ReplayKit.RPBroadcastController.startBroadcastWithHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            ReplayKit.RPBroadcastController.finishBroadcastWithHandler_, 0, b"v@"
        )

    def test_protocols(self):
        objc.protocolNamed("RPBroadcastActivityControllerDelegate")
        objc.protocolNamed("RPBroadcastControllerDelegate")
