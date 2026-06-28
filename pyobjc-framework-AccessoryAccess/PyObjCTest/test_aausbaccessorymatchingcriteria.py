from PyObjCTools.TestSupport import TestCase

import AccessoryAccess


class TestAAUSBAccessoryMatchingCriteria(TestCase):
    def test_enums(self):
        self.assertIsEnumType(
            AccessoryAccess.AAUSBAccessoryMatchingCriteriaInterfaceMatchingOption
        )
        self.assertEqual(
            AccessoryAccess.AAUSBAccessoryMatchingCriteriaInterfaceMatchingOptionMatchAll,
            0,
        )
        self.assertEqual(
            AccessoryAccess.AAUSBAccessoryMatchingCriteriaInterfaceMatchingOptionMatchAny,
            1,
        )
