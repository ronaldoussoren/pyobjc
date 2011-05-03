
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIFilterGenerator (TestCase):
    def testConstants(self):
        self.assertIsInstance(kCIFilterGeneratorExportedKey, unicode)
        self.assertIsInstance(kCIFilterGeneratorExportedKeyTargetObject, unicode)
        self.assertIsInstance(kCIFilterGeneratorExportedKeyName, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(CIFilterGenerator.writeToURL_atomically_)
        self.assertArgIsBOOL(CIFilterGenerator.writeToURL_atomically_, 1)


if __name__ == "__main__":
    main()
