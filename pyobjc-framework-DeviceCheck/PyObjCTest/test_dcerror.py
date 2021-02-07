from PyObjCTools.TestSupport import TestCase

import DeviceCheck


class TestDCError(TestCase):
    def test_constants(self):
        self.assertIsInstance(DeviceCheck.DCErrorDomain, str)

        self.assertEqual(DeviceCheck.DCErrorUnknownSystemFailure, 0)
        self.assertEqual(DeviceCheck.DCErrorFeatureUnsupported, 1)
        self.assertEqual(DeviceCheck.DCErrorInvalidInput, 2)
        self.assertEqual(DeviceCheck.DCErrorInvalidKey, 3)
        self.assertEqual(DeviceCheck.DCErrorServerUnavailable, 4)
