import GameKit
import objc
from PyObjCTools.TestSupport import *


class TestGKEventListener(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKChallengeListener")


if __name__ == "__main__":
    main()
