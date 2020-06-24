import MediaAccessibility
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMAImageCaptioning(TestCase):
    @min_os_level("10.15")
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(MediaAccessibility.MAImageCaptioningCopyCaption)
        self.assertArgIsOut(MediaAccessibility.MAImageCaptioningCopyCaption, 1)
        self.assertArgIsCFRetained(MediaAccessibility.MAImageCaptioningCopyCaption, 1)

        self.assertArgIsOut(MediaAccessibility.MAImageCaptioningSetCaption, 2)
        self.assertArgIsCFRetained(MediaAccessibility.MAImageCaptioningSetCaption, 2)

        self.assertResultIsCFRetained(
            MediaAccessibility.MAImageCaptioningCopyMetadataTagPath
        )
