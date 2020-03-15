import Foundation
from PyObjCTools.TestSupport import TestCase


class TestArchiver(TestCase):
    def testConstants(self):
        self.assertIsInstance(Foundation.NSInconsistentArchiveException, str)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSArchiver.archiveRootObject_toFile_)
        self.assertResultIsBOOL(Foundation.NSUnarchiver.isAtEnd)
