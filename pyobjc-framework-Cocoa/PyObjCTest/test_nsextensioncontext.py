from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSExtensionContext (TestCase):
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsBlock(NSExtensionContext.completeRequestReturningItems_completionHandler_, 1, 'vZ')
        self.assertArgIsBlock(NSExtensionContext.openURL_completionHandler_, 1, 'vZ')

    @min_os_level('10.6')
    def testConstant10_10(self):
        self.assertIsInstance(NSExtensionItemsAndErrorsKey, unicode)


if __name__ == "__main__":
    main()
