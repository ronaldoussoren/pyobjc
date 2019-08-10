from PyObjCTools.TestSupport import *

import CoreHaptics


class TestCHHapticParameter(TestCase):
    @min_sdk_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            CoreHaptics.CHHapticEventParameterIDHapticIntensity, unicode
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticEventParameterIDHapticSharpness, unicode
        )
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDAttackTime, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDDecayTime, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDReleaseTime, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDSustained, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDAudioVolume, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDAudioPitch, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDAudioPan, unicode)
        self.assertIsInstance(
            CoreHaptics.CHHapticEventParameterIDAudioBrightness, unicode
        )

        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDHapticIntensityControl, unicode
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDHapticSharpnessControl, unicode
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDHapticAttackTimeControl, unicode
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDHapticDecayTimeControl, unicode
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDHapticReleaseTimeControl, unicode
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioVolumeControl, unicode
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioPanControl, unicode
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioBrightnessControl, unicode
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioPitchControl, unicode
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioAttackTimeControl, unicode
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioDecayTimeControl, unicode
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioReleaseTimeControl, unicode
        )
