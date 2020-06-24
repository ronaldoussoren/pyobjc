import CoreMedia
from PyObjCTools.TestSupport import TestCase


class TestCMBase(TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMPersistentTrackID_Invalid, 0)
