import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

import GameCenter  # noqa: F401


class TestGKSavedGameListener(TestCase):
    @min_os_level("10.10")
    def testProtocols(self):
        objc.protocolNamed("GKSavedGameListener")
