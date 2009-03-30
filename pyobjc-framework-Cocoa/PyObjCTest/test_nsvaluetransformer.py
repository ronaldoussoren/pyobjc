from Foundation import *
from PyObjCTools.TestSupport import *

class TestValueTrans (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSNegateBooleanTransformerName, unicode))
        self.failUnless(isinstance(NSIsNilTransformerName, unicode))
        self.failUnless(isinstance(NSIsNotNilTransformerName, unicode))
        self.failUnless(isinstance(NSUnarchiveFromDataTransformerName, unicode))
        self.failUnless(isinstance(NSKeyedUnarchiveFromDataTransformerName, unicode))

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSValueTransformer.allowsReverseTransformation)

if __name__ == "__main__":
    main()
