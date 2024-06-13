from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSContainer(TestCase):
    def test_constants(self):
        self.assertIsEnumType(FSKit.SContainerState)
        self.assertEqual(FSKit.FSContainerNotReady, 0)
        self.assertEqual(FSKit.FSContainerBlocked, 1)
        self.assertEqual(FSKit.FSContainerReady, 2)
        self.assertEqual(FSKit.FSContainerActive, 3)
