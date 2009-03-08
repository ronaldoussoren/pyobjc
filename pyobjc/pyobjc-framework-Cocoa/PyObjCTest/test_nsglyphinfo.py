
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSGlyphInfo (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSIdentityMappingCharacterCollection, 0)
        self.failUnlessEqual(NSAdobeCNS1CharacterCollection, 1)
        self.failUnlessEqual(NSAdobeGB1CharacterCollection, 2)
        self.failUnlessEqual(NSAdobeJapan1CharacterCollection, 3)
        self.failUnlessEqual(NSAdobeJapan2CharacterCollection, 4)
        self.failUnlessEqual(NSAdobeKorea1CharacterCollection, 5)

if __name__ == "__main__":
    main()
