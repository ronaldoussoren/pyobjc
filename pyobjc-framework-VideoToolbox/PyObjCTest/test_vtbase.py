import VideoToolbox
from PyObjCTools.TestSupport import TestCase


class TestVTBase(TestCase):
    def test_structs(self):
        v = VideoToolbox.VTInt32Point()
        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 0)
        self.assertPickleRoundTrips(v)

        v = VideoToolbox.VTInt32Size()
        self.assertEqual(v.width, 0)
        self.assertEqual(v.height, 0)
        self.assertPickleRoundTrips(v)
