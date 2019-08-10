from PyObjCTools.TestSupport import *

import CoreHaptics


class TestCHHapticParameter(TestCase):
    @min_sdk_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyVersion, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyPattern, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyEvent, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyEventType, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyTime, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyEventDuration, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyEventWaveformPath, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyEventParameters, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyParameter, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyParameterID, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyParameterValue, unicode)
        self.assertIsInstance(CoreHaptics.CHHapticPatternKeyParameterCurve, unicode)
        self.assertIsInstance(
            CoreHaptics.CHHapticPatternKeyParameterCurveControlPoints, unicode
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
