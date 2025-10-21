from PyObjCTools.TestSupport import TestCase, min_sdk_level

import AVRouting  # noqa: F401


class TestAVRoutingPlaybackArbiter(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("AVRoutingPlaybackParticipant")
