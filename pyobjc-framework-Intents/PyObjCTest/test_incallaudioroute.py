from PyObjCTools.TestSupport import TestCase
import Intents


class TestINCallAudioRoute(TestCase):
    def test_constants(self):
        self.assertEqual(Intents.INCallAudioRouteUnknown, 0)
        self.assertEqual(Intents.INCallAudioRouteSpeakerphoneAudioRoute, 1)
        self.assertEqual(Intents.INCallAudioRouteBluetoothAudioRoute, 2)
