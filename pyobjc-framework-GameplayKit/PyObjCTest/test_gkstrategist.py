from PyObjCTools.TestSupport import TestCase

import GameplayKit  # noqa: F401


class TestGKStrategist(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("GKStrategist", GameplayKit)
