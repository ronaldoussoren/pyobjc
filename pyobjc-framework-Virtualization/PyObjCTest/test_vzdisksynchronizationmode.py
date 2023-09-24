from PyObjCTools.TestSupport import TestCase

import Virtualization


class TestVZDiskSynchronizationMode(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Virtualization.VZDiskSynchronizationMode)

        self.assertEqual(Virtualization.VZDiskSynchronizationModeFull, 0)
        self.assertEqual(Virtualization.VZDiskSynchronizationModeNone, 1)
