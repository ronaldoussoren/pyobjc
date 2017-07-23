from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSItemProviderReadingWritingHelper (NSObject):
    def loadDataWithTypeIdentifier_forItemProviderCompletionHandler_(self, ti, ch): pass
    def initWithItemProviderData_typeIdentifier_error_(self, d, ti, e): pass

    @classmethod
    def objectWithItemProviderData_typeIdentifier_error_(self, d, ti, e): pass

class TestNSItemProviderReadingWriting (TestCase):
    def testMethods(self):
        self.assertArgIsBlock(TestNSItemProviderReadingWritingHelper.loadDataWithTypeIdentifier_forItemProviderCompletionHandler_, 1, b'v@@')
        self.assertArgIsOut(TestNSItemProviderReadingWritingHelper.initWithItemProviderData_typeIdentifier_error_, 2)

        self.assertArgIsOut(TestNSItemProviderReadingWritingHelper.objectWithItemProviderData_typeIdentifier_error_, 2)
if __name__ == "__main__":
    main()
