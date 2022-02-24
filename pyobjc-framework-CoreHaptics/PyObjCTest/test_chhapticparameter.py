import CoreHaptics
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestCHHapticParameter(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(CoreHaptics.CHHapticEventParameterID, str)
        self.assertIsTypedEnum(CoreHaptics.CHHapticDynamicParameterID, str)

    @min_sdk_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDHapticIntensity, str)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDHapticSharpness, str)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDAttackTime, str)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDDecayTime, str)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDReleaseTime, str)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDSustained, str)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDAudioVolume, str)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDAudioPitch, str)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDAudioPan, str)
        self.assertIsInstance(CoreHaptics.CHHapticEventParameterIDAudioBrightness, str)

        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDHapticIntensityControl, str
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDHapticSharpnessControl, str
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDHapticAttackTimeControl, str
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDHapticDecayTimeControl, str
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDHapticReleaseTimeControl, str
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioVolumeControl, str
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioPanControl, str
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioBrightnessControl, str
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioPitchControl, str
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioAttackTimeControl, str
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioDecayTimeControl, str
        )
        self.assertIsInstance(
            CoreHaptics.CHHapticDynamicParameterIDAudioReleaseTimeControl, str
        )
