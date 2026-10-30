import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestValueTrans(TestCase):
    def test_constants(self):
        self.assertIsInstance(Foundation.NSNegateBooleanTransformerName, str)
        self.assertIsInstance(Foundation.NSIsNilTransformerName, str)
        self.assertIsInstance(Foundation.NSIsNotNilTransformerName, str)
        self.assertIsInstance(Foundation.NSUnarchiveFromDataTransformerName, str)
        self.assertIsInstance(Foundation.NSKeyedUnarchiveFromDataTransformerName, str)

    @min_os_level("10.14")
    def test_constants10_14(self):
        self.assertIsInstance(Foundation.NSSecureUnarchiveFromDataTransformerName, str)

    def test_methods(self):
        self.assertResultIsBOOL(
            Foundation.NSValueTransformer.allowsReverseTransformation
        )
