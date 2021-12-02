import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioTypes(TestCase):
    @min_os_level("10.7")
    def testStructs(self):
        v = AVFoundation.AVAudio3DPoint()
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)
        self.assertIsInstance(v.z, float)
        self.assertPickleRoundTrips(v)

        self.assertTrue(AVFoundation.AVAudio3DVector, AVFoundation.AVAudio3DPoint)

        v = AVFoundation.AVAudio3DVectorOrientation()
        self.assertIsInstance(v.forward, AVFoundation.AVAudio3DVector)
        self.assertIsInstance(v.up, AVFoundation.AVAudio3DVector)
        self.assertPickleRoundTrips(v)

        v = AVFoundation.AVAudio3DAngularOrientation()
        self.assertIsInstance(v.yaw, float)
        self.assertIsInstance(v.pitch, float)
        self.assertIsInstance(v.roll, float)
        self.assertPickleRoundTrips(v)

    @min_os_level("10.10")
    def testFunctions(self):
        v = AVFoundation.AVAudioMake3DPoint(1.5, 2.5, 3.5)
        self.assertIsInstance(v, AVFoundation.AVAudio3DPoint)
        self.assertEqual(v.x, 1.5)
        self.assertEqual(v.y, 2.5)
        self.assertEqual(v.z, 3.5)

        v = AVFoundation.AVAudioMake3DVector(1.5, 2.5, 3.5)
        self.assertIsInstance(v, AVFoundation.AVAudio3DVector)
        self.assertEqual(v.x, 1.5)
        self.assertEqual(v.y, 2.5)
        self.assertEqual(v.z, 3.5)

        x = AVFoundation.AVAudioMake3DVector(1.5, 2.5, 3.5)
        y = AVFoundation.AVAudioMake3DVector(2.5, 3.5, 4.5)
        v = AVFoundation.AVAudioMake3DVectorOrientation(x, y)
        self.assertIsInstance(v, AVFoundation.AVAudio3DVectorOrientation)
        self.assertEqual(v.forward, x)
        self.assertEqual(v.up, y)

        v = AVFoundation.AVAudioMake3DAngularOrientation(1.5, 2.5, 3.5)
        self.assertIsInstance(v, AVFoundation.AVAudio3DAngularOrientation)
        self.assertEqual(v.yaw, 1.5)
        self.assertEqual(v.pitch, 2.5)
        self.assertEqual(v.roll, 3.5)
