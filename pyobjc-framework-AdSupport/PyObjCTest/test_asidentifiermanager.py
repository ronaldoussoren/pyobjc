from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import AdSupport

    class ASIdentifierManager (TestCase):
        @min_os_level('10.14')
        def test_classes(self):
            AdSupport.ASIdentifierManager

        @min_os_level('10.14')
        def test_methods(self):
            self.assertResultIsBOOL(AdSupport.ASIdentifierManager.isAdvertisingTrackingEnabled)


if __name__ == "__main__":
    main()
