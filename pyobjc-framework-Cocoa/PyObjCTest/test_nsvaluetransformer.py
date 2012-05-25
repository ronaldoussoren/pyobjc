from Foundation import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str

class TestValueTrans (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSNegateBooleanTransformerName, unicode)
        self.assertIsInstance(NSIsNilTransformerName, unicode)
        self.assertIsInstance(NSIsNotNilTransformerName, unicode)
        self.assertIsInstance(NSUnarchiveFromDataTransformerName, unicode)
        self.assertIsInstance(NSKeyedUnarchiveFromDataTransformerName, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSValueTransformer.allowsReverseTransformation)

if __name__ == "__main__":
    main()
