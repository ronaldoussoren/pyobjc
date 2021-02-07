from PyObjCTools.TestSupport import TestCase
import objc

import GameplayKit  # noqa: F401


class TestGKStrategist(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKStrategist")
