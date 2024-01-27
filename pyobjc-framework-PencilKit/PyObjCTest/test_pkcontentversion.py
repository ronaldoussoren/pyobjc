from PyObjCTools.TestSupport import TestCase

import PencilKit


class TestPKContentVersion(TestCase):
    def test_constants(self):
        self.assertIsEnumType(PencilKit.PKContentVersion)
        self.assertEqual(PencilKit.PKContentVersion1, 1)
        self.assertEqual(PencilKit.PKContentVersion2, 2)
        self.assertEqual(PencilKit.PKContentVersion3, 3)
        self.assertNotHasAttr(PencilKit, "PKContentVersionLatest")
