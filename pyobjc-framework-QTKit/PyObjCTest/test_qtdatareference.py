from PyObjCTools.TestSupport import TestCase
import QTKit


class TestQTDataReference(TestCase):
    def testConstants(self):
        self.assertIsInstance(QTKit.QTDataReferenceTypeFile, str)
        self.assertIsInstance(QTKit.QTDataReferenceTypeHandle, str)
        self.assertIsInstance(QTKit.QTDataReferenceTypePointer, str)
        self.assertIsInstance(QTKit.QTDataReferenceTypeResource, str)
        self.assertIsInstance(QTKit.QTDataReferenceTypeURL, str)
