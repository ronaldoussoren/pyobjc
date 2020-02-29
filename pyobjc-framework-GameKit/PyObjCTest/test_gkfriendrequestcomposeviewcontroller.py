import GameKit
import objc
from PyObjCTools.TestSupport import *


class TestGKFriendRequestComposeViewController(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKFriendRequestComposeViewControllerDelegate")


if __name__ == "__main__":
    main()
