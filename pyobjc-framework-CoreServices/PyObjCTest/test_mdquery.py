import CoreServices
from PyObjCTools.TestSupport import TestCase, expectedFailure
import objc


class TestMDQuery(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreServices.MDQueryOptionFlags)
        self.assertEqual(CoreServices.kMDQuerySynchronous, 1)
        self.assertEqual(CoreServices.kMDQueryWantsUpdates, 4)
        self.assertEqual(CoreServices.kMDQueryAllowFSTranslation, 8)

        self.assertIsEnumType(CoreServices.MDQuerySortOptionFlags)
        self.assertEqual(CoreServices.kMDQueryReverseSortOrderFlag, 1 << 0)

    def test_constants(self):
        self.assertIsInstance(CoreServices.kMDQueryProgressNotification, str)
        self.assertIsInstance(CoreServices.kMDQueryDidFinishNotification, str)
        self.assertIsInstance(CoreServices.kMDQueryDidUpdateNotification, str)
        self.assertIsInstance(CoreServices.kMDQueryUpdateAddedItems, str)
        self.assertIsInstance(CoreServices.kMDQueryUpdateChangedItems, str)
        self.assertIsInstance(CoreServices.kMDQueryUpdateRemovedItems, str)
        self.assertIsInstance(CoreServices.kMDQueryResultContentRelevance, str)
        self.assertIsInstance(CoreServices.kMDQueryScopeHome, str)
        self.assertIsInstance(CoreServices.kMDQueryScopeComputer, str)
        self.assertIsInstance(CoreServices.kMDQueryScopeNetwork, str)

        self.assertIsInstance(CoreServices.kMDQueryScopeAllIndexed, str)
        self.assertIsInstance(CoreServices.kMDQueryScopeComputerIndexed, str)
        self.assertIsInstance(CoreServices.kMDQueryScopeNetworkIndexed, str)

    @expectedFailure
    def test_types(self):
        self.assertIsCFType(CoreServices.MDQueryRef)

    def test_functions(self):
        self.assertIsInstance(CoreServices.MDQueryGetTypeID(), int)

        self.assertResultIsCFRetained(CoreServices.MDQueryCreate)
        self.assertResultIsCFRetained(CoreServices.MDQueryCreateSubset)
        self.assertResultIsCFRetained(CoreServices.MDQueryCreateForItems)
        self.assertResultIsCFRetained(CoreServices.MDQueryCopyQueryString)
        self.assertResultIsCFRetained(CoreServices.MDQueryCopyValueListAttributes)
        self.assertResultIsCFRetained(CoreServices.MDQueryCopySortingAttributes)

        CoreServices.MDQueryGetBatchingParameters
        CoreServices.MDQuerySetBatchingParameters

        self.assertArgIsFunction(
            CoreServices.MDQuerySetCreateResultFunction,
            1,
            b"^v^{__MDQuery=}^{__MDItem=}^v",
            1,
        )
        # XXX: ArrayCallbacks for argument 2, must be None?

        self.assertArgIsFunction(
            CoreServices.MDQuerySetCreateValueFunction,
            1,
            b"^v^{__MDQuery=}^{__CFString=}@^v",
            1,
        )
        # XXX: ArrayCallbacks for argument 2, must be None?

        CoreServices.MDQuerySetDispatchQueue

        self.assertResultIsBOOL(CoreServices.MDQueryExecute)

        CoreServices.MDQueryStop
        CoreServices.MDQueryDisableUpdates
        CoreServices.MDQueryEnableUpdates

        self.assertResultIsBOOL(CoreServices.MDQueryIsGatheringComplete)

        CoreServices.MDQueryGetResultCount

        self.assertResultHasType(CoreServices.MDQueryGetResultAtIndex, objc._C_ID)

        self.assertArgHasType(CoreServices.MDQueryGetIndexOfResult, 1, objc._C_ID)

        self.assertResultHasType(
            CoreServices.MDQueryGetAttributeValueOfResultAtIndex, objc._C_ID
        )

        CoreServices.MDQueryCopyValuesOfAttribute
        CoreServices.MDQueryGetCountOfResultsWithAttributeValue

        self.assertArgIsFunction(
            CoreServices.MDQuerySetSortComparator, 1, objc._C_NSInteger + b"n^@n^@^v", 1
        )
        self.assertArgIsBlock(
            CoreServices.MDQuerySetSortComparatorBlock, 1, objc._C_NSInteger + b"n^@n^@"
        )

        CoreServices.MDQuerySetSearchScope
        CoreServices.MDQuerySetMaxCount

        self.assertResultIsBOOL(CoreServices.MDQuerySetSortOrder)
        CoreServices.MDQuerySetSortOptionFlagsForAttribute

    def test_structs(self):
        v = CoreServices.MDQueryBatchingParams()
        self.assertEqual(v.first_max_num, 0)
        self.assertEqual(v.first_max_ms, 0)
        self.assertEqual(v.progress_max_num, 0)
        self.assertEqual(v.progress_max_ms, 0)
        self.assertEqual(v.update_max_num, 0)
        self.assertEqual(v.update_max_ms, 0)
        self.assertPickleRoundTrips(v)
