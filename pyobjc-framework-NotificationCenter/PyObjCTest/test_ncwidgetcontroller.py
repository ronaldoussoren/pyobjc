from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import NotificationCenter

    class TestNCWidgetController (TestCase):
        @min_os_level('10.10')
        def testClasses10_10(self):
            self.assertIsInstance(NotificationCenter.NCWidgetController, objc.objc_class)

            self.assertArgIsBOOL(NotificationCenter.NCWidgetController.setHasContent_forWidgetWithBundleIdentifier_, 0)


if __name__ == "__main__":
    main()
