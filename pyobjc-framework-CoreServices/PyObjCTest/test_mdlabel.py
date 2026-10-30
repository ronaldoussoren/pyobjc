import CoreServices
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestMDLabel(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreServices.MDLabelDomain)
        self.assertEqual(CoreServices.kMDLabelUserDomain, 0)
        self.assertEqual(CoreServices.kMDLabelLocalDomain, 1)

    def test_constants(self):
        self.assertIsInstance(CoreServices.kMDLabelBundleURL, str)
        self.assertIsInstance(CoreServices.kMDLabelContentChangeDate, str)
        self.assertIsInstance(CoreServices.kMDLabelDisplayName, str)
        self.assertIsInstance(CoreServices.kMDLabelIconData, str)
        self.assertIsInstance(CoreServices.kMDLabelIconUUID, str)
        self.assertIsInstance(CoreServices.kMDLabelIsMutuallyExclusiveSetMember, str)
        self.assertIsInstance(CoreServices.kMDLabelKind, str)
        self.assertIsInstance(CoreServices.kMDLabelSetsFinderColor, str)
        self.assertIsInstance(CoreServices.kMDLabelUUID, str)
        self.assertIsInstance(CoreServices.kMDLabelVisibility, str)
        self.assertIsInstance(CoreServices.kMDLabelKindIsMutuallyExclusiveSetKey, str)
        self.assertIsInstance(CoreServices.kMDLabelKindVisibilityKey, str)
        self.assertIsInstance(CoreServices.kMDPrivateVisibility, str)
        self.assertIsInstance(CoreServices.kMDPublicVisibility, str)
        self.assertIsInstance(CoreServices.kMDLabelAddedNotification, str)
        self.assertIsInstance(CoreServices.kMDLabelChangedNotification, str)
        self.assertIsInstance(CoreServices.kMDLabelRemovedNotification, str)

    @expectedFailure
    def test_types(self):
        self.assertIsCFType(CoreServices.MDLabelRef)

    def test_functions(self):
        self.assertIsInstance(CoreServices.MDLabelGetTypeID(), int)

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
