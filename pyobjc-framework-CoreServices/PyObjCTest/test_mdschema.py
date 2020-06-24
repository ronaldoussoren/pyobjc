import CoreServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMDSchema(TestCase):
    def test_functions(self):
        self.assertResultIsCFRetained(CoreServices.MDSchemaCopyAttributesForContentType)
        self.assertResultIsCFRetained(
            CoreServices.MDSchemaCopyMetaAttributesForAttribute
        )
        self.assertResultIsCFRetained(CoreServices.MDSchemaCopyAllAttributes)
        self.assertResultIsCFRetained(CoreServices.MDSchemaCopyDisplayNameForAttribute)
        self.assertResultIsCFRetained(
            CoreServices.MDSchemaCopyDisplayDescriptionForAttribute
        )

    def test_constants(self):
        self.assertIsInstance(CoreServices.kMDAttributeDisplayValues, str)
        self.assertIsInstance(CoreServices.kMDAttributeAllValues, str)
        self.assertIsInstance(CoreServices.kMDAttributeName, str)
        self.assertIsInstance(CoreServices.kMDAttributeType, str)
        self.assertIsInstance(CoreServices.kMDAttributeMultiValued, str)
        self.assertIsInstance(CoreServices.kMDAttributeDisplayValues, str)

    @min_os_level("10.5")
    def test_constants10_5(self):
        self.assertIsInstance(CoreServices.kMDAttributeReadOnlyValues, str)
        self.assertIsInstance(CoreServices.kMDExporterAvaliable, str)
