import AppKit
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    min_sdk_level,
)


class TestNSKeyValueBindingHelper(AppKit.NSObject):
    def commitEditingWithDelegate_didCommitSelector_contextInfo_(self, d, s, i):
        return None

    def commitEditingAndReturnError_(self, v):
        return 1

    def commitEditing(self):
        return 1


class TestNSKeyValueBinding(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSBindingInfoKey, str)
        self.assertIsTypedEnum(AppKit.NSBindingName, str)
        self.assertIsTypedEnum(AppKit.NSBindingOption, str)

    def testConstants(self):
        self.assertIsInstance(AppKit.NSMultipleValuesMarker, AppKit.NSObject)
        self.assertIsInstance(AppKit.NSNoSelectionMarker, AppKit.NSObject)
        self.assertIsInstance(AppKit.NSNotApplicableMarker, AppKit.NSObject)

        self.assertIsInstance(AppKit.NSObservedObjectKey, str)
        self.assertIsInstance(AppKit.NSObservedKeyPathKey, str)
        self.assertIsInstance(AppKit.NSOptionsKey, str)

        self.assertIsInstance(AppKit.NSAlignmentBinding, str)
        self.assertIsInstance(AppKit.NSAlternateImageBinding, str)
        self.assertIsInstance(AppKit.NSAlternateTitleBinding, str)
        self.assertIsInstance(AppKit.NSAnimateBinding, str)
        self.assertIsInstance(AppKit.NSAnimationDelayBinding, str)
        self.assertIsInstance(AppKit.NSArgumentBinding, str)
        self.assertIsInstance(AppKit.NSAttributedStringBinding, str)
        self.assertIsInstance(AppKit.NSContentArrayBinding, str)
        self.assertIsInstance(AppKit.NSContentArrayForMultipleSelectionBinding, str)
        self.assertIsInstance(AppKit.NSContentBinding, str)
        self.assertIsInstance(AppKit.NSContentHeightBinding, str)
        self.assertIsInstance(AppKit.NSContentObjectBinding, str)
        self.assertIsInstance(AppKit.NSContentObjectsBinding, str)
        self.assertIsInstance(AppKit.NSContentSetBinding, str)
        self.assertIsInstance(AppKit.NSContentValuesBinding, str)
        self.assertIsInstance(AppKit.NSContentWidthBinding, str)
        self.assertIsInstance(AppKit.NSCriticalValueBinding, str)
        self.assertIsInstance(AppKit.NSDataBinding, str)
        self.assertIsInstance(AppKit.NSDisplayPatternTitleBinding, str)
        self.assertIsInstance(AppKit.NSDisplayPatternValueBinding, str)
        self.assertIsInstance(AppKit.NSDocumentEditedBinding, str)
        self.assertIsInstance(AppKit.NSDoubleClickArgumentBinding, str)
        self.assertIsInstance(AppKit.NSDoubleClickTargetBinding, str)
        self.assertIsInstance(AppKit.NSEditableBinding, str)
        self.assertIsInstance(AppKit.NSEnabledBinding, str)
        self.assertIsInstance(AppKit.NSFilterPredicateBinding, str)
        self.assertIsInstance(AppKit.NSFontBinding, str)
        self.assertIsInstance(AppKit.NSFontBoldBinding, str)
        self.assertIsInstance(AppKit.NSFontFamilyNameBinding, str)
        self.assertIsInstance(AppKit.NSFontItalicBinding, str)
        self.assertIsInstance(AppKit.NSFontNameBinding, str)
        self.assertIsInstance(AppKit.NSFontSizeBinding, str)
        self.assertIsInstance(AppKit.NSHeaderTitleBinding, str)
        self.assertIsInstance(AppKit.NSHiddenBinding, str)
        self.assertIsInstance(AppKit.NSImageBinding, str)
        self.assertIsInstance(AppKit.NSIsIndeterminateBinding, str)
        self.assertIsInstance(AppKit.NSLabelBinding, str)
        self.assertIsInstance(AppKit.NSManagedObjectContextBinding, str)
        self.assertIsInstance(AppKit.NSMaximumRecentsBinding, str)
        self.assertIsInstance(AppKit.NSMaxValueBinding, str)
        self.assertIsInstance(AppKit.NSMaxWidthBinding, str)
        self.assertIsInstance(AppKit.NSMinValueBinding, str)
        self.assertIsInstance(AppKit.NSMinWidthBinding, str)
        self.assertIsInstance(AppKit.NSMixedStateImageBinding, str)
        self.assertIsInstance(AppKit.NSOffStateImageBinding, str)
        self.assertIsInstance(AppKit.NSOnStateImageBinding, str)
        self.assertIsInstance(AppKit.NSPredicateBinding, str)
        self.assertIsInstance(AppKit.NSRecentSearchesBinding, str)
        self.assertIsInstance(AppKit.NSRepresentedFilenameBinding, str)
        self.assertIsInstance(AppKit.NSRowHeightBinding, str)
        self.assertIsInstance(AppKit.NSSelectedIdentifierBinding, str)
        self.assertIsInstance(AppKit.NSSelectedIndexBinding, str)
        self.assertIsInstance(AppKit.NSSelectedLabelBinding, str)
        self.assertIsInstance(AppKit.NSSelectedObjectBinding, str)
        self.assertIsInstance(AppKit.NSSelectedObjectsBinding, str)
        self.assertIsInstance(AppKit.NSSelectedTagBinding, str)
        self.assertIsInstance(AppKit.NSSelectedValueBinding, str)
        self.assertIsInstance(AppKit.NSSelectedValuesBinding, str)
        self.assertIsInstance(AppKit.NSSelectionIndexesBinding, str)
        self.assertIsInstance(AppKit.NSSelectionIndexPathsBinding, str)
        self.assertIsInstance(AppKit.NSSortDescriptorsBinding, str)
        self.assertIsInstance(AppKit.NSTargetBinding, str)
        self.assertIsInstance(AppKit.NSTextColorBinding, str)
        self.assertIsInstance(AppKit.NSTitleBinding, str)
        self.assertIsInstance(AppKit.NSToolTipBinding, str)
        self.assertIsInstance(AppKit.NSValueBinding, str)
        self.assertIsInstance(AppKit.NSValuePathBinding, str)
        self.assertIsInstance(AppKit.NSValueURLBinding, str)
        self.assertIsInstance(AppKit.NSVisibleBinding, str)
        self.assertIsInstance(AppKit.NSWarningValueBinding, str)
        self.assertIsInstance(AppKit.NSWidthBinding, str)

        self.assertIsInstance(
            AppKit.NSAllowsEditingMultipleValuesSelectionBindingOption, str
        )
        self.assertIsInstance(AppKit.NSAllowsNullArgumentBindingOption, str)
        self.assertIsInstance(
            AppKit.NSAlwaysPresentsApplicationModalAlertsBindingOption, str
        )
        self.assertIsInstance(AppKit.NSConditionallySetsEditableBindingOption, str)
        self.assertIsInstance(AppKit.NSConditionallySetsEnabledBindingOption, str)
        self.assertIsInstance(AppKit.NSConditionallySetsHiddenBindingOption, str)
        self.assertIsInstance(AppKit.NSContinuouslyUpdatesValueBindingOption, str)
        self.assertIsInstance(AppKit.NSCreatesSortDescriptorBindingOption, str)
        self.assertIsInstance(AppKit.NSDeletesObjectsOnRemoveBindingsOption, str)
        self.assertIsInstance(AppKit.NSDisplayNameBindingOption, str)
        self.assertIsInstance(AppKit.NSDisplayPatternBindingOption, str)
        self.assertIsInstance(AppKit.NSHandlesContentAsCompoundValueBindingOption, str)
        self.assertIsInstance(AppKit.NSInsertsNullPlaceholderBindingOption, str)
        self.assertIsInstance(
            AppKit.NSInvokesSeparatelyWithArrayObjectsBindingOption, str
        )
        self.assertIsInstance(AppKit.NSMultipleValuesPlaceholderBindingOption, str)
        self.assertIsInstance(AppKit.NSNoSelectionPlaceholderBindingOption, str)
        self.assertIsInstance(AppKit.NSNotApplicablePlaceholderBindingOption, str)
        self.assertIsInstance(AppKit.NSNullPlaceholderBindingOption, str)
        self.assertIsInstance(AppKit.NSRaisesForNotApplicableKeysBindingOption, str)
        self.assertIsInstance(AppKit.NSPredicateFormatBindingOption, str)
        self.assertIsInstance(AppKit.NSSelectorNameBindingOption, str)
        self.assertIsInstance(AppKit.NSSelectsAllWhenSettingContentBindingOption, str)
        self.assertIsInstance(AppKit.NSValidatesImmediatelyBindingOption, str)
        self.assertIsInstance(AppKit.NSValueTransformerNameBindingOption, str)
        self.assertIsInstance(AppKit.NSValueTransformerBindingOption, str)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(AppKit.NSContentDictionaryBinding, str)
        self.assertIsInstance(AppKit.NSExcludedKeysBinding, str)
        self.assertIsInstance(AppKit.NSIncludedKeysBinding, str)
        self.assertIsInstance(AppKit.NSInitialKeyBinding, str)
        self.assertIsInstance(AppKit.NSInitialValueBinding, str)
        self.assertIsInstance(AppKit.NSLocalizedKeyDictionaryBinding, str)
        self.assertIsInstance(AppKit.NSTransparentBinding, str)
        self.assertIsInstance(AppKit.NSContentPlacementTagBindingOption, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(AppKit.NSPositioningRectBinding, str)

    def testFunctions(self):
        o = AppKit.NSObject.alloc().init()
        self.assertIs(AppKit.NSIsControllerMarker(o), False)
        self.assertIs(AppKit.NSIsControllerMarker(AppKit.NSMultipleValuesMarker), True)

    def testMethods(self):
        o = TestNSKeyValueBindingHelper.alloc().init()
        m = o.commitEditingWithDelegate_didCommitSelector_contextInfo_.__metadata__()
        self.assertEqual(m["arguments"][3]["sel_of_type"], b"v@:@Z^v")

        self.assertResultIsBOOL(TestNSKeyValueBindingHelper.commitEditing)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(
            TestNSKeyValueBindingHelper.commitEditingAndReturnError_
        )
        self.assertArgIsOut(TestNSKeyValueBindingHelper.commitEditingAndReturnError_, 0)

    @min_sdk_level("10.14")
    def test_protocols(self):
        self.assertProtocolExists("NSEditor")
        self.assertProtocolExists("NSEditorRegistration")
