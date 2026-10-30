import Foundation
from PyObjCTools.TestSupport import TestCase


class TestArchiver(TestCase):
    def test_constants(self):
        self.assertIsInstance(Foundation.NSInconsistentArchiveException, str)

    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSArchiver.archiveRootObject_toFile_)
        self.assertResultIsBOOL(Foundation.NSUnarchiver.isAtEnd)
