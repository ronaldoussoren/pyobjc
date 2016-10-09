import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import SafariServices

    class TestSFSafariExtensionHandlingHelper (SafariServices.NSObject):
        def validateToolbarItemInWindow_validationHandler_(self, w, h): pass

    class TestSFSafariExtensionHandling (TestCase):
        @min_os_level('10.12')
        def testProtocols(self):
            objc.protocolNamed('SFSafariExtensionHandling')

        @min_os_level('10.12')
        def testMethods(self):
            self.assertArgIsBlock(TestSFSafariExtensionHandlingHelper.validateToolbarItemInWindow_validationHandler_, b'vZ@')




if __name__ == "__main__":
    main()

