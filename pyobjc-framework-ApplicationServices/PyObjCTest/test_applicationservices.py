import ApplicationServices
import HIServices
import PrintCore
from PyObjCTools.TestSupport import TestCase


class TestApplicationServices(TestCase):
    def testTrivial(self):
        ApplicationServices.kAXErrorSuccess


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            ApplicationServices,
            exclude_attrs={
                "GetIconFamilyData",
                "SetIconFamilyData",
                "ABCDGroup_ABCDGroup_",
                "ABCDContact_ABCDContact_",
            },
        )
        self.assertCallableMetadataIsSane(
            HIServices,
            exclude_attrs={
                "GetIconFamilyData",
                "SetIconFamilyData",
                "ABCDGroup_ABCDGroup_",
                "ABCDContact_ABCDContact_",
            },
        )
        self.assertCallableMetadataIsSane(
            PrintCore,
            exclude_attrs={
                "ABCDGroup_ABCDGroup_",
                "ABCDContact_ABCDContact_",
            },
        )
