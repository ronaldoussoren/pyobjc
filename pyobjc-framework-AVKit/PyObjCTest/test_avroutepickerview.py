import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import AVKit

    class TestAVRoutePickerView(TestCase):
        def test_constants(self):
            self.assertEqual(AVKit.AVRoutePickerViewButtonStateNormal, 0)
            self.assertEqual(AVKit.AVRoutePickerViewButtonStateNormalHighlighted, 1)
            self.assertEqual(AVKit.AVRoutePickerViewButtonStateActive, 2)
            self.assertEqual(AVKit.AVRoutePickerViewButtonStateActiveHighlighted, 3)

        @min_os_level("10.15")
        def test_methods(self):
            self.assertResultIsBOOL(AVKit.AVRoutePickerView.isRoutePickerButtonBordered)
            self.assertArgIsBOOL(
                AVKit.AVRoutePickerView.setRoutePickerButtonBordered_, 0
            )

        @min_sdk_level("10.15")
        def test_protocols(self):
            objc.protocolNamed("AVRoutePickerViewDelegate")


if __name__ == "__main__":
    main()
