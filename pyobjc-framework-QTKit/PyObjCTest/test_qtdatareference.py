
from PyObjCTools.TestSupport import *
from QTKit import *

try:
    unicode
except NameError:
    unicode = str

class TestQTDataReference (TestCase):
    def testConstants(self):
        self.assertIsInstance(QTDataReferenceTypeFile, unicode)
        self.assertIsInstance(QTDataReferenceTypeHandle, unicode)
        self.assertIsInstance(QTDataReferenceTypePointer, unicode)
        self.assertIsInstance(QTDataReferenceTypeResource, unicode)
        self.assertIsInstance(QTDataReferenceTypeURL, unicode)

if __name__ == "__main__":
    main()
