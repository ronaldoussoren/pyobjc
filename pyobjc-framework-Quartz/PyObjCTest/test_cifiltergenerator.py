from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCIFilterGenerator(TestCase):
    def testConstants(self):
        self.assertIsInstance(Quartz.kCIFilterGeneratorExportedKey, str)
        self.assertIsInstance(Quartz.kCIFilterGeneratorExportedKeyTargetObject, str)
        self.assertIsInstance(Quartz.kCIFilterGeneratorExportedKeyName, str)

    def testMethods(self):
        self.assertResultIsBOOL(Quartz.CIFilterGenerator.writeToURL_atomically_)
        self.assertArgIsBOOL(Quartz.CIFilterGenerator.writeToURL_atomically_, 1)
