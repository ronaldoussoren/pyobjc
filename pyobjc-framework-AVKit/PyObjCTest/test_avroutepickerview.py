import sys
import objc
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import AVKit

    class TestAVRoutePickerView (TestCase):
        def testConstants(self):
            self.assertEqual(AVKit.AVRoutePickerViewButtonStateNormal, 0)
            self.assertEqual(AVKit.AVRoutePickerViewButtonStateNormalHighlighted, 1)
            self.assertEqual(AVKit.AVRoutePickerViewButtonStateActive, 2)
            self.assertEqual(AVKit.AVRoutePickerViewButtonStateActiveHighlighted, 3)

        @min_os_level('10.13')
        def testMethods10_13(self):
            self.assertResultIsBOOL(AVKit.AVRoutePickerView.isRoutePickerButtonBordered)
            self.assertArgIsBOOL(AVKit.AVRoutePickerView.setRoutePickerButtonBordered_, 0)

        @min_sdk_level('10.13')
        def testProtocols(self):
            objc.protocolNamed('AVRoutePickerViewDelegate')

if __name__ == "__main__":
    main()
