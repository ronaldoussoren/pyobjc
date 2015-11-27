from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioMixingHelper (AVFoundation.NSObject):
    def destinationForMixer_bus_(self, a, b): return 1
    def setVolume_(self, a): pass
    def setPan_(self, a): pass
    def setRenderingAlgorithm_(self, a): pass
    def setRate_(self, a): pass
    def setReverbBlend_(self, a): pass
    def setObstruction_(self, a): pass
    def setOcclusion_(self, a): pass
    def setPosition_(self, a): pass
    def volume(self): return 1
    def pan(self): return 1
    def renderingAlgorithm(self): return 1
    def rate(self): return 1
    def reverbBlend(self): return 1
    def obstruction(self): return 1
    def occlusion(self): return 1
    def position(self): return 1



class TestAkAudioMixing (TestCase):
    def testMethods(self):
        self.assertArgHasType(TestAVAudioMixingHelper.destinationForMixer_bus_, 1, objc._C_NSUInteger)

        self.assertArgHasType(TestAVAudioMixingHelper.setVolume_, 0, objc._C_FLT)
        self.assertResultHasType(TestAVAudioMixingHelper.volume, objc._C_FLT)

        self.assertArgHasType(TestAVAudioMixingHelper.setPan_, 0, objc._C_FLT)
        self.assertResultHasType(TestAVAudioMixingHelper.pan, objc._C_FLT)

        self.assertArgHasType(TestAVAudioMixingHelper.setRenderingAlgorithm_, 0, objc._C_NSInteger)
        self.assertResultHasType(TestAVAudioMixingHelper.renderingAlgorithm, objc._C_NSInteger)

        self.assertArgHasType(TestAVAudioMixingHelper.setRate_, 0, objc._C_FLT)
        self.assertResultHasType(TestAVAudioMixingHelper.rate, objc._C_FLT)

        self.assertArgHasType(TestAVAudioMixingHelper.setReverbBlend_, 0, objc._C_FLT)
        self.assertResultHasType(TestAVAudioMixingHelper.reverbBlend, objc._C_FLT)

        self.assertArgHasType(TestAVAudioMixingHelper.setObstruction_, 0, objc._C_FLT)
        self.assertResultHasType(TestAVAudioMixingHelper.obstruction, objc._C_FLT)

        self.assertArgHasType(TestAVAudioMixingHelper.setOcclusion_, 0, objc._C_FLT)
        self.assertResultHasType(TestAVAudioMixingHelper.occlusion, objc._C_FLT)

        self.assertArgHasType(TestAVAudioMixingHelper.setPosition_, 0, AVFoundation.AVAudio3DPoint.__typestr__)
        self.assertResultHasType(TestAVAudioMixingHelper.position, AVFoundation.AVAudio3DPoint.__typestr__)

    def testConstants(self):
        self.assertEqual(AVFoundation.AVAudio3DMixingRenderingAlgorithmEqualPowerPanning, 0)
        self.assertEqual(AVFoundation.AVAudio3DMixingRenderingAlgorithmSphericalHead, 1)
        self.assertEqual(AVFoundation.AVAudio3DMixingRenderingAlgorithmHRTF, 2)
        self.assertEqual(AVFoundation.AVAudio3DMixingRenderingAlgorithmSoundField, 3)
        self.assertEqual(AVFoundation.AVAudio3DMixingRenderingAlgorithmStereoPassThrough, 5)


if __name__ == "__main__":
    main()
