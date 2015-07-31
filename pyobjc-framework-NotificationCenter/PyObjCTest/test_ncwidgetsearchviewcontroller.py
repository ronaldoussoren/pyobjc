from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import NotificationCenter

    def TestNCWidgetSearchViewDelegateHelper (NSObject):
        def setHasContent_forWidgetWithBundleIdentifier_(self, c, i): pass


    class TestNCWidgetSearchViewControlle (TestCase):
        @min_os_level('10.10')
        def testClasses10_10(self):
            objc.protocolNamed('NCWidgetSearchViewDelegate')

            self.assertArgIsBOOL(NotificationCenter.NCWidgetController.setHasContent_forWidgetWithBundleIdentifier_, 0)


if __name__ == "__main__":
    main()
