
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSGlyphInfo (TestCase):
    def testConstants(self):
        self.assertEqual(NSIdentityMappingCharacterCollection, 0)
        self.assertEqual(NSAdobeCNS1CharacterCollection, 1)
        self.assertEqual(NSAdobeGB1CharacterCollection, 2)
        self.assertEqual(NSAdobeJapan1CharacterCollection, 3)
        self.assertEqual(NSAdobeJapan2CharacterCollection, 4)
        self.assertEqual(NSAdobeKorea1CharacterCollection, 5)

if __name__ == "__main__":
    main()
