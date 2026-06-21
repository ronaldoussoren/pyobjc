from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCIFilterGenerator(TestCase):
    def test_constants(self):
        self.assertIsInstance(Quartz.kCIFilterGeneratorExportedKey, str)
        self.assertIsInstance(Quartz.kCIFilterGeneratorExportedKeyTargetObject, str)
        self.assertIsInstance(Quartz.kCIFilterGeneratorExportedKeyName, str)

    def test_methods(self):
        self.assertResultIsBOOL(Quartz.CIFilterGenerator.writeToURL_atomically_)
        self.assertArgIsBOOL(Quartz.CIFilterGenerator.writeToURL_atomically_, 1)
