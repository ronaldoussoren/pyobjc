from PyObjCTools.TestSupport import *

import CoreServices

class TestMDLabel (TestCase):
    @expectedFailure
    @min_os_level('10.7')
    def test_types(self):
        self.assertIsCFType(CoreServices.MDLabelRef)

    @min_os_level('10.7')
    def test_functions(self):
        self.assertIsInstance(CoreServices.MDLabelGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CoreServices.MDItemCopyLabels)
        self.assertResultIsBOOL(CoreServices.MDItemSetLabel)
        self.assertResultIsBOOL(CoreServices.MDItemRemoveLabel)
        self.assertResultIsCFRetained(CoreServices.MDLabelCreate)
        self.assertResultIsCFRetained(CoreServices.MDLabelCopyAttribute)
        self.assertResultIsCFRetained(CoreServices.MDLabelCopyAttributeName)
        self.assertResultIsBOOL(CoreServices.MDLabelDelete)
        self.assertResultIsBOOL(CoreServices.MDLabelSetAttributes)
        self.assertResultIsCFRetained(CoreServices.MDCopyLabelKinds)
        self.assertResultIsCFRetained(CoreServices.MDCopyLabelsMatchingExpression)
        self.assertResultIsCFRetained(CoreServices.MDCopyLabelsWithKind)
        self.assertResultIsCFRetained(CoreServices.MDCopyLabelWithUUID)

    def test_constants(self):
        self.assertEqual(CoreServices.kMDLabelUserDomain, 0)
        self.assertEqual(CoreServices.kMDLabelLocalDomain, 1)


    @min_os_level('10.7')
    def test_constants10_7(self):
        self.assertIsInstance(CoreServices.kMDLabelBundleURL, unicode)
        self.assertIsInstance(CoreServices.kMDLabelContentChangeDate, unicode)
        self.assertIsInstance(CoreServices.kMDLabelDisplayName, unicode)
        self.assertIsInstance(CoreServices.kMDLabelIconData, unicode)
        self.assertIsInstance(CoreServices.kMDLabelIconUUID, unicode)
        self.assertIsInstance(CoreServices.kMDLabelIsMutuallyExclusiveSetMember, unicode)
        self.assertIsInstance(CoreServices.kMDLabelKind, unicode)
        self.assertIsInstance(CoreServices.kMDLabelSetsFinderColor, unicode)
        self.assertIsInstance(CoreServices.kMDLabelUUID, unicode)
        self.assertIsInstance(CoreServices.kMDLabelVisibility, unicode)
        self.assertIsInstance(CoreServices.kMDLabelKindIsMutuallyExclusiveSetKey, unicode)
        self.assertIsInstance(CoreServices.kMDLabelKindVisibilityKey, unicode)
        self.assertIsInstance(CoreServices.kMDPrivateVisibility, unicode)
        self.assertIsInstance(CoreServices.kMDPublicVisibility, unicode)
        self.assertIsInstance(CoreServices.kMDLabelAddedNotification, unicode)
        self.assertIsInstance(CoreServices.kMDLabelChangedNotification, unicode)
        self.assertIsInstance(CoreServices.kMDLabelRemovedNotification, unicode)


if __name__ == "__main__":
    main()
