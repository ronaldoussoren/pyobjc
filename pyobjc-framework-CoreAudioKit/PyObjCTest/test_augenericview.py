import CoreAudioKit
from PyObjCTools.TestSupport import TestCase


class TestAUGenericView(TestCase):
    def testConstants(self):
        self.assertEqual(CoreAudioKit.AUViewTitleDisplayFlag, 1 << 0)
        self.assertEqual(CoreAudioKit.AUViewPropertiesDisplayFlag, 1 << 1)
        self.assertEqual(CoreAudioKit.AUViewParametersDisplayFlag, 1 << 2)

    def testMethods(self):
        self.assertResultIsBOOL(CoreAudioKit.AUGenericView.showsExpertParameters)
        self.assertArgIsBOOL(CoreAudioKit.AUGenericView.setShowsExpertParameters_, 0)
