from PyObjCTools.TestSupport import TestCase
import QTKit


class TestQTCompressionOptions(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(QTKit.QTCompressionOptions.isEqualToCompressionOptions_)
