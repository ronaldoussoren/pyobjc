import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSOrderedCollectionChange(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSCollectionChangeType)
        self.assertEqual(Foundation.NSCollectionChangeInsert, 0)
        self.assertEqual(Foundation.NSCollectionChangeRemove, 1)
