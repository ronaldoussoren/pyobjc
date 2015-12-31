from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSExtensionContext (TestCase):
    @min_os_level('10.10')
    @onlyOn64Bit
    def testMethods10_10(self):
        self.assertArgIsBlock(NSExtensionContext.completeRequestReturningItems_completionHandler_, 1, b'vZ')
        self.assertArgIsBlock(NSExtensionContext.openURL_completionHandler_, 1, b'vZ')

    @min_os_level('10.10')
    @onlyOn64Bit
    def testConstant10_10(self):
        self.assertIsInstance(NSExtensionItemsAndErrorsKey, unicode)


if __name__ == "__main__":
    main()
