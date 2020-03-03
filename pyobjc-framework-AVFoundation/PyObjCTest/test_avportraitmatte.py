import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVPortraitMatte(TestCase):
    @min_os_level("10.14")
    def testMethods(self):
        self.assertArgIsOut(
            AVFoundation.AVPortraitEffectsMatte.portraitEffectsMatteFromDictionaryRepresentation_error_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            AVFoundation.AVPortraitEffectsMatte.portraitEffectsMatteByReplacingPortraitEffectsMatteWithPixelBuffer_error_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            AVFoundation.AVPortraitEffectsMatte.dictionaryRepresentationForAuxiliaryDataType_,  # noqa: B950
            0,
        )
