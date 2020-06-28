from PyObjCTools.TestSupport import TestCase

import ReplayKit
import objc


class TestRPBroadcast(TestCase):
    def test_methods(self):
        self.asssertArgIsBlock(
            ReplayKit.RPBroadcastActivityController.showBroadcastPickerAtPoint_fromWindow_preferredExtensionIdentifier_completionHandler_,  # noqa: B950
            3,
            b"v@@",
        )

        self.asssertResultIsBOOL(ReplayKit.RPBroadcastController.isBroadcasting)
        self.asssertResultIsBOOL(ReplayKit.RPBroadcastController.isPaused)

        self.asssertArgIsBlock(
            ReplayKit.RPBroadcastController.startBroadcastWithHandler_, 0, b"v@"
        )
        self.asssertArgIsBlock(
            ReplayKit.RPBroadcastController.finishBroadcastWithHandler_, 0, b"v@"
        )

    def test_protocols(self):
        objc.protocolNamed("RPBroadcastActivityControllerDelegate")
        objc.protocolNamed("RPBroadcastControllerDelegate")
