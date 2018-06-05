from Foundation import *
from PyObjCTools.TestSupport import *

class TestValueTrans (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSNegateBooleanTransformerName, unicode)
        self.assertIsInstance(NSIsNilTransformerName, unicode)
        self.assertIsInstance(NSIsNotNilTransformerName, unicode)
        self.assertIsInstance(NSUnarchiveFromDataTransformerName, unicode)
        self.assertIsInstance(NSKeyedUnarchiveFromDataTransformerName, unicode)

    @min_os_level('10.14')
    def testConstants(self):
        self.assertIsInstance(NSSecureUnarchiveFromDataTransformerName, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSValueTransformer.allowsReverseTransformation)

if __name__ == "__main__":
    main()
