import Foundation
import CoreFoundation
from PyObjCTools.TestSupport import TestCase


class TestNSPropertyList(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSPropertyListMutabilityOptions)
        self.assertEqual(
            Foundation.NSPropertyListImmutable, CoreFoundation.kCFPropertyListImmutable
        )
        self.assertEqual(
            Foundation.NSPropertyListMutableContainers,
            CoreFoundation.kCFPropertyListMutableContainers,
        )
        self.assertEqual(
            Foundation.NSPropertyListMutableContainersAndLeaves,
            CoreFoundation.kCFPropertyListMutableContainersAndLeaves,
        )

        self.assertIsEnumType(Foundation.NSPropertyListFormat)
        self.assertEqual(
            Foundation.NSPropertyListOpenStepFormat,
            CoreFoundation.kCFPropertyListOpenStepFormat,
        )
        self.assertEqual(
            Foundation.NSPropertyListXMLFormat_v1_0,
            CoreFoundation.kCFPropertyListXMLFormat_v1_0,
        )
        self.assertEqual(
            Foundation.NSPropertyListBinaryFormat_v1_0,
            CoreFoundation.kCFPropertyListBinaryFormat_v1_0,
        )

    def test_methods(self):
        self.assertResultIsBOOL(
            Foundation.NSPropertyListSerialization.propertyList_isValidForFormat_
        )
        self.assertArgIsOut(
            Foundation.NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            Foundation.NSPropertyListSerialization.propertyListFromData_mutabilityOption_format_errorDescription_,  # noqa: B950
            3,
        )

        self.assertArgIsOut(
            Foundation.NSPropertyListSerialization.dataWithPropertyList_format_options_error_,
            3,
        )
        self.assertArgIsOut(
            Foundation.NSPropertyListSerialization.writePropertyList_toStream_format_options_error_,  # noqa: B950
            4,
        )
        self.assertArgIsOut(
            Foundation.NSPropertyListSerialization.propertyListWithData_options_format_error_,
            3,
        )
        self.assertArgIsOut(
            Foundation.NSPropertyListSerialization.propertyListWithStream_options_format_error_,
            3,
        )
