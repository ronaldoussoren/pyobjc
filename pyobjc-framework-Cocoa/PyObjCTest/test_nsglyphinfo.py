import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSGlyphInfo(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSIdentityMappingCharacterCollection, 0)
        self.assertEqual(AppKit.NSAdobeCNS1CharacterCollection, 1)
        self.assertEqual(AppKit.NSAdobeGB1CharacterCollection, 2)
        self.assertEqual(AppKit.NSAdobeJapan1CharacterCollection, 3)
        self.assertEqual(AppKit.NSAdobeJapan2CharacterCollection, 4)
        self.assertEqual(AppKit.NSAdobeKorea1CharacterCollection, 5)
