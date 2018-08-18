from PyObjCTools.TestSupport import *

import CoreServices

class TestMDQuery (TestCase):
    @expectedFailure
    def test_types(self):
        self.assertIsCFType(CoreServices.MDQueryRef)

    def test_functions(self):
        self.assertIsInstance(CoreServices.MDQueryGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CoreServices.MDQueryCreate)
        self.assertResultIsCFRetained(CoreServices.MDQueryCreateSubset)
        self.assertResultIsCFRetained(CoreServices.MDQueryCreateForItems)
        self.assertResultIsCFRetained(CoreServices.MDQueryCopyQueryString)
        self.assertResultIsCFRetained(CoreServices.MDQueryCopyValueListAttributes)
        self.assertResultIsCFRetained(CoreServices.MDQueryCopySortingAttributes)

        CoreServices.MDQueryGetBatchingParameters
        CoreServices.MDQuerySetBatchingParameters

        self.assertArgIsFunction(CoreServices.MDQuerySetCreateResultFunction, 1, b'^v^{__MDQuery=}^{__MDItem=}^v', 1)
        # XXX: ArrayCallbacks for argument 2, must be None?

        self.assertArgIsFunction(CoreServices.MDQuerySetCreateValueFunction, 1, b'^v^{__MDQuery=}^{__CFString=}@^v', 1)
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

        self.assertResultHasType(CoreServices.MDQueryGetAttributeValueOfResultAtIndex, objc._C_ID)

        CoreServices.MDQueryCopyValuesOfAttribute
        CoreServices.MDQueryGetCountOfResultsWithAttributeValue

        self.assertArgIsFunction(CoreServices.MDQuerySetSortComparator, 1, objc._C_NSInteger + b'n^@n^@^v', 1)
        self.assertArgIsBlock(CoreServices.MDQuerySetSortComparatorBlock, 1, objc._C_NSInteger + b'n^@n^@')

        CoreServices.MDQuerySetSearchScope
        CoreServices.MDQuerySetMaxCount


    @min_os_level('10.7')
    def test_functions10_7(self):
        self.assertResultIsBOOL(CoreServices.MDQuerySetSortOrder)
        CoreServices.MDQuerySetSortOptionFlagsForAttribute

    @min_os_level('10.7')
    @expectedFailure
    def test_functions_10_7_missing(self):
        CoreServices.MDQueryGetSortOptionFlagsForAttribute


    def test_structs(self):
        v =  CoreServices.MDQueryBatchingParams()
        self.assertEqual(v.first_max_num, 0)
        self.assertEqual(v.first_max_ms, 0)
        self.assertEqual(v.progress_max_num, 0)
        self.assertEqual(v.progress_max_ms, 0)
        self.assertEqual(v.update_max_num, 0)
        self.assertEqual(v.update_max_ms, 0)


    def test_constants(self):
        self.assertEqual(CoreServices.kMDQuerySynchronous, 1)
        self.assertEqual(CoreServices.kMDQueryWantsUpdates, 4)
        self.assertEqual(CoreServices.kMDQueryAllowFSTranslation, 8)

        self.assertEqual(CoreServices. kMDQueryReverseSortOrderFlag, 1<<0)

        self.assertIsInstance(CoreServices.kMDQueryProgressNotification, unicode)
        self.assertIsInstance(CoreServices.kMDQueryDidFinishNotification, unicode)
        self.assertIsInstance(CoreServices.kMDQueryDidUpdateNotification, unicode)
        self.assertIsInstance(CoreServices.kMDQueryUpdateAddedItems, unicode)
        self.assertIsInstance(CoreServices.kMDQueryUpdateChangedItems, unicode)
        self.assertIsInstance(CoreServices.kMDQueryUpdateRemovedItems, unicode)
        self.assertIsInstance(CoreServices.kMDQueryResultContentRelevance, unicode)
        self.assertIsInstance(CoreServices.kMDQueryScopeHome, unicode)
        self.assertIsInstance(CoreServices.kMDQueryScopeComputer, unicode)
        self.assertIsInstance(CoreServices.kMDQueryScopeNetwork, unicode)

    def test_constants10_6(self):
        self.assertIsInstance(CoreServices.kMDQueryScopeAllIndexed, unicode)
        self.assertIsInstance(CoreServices.kMDQueryScopeComputerIndexed, unicode)
        self.assertIsInstance(CoreServices.kMDQueryScopeNetworkIndexed, unicode)


if __name__ == "__main__":
    main()
