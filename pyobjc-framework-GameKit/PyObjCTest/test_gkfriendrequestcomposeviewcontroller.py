from PyObjCTools.TestSupport import *

import objc
import GameKit

class TestGKFriendRequestComposeViewController (TestCase):
    def testProtocols(self):
        objc.protocolNamed('GKFriendRequestComposeViewControllerDelegate')


if __name__ == "__main__":
    main()
