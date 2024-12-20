from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSContainer(TestCase):
    def test_constants(self):
        self.assertIsEnumType(FSKit.FSContainerState)
        self.assertEqual(FSKit.FSContainerStateNotReady, 0)
        self.assertEqual(FSKit.FSContainerStateBlocked, 1)
        self.assertEqual(FSKit.FSContainerStateReady, 2)
        self.assertEqual(FSKit.FSContainerStateActive, 3)
