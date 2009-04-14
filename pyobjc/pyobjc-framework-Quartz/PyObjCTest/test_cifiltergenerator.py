
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIFilterGenerator (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kCIFilterGeneratorExportedKey, unicode)
        self.failUnlessIsInstance(kCIFilterGeneratorExportedKeyTargetObject, unicode)
        self.failUnlessIsInstance(kCIFilterGeneratorExportedKeyName, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(CIFilterGenerator.writeToURL_atomically_)
        self.failUnlessArgIsBOOL(CIFilterGenerator.writeToURL_atomically_, 1)


if __name__ == "__main__":
    main()
