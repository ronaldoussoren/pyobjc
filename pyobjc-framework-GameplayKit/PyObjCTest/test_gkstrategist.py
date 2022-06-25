from PyObjCTools.TestSupport import TestCase

import GameplayKit  # noqa: F401


class TestGKStrategist(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("GKStrategist")
