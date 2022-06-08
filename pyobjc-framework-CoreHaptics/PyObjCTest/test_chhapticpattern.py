import CoreHaptics
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestCHHapticParameter(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(CoreHaptics.CHHapticPatternKey, str)

    @min_sdk_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyVersion, str)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyPattern, str)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyEvent, str)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyEventType, str)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyTime, str)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyEventDuration, str)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyEventWaveformPath, str)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyEventParameters, str)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyParameter, str)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyParameterID, str)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyParameterValue, str)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyParameterCurve, str)
        self.assertIsInstance(
            CoreHaptics.CHHapticPatternKeyParameterCurveControlPoints, str
        )

    @min_sdk_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            CoreHaptics.CHHapticPatternKeyEventWaveformUseVolumeEnvelope, str
        )

    @min_sdk_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(
            CoreHaptics.CHHapticPatternKeyEventWaveformLoopEnabled, str
        )

    @min_sdk_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsOut(
            CoreHaptics.CHHapticPattern.initWithEvents_parameters_error_, 2
        )
        self.assertArgIsOut(
            CoreHaptics.CHHapticPattern.initWithEvents_parameterCurves_error_, 2
        )
        self.assertArgIsOut(CoreHaptics.CHHapticPattern.initWithDictionary_error_, 1)
        self.assertArgIsOut(
            CoreHaptics.CHHapticPattern.exportDictionaryAndReturnError_, 0
        )

    @min_sdk_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsOut(CoreHaptics.CHHapticPattern.initWithContentsOfURL_error_, 1)
