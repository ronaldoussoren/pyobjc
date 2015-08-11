from PyObjCTools.TestSupport import *
from Foundation import *

try:
    unicode
except NameError:
    unicode = str

class TestNSExtensionItem (TestCase):
    @min_os_level('10.6')
    def testConstant10_10(self):
        self.assertIsInstance(NSExtensionItemAttributedTitleKey, unicode)
        self.assertIsInstance(NSExtensionItemAttributedContentTextKey, unicode)
        self.assertIsInstance(NSExtensionItemAttachmentsKey, unicode)


if __name__ == "__main__":
    main()
