from PyObjCTools.TestSupport import *
from Foundation import *


class TestNSOrderedCollectionChange(TestCase):
    def test_constants(self):
        self.assertEqual(NSCollectionChangeInsert, 0)
        self.assertEqual(NSCollectionChangeRemove, 1)


if __name__ == "__main__":
    main()
