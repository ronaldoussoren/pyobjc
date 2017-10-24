from PyObjCTools.TestSupport import *
import objc

try:
    from Quartz.QuickLookUI import *

except ImportError:
    pass

from Foundation import NSObject

QLPreviewItemLoadingBlock=b'v@'

class TestQLPreviewingControllerHelper (NSObject):
    def preparePreviewOfSearchableItemWithIdentifier_queryString_completionHandler_(self, i, q, c): pass

class TestQLPreviewingController (TestCase):
    @min_sdk_level('10.13')
    def testProtocols(self):
        objc.protocolNamed('QLPreviewingController')

    def testMethods(self):
        self.assertArgIsBlock(TestQLPreviewingControllerHelper.preparePreviewOfSearchableItemWithIdentifier_queryString_completionHandler_, 2, QLPreviewItemLoadingBlock)



if __name__ == "__main__":
    main()
