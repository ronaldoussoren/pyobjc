from PyObjCTools.TestSupport import TestCase

import AccessoryAccess


class TestAAError(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AccessoryAccess.AAErrorCode)
        self.assertEqual(AccessoryAccess.AAErrorCodeInternal, 1)
        self.assertEqual(
            AccessoryAccess.AAErrorCodeAccessoryListenerAlreadyRegistered, 2
        )
        self.assertEqual(AccessoryAccess.AAErrorCodeAccessoryNotAccessible, 3)
        self.assertEqual(AccessoryAccess.AAErrorCodeInvalidAccessoryState, 4)
