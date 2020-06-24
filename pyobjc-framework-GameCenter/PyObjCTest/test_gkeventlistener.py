import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

import GameCenter  # noqa: F401


class TestGKEventListener(TestCase):
    @min_os_level("10.10")
    def testProtocols(self):
        objc.protocolNamed("GKChallengeListener")
