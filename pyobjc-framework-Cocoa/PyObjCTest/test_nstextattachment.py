
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextAttachment (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSAttachmentCharacter, unichr(0xfffc))

if __name__ == "__main__":
    main()
