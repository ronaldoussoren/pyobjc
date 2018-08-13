from PyObjCTools.TestSupport import *

import CoreServices

class TestMDSchema (TestCase):
    def test_functions(self):
        self.assertResultIsCFRetained(CoreServices.MDSchemaCopyAttributesForContentType)
        self.assertResultIsCFRetained(CoreServices.MDSchemaCopyMetaAttributesForAttribute)
        self.assertResultIsCFRetained(CoreServices.MDSchemaCopyAllAttributes)
        self.assertResultIsCFRetained(CoreServices.MDSchemaCopyDisplayNameForAttribute)
        self.assertResultIsCFRetained(CoreServices.MDSchemaCopyDisplayDescriptionForAttribute)

    def test_constants(self):
        self.assertIsInstance(CoreServices.kMDAttributeDisplayValues, unicode)
        self.assertIsInstance(CoreServices.kMDAttributeAllValues, unicode)
        self.assertIsInstance(CoreServices.kMDAttributeName, unicode)
        self.assertIsInstance(CoreServices.kMDAttributeType, unicode)
        self.assertIsInstance(CoreServices.kMDAttributeMultiValued, unicode)
        self.assertIsInstance(CoreServices.kMDAttributeDisplayValues, unicode)

    @min_os_level('10.5')
    def test_constants10_5(self):
        self.assertIsInstance(CoreServices.kMDAttributeReadOnlyValues, unicode)
        self.assertIsInstance(CoreServices.kMDExporterAvaliable, unicode)

if __name__ == "__main__":
    main()
