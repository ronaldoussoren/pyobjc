import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestAVAudioMixingHelper(AVFoundation.NSObject):
    def destinationForMixer_bus_(self, a, b):
        return 1

    def volume(self):
        return 1

    def setVolume_(self, a):
        pass

    def pan(self):
        return 1

    def setPan_(self, a):
        pass

    def renderingAlgorithm(self):
        return 1

    def setRenderingAlgorithm_(self, a):
        pass

    def rate(self):
        return 1

    def setRate_(self, a):
        pass

    def reverbBlend(self):
        return 1

    def setReverbBlend_(self, a):
        pass

    def obstruction(self):
        return 1

    def setObstruction_(self, a):
        pass

    def occlusion(self):
        return 1

    def setOcclusion_(self, a):
        pass

    def position(self):
        return 1

    def setPosition_(self, a):
        pass


class TestAkAudioMixing(TestCase):
    def testMethods(self):
        self.assertArgHasType(
            TestAVAudioMixingHelper.destinationForMixer_bus_, 1, objc._C_NSUInteger
        )

        self.assertArgHasType(TestAVAudioMixingHelper.setVolume_, 0, objc._C_FLT)
        self.assertResultHasType(TestAVAudioMixingHelper.volume, objc._C_FLT)

        self.assertArgHasType(TestAVAudioMixingHelper.setPan_, 0, objc._C_FLT)
        self.assertResultHasType(TestAVAudioMixingHelper.pan, objc._C_FLT)

        self.assertArgHasType(
            TestAVAudioMixingHelper.setRenderingAlgorithm_, 0, objc._C_NSInteger
        )
        self.assertResultHasType(
            TestAVAudioMixingHelper.renderingAlgorithm, objc._C_NSInteger
        )

        self.assertArgHasType(TestAVAudioMixingHelper.setRate_, 0, objc._C_FLT)
        self.assertResultHasType(TestAVAudioMixingHelper.rate, objc._C_FLT)

        self.assertArgHasType(TestAVAudioMixingHelper.setReverbBlend_, 0, objc._C_FLT)
        self.assertResultHasType(TestAVAudioMixingHelper.reverbBlend, objc._C_FLT)

        self.assertArgHasType(TestAVAudioMixingHelper.setObstruction_, 0, objc._C_FLT)
        self.assertResultHasType(TestAVAudioMixingHelper.obstruction, objc._C_FLT)

        self.assertArgHasType(TestAVAudioMixingHelper.setOcclusion_, 0, objc._C_FLT)
        self.assertResultHasType(TestAVAudioMixingHelper.occlusion, objc._C_FLT)

        self.assertArgHasType(
            TestAVAudioMixingHelper.setPosition_,
            0,
            AVFoundation.AVAudio3DPoint.__typestr__,
        )
        self.assertResultHasType(
            TestAVAudioMixingHelper.position, AVFoundation.AVAudio3DPoint.__typestr__
        )

    def testConstants(self):
        self.assertEqual(
            AVFoundation.AVAudio3DMixingRenderingAlgorithmEqualPowerPanning, 0
        )
        self.assertEqual(AVFoundation.AVAudio3DMixingRenderingAlgorithmSphericalHead, 1)
        self.assertEqual(AVFoundation.AVAudio3DMixingRenderingAlgorithmHRTF, 2)
        self.assertEqual(AVFoundation.AVAudio3DMixingRenderingAlgorithmSoundField, 3)
        self.assertEqual(
            AVFoundation.AVAudio3DMixingRenderingAlgorithmStereoPassThrough, 5
        )
        self.assertEqual(AVFoundation.AVAudio3DMixingRenderingAlgorithmHRTFHQ, 6)
        self.assertEqual(AVFoundation.AVAudio3DMixingRenderingAlgorithmAuto, 7)

        self.assertEqual(AVFoundation.AVAudio3DMixingSourceModeSpatializeIfMono, 0)
        self.assertEqual(AVFoundation.AVAudio3DMixingSourceModeBypass, 1)
        self.assertEqual(AVFoundation.AVAudio3DMixingSourceModePointSource, 2)
        self.assertEqual(AVFoundation.AVAudio3DMixingSourceModeAmbienceBed, 3)

        self.assertEqual(AVFoundation.AVAudio3DMixingPointSourceInHeadModeMono, 0)
        self.assertEqual(AVFoundation.AVAudio3DMixingPointSourceInHeadModeBypass, 1)

    @min_sdk_level("10.10")
    def testProtocols(self):
        objc.protocolNamed("AVAudioMixing")
        objc.protocolNamed("AVAudioStereoMixing")
        objc.protocolNamed("AVAudio3DMixing")
