import CoreAudio
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCATapDescription(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CoreAudio.CATapMuteBehavior)
        self.assertEqual(CoreAudio.CATapUnmuted, 0)
        self.assertEqual(CoreAudio.CATapMuted, 1)
        self.assertEqual(CoreAudio.CATapMutedWhenTapped, 2)

    @min_os_level("12.0")
    def test_methods(self):
        self.assertResultIsBOOL(CoreAudio.CATapDescription.isMono)
        self.assertArgIsBOOL(CoreAudio.CATapDescription.setMono_, 0)
        self.assertResultIsBOOL(CoreAudio.CATapDescription.isExclusive)
        self.assertArgIsBOOL(CoreAudio.CATapDescription.setExclusive_, 0)
        self.assertResultIsBOOL(CoreAudio.CATapDescription.isMixdown)
        self.assertArgIsBOOL(CoreAudio.CATapDescription.setMixdown_, 0)
        self.assertResultIsBOOL(CoreAudio.CATapDescription.isPrivate)
        self.assertArgIsBOOL(CoreAudio.CATapDescription.setPrivate_, 0)
