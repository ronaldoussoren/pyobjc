import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSOrderedCollectionChange(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSCollectionChangeType)

    def test_constants(self):
        self.assertEqual(Foundation.NSCollectionChangeInsert, 0)
        self.assertEqual(Foundation.NSCollectionChangeRemove, 1)
