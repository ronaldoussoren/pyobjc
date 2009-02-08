
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTDataReference (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(QTDataReferenceTypeFile, unicode)
        self.failUnlessIsInstance(QTDataReferenceTypeHandle, unicode)
        self.failUnlessIsInstance(QTDataReferenceTypePointer, unicode)
        self.failUnlessIsInstance(QTDataReferenceTypeResource, unicode)
        self.failUnlessIsInstance(QTDataReferenceTypeURL, unicode)

if __name__ == "__main__":
    main()
