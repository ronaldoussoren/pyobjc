from PyObjCTools.TestSupport import TestCase
import AVKit


class TestAVLegibleMediaOptionsMenuControllerHelper(AVKit.NSObject):
    def legibleMenuController_didChangeMenuState_(self, a, b):
        pass


class TestAVLegibleMediaOptionsMenuController(TestCase):
    def test_enum(self):
        self.assertIsEnumType(AVKit.AVLegibleMediaOptionsMenuType)
        self.assertEqual(AVKit.AVLegibleMediaOptionsMenuTypeDefault, 0)
        self.assertEqual(AVKit.AVLegibleMediaOptionsMenuTypeCaptionAppearance, 1)

        self.assertIsEnumType(AVKit.AVLegibleMediaOptionsMenuStateChangeReason)
        self.assertEqual(AVKit.AVLegibleMediaOptionsMenuStateChangeReasonNone, 0)
        self.assertEqual(
            AVKit.AVLegibleMediaOptionsMenuStateChangeReasonLanguageMismatch, 1
        )

        self.assertIsEnumType(AVKit.AVLegibleMediaOptionsMenuContents)
        self.assertEqual(AVKit.AVLegibleMediaOptionsMenuContentsLegible, 1 << 0)
        self.assertEqual(
            AVKit.AVLegibleMediaOptionsMenuContentsCaptionAppearance, 1 << 1
        )
        self.assertEqual(
            AVKit.AVLegibleMediaOptionsMenuContentsAll,
            AVKit.AVLegibleMediaOptionsMenuContentsLegible
            | AVKit.AVLegibleMediaOptionsMenuContentsCaptionAppearance,
        )

    def test_structs(self):
        v = AVKit.AVLegibleMediaOptionsMenuState()
        self.assertIs(v.enabled, False)
        self.assertEqual(v.reason, 0)

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestAVLegibleMediaOptionsMenuControllerHelper.legibleMenuController_didChangeMenuState_,
            1,
            AVKit.AVLegibleMediaOptionsMenuState.__typestr__,
        )
