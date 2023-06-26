import MediaAccessibility
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMAFlashingLightsProcessing(TestCase):
    @min_os_level("14.0")
    def testConstants14_0(self):
        self.assertIsTypedEnum(
            MediaAccessibility.MAFlashingLightsProcessorOptionKey, str
        )

    @min_os_level("14.0")
    def testMethods14_0(self):
        self.assertResultIsBOOL(
            MediaAccessibility.MAFlashingLightsProcessorResult.surfaceProcessed
        )

        self.assertResultIsBOOL(
            MediaAccessibility.MAFlashingLightsProcessor.canProcessSurface_
        )
