import CoreAudioKit
from PyObjCTools.TestSupport import TestCase


class TestAUGenericView(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreAudioKit.AUGenericViewDisplayFlags)
        self.assertEqual(CoreAudioKit.AUViewTitleDisplayFlag, 1 << 0)
        self.assertEqual(CoreAudioKit.AUViewPropertiesDisplayFlag, 1 << 1)
        self.assertEqual(CoreAudioKit.AUViewParametersDisplayFlag, 1 << 2)

    def test_methods(self):
        self.assertResultIsBOOL(CoreAudioKit.AUGenericView.showsExpertParameters)
        self.assertArgIsBOOL(CoreAudioKit.AUGenericView.setShowsExpertParameters_, 0)
