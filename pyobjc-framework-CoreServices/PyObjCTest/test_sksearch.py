import CoreServices
from PyObjCTools.TestSupport import TestCase, os_level_key, os_release
import objc


class TestSKSearch(TestCase):
    def testTypes(self):
        self.assertIsInstance(CoreServices.SKSearchGroupRef, objc.objc_class)
        self.assertIsInstance(CoreServices.SKSearchResultsRef, objc.objc_class)
        self.assertIsInstance(CoreServices.SKSearchRef, objc.objc_class)

    def testConstants(self):
        self.assertEqual(CoreServices.kSKSearchRanked, 0)
        self.assertEqual(CoreServices.kSKSearchBooleanRanked, 1)
        self.assertEqual(CoreServices.kSKSearchRequiredRanked, 2)
        self.assertEqual(CoreServices.kSKSearchPrefixRanked, 3)

        self.assertEqual(CoreServices.kSKSearchOptionDefault, 0)
        self.assertEqual(CoreServices.kSKSearchOptionNoRelevanceScores, 1)
        self.assertEqual(CoreServices.kSKSearchOptionSpaceMeansOR, 2)
        self.assertEqual(CoreServices.kSKSearchOptionFindSimilar, 4)

    def testFunctions(self):
        self.assertIsInstance(CoreServices.SKSearchGroupGetTypeID(), int)
        self.assertIsInstance(CoreServices.SKSearchResultsGetTypeID(), int)
        self.assertIsInstance(CoreServices.SKSearchGetTypeID(), int)

        data = CoreServices.NSMutableData.data()
        index = CoreServices.SKIndexCreateWithMutableData(
            data, "pyobjc.test", CoreServices.kSKIndexInverted, None
        )
        self.assertIsInstance(index, CoreServices.SKIndexRef)
        doc = CoreServices.SKDocumentCreateWithURL(
            CoreServices.CFURLCreateWithFileSystemPath(
                None,
                "/Library/Documentation/Acknowledgements.rtf",
                CoreServices.kCFURLPOSIXPathStyle,
                False,
            )
        )
        doc2 = CoreServices.SKDocumentCreateWithURL(
            CoreServices.CFURLCreateWithFileSystemPath(
                None,
                "/Library/Documentation/iPod/Acknowledgements.rtf",
                CoreServices.kCFURLPOSIXPathStyle,
                False,
            )
        )
        CoreServices.SKIndexAddDocumentWithText(
            index, doc, "copyright and licenses", True
        )
        CoreServices.SKIndexAddDocumentWithText(
            index, doc2, "copyright and licenses for iPod", True
        )
        CoreServices.SKIndexFlush(index)

        grp = CoreServices.SKSearchGroupCreate([index])
        self.assertIsInstance(grp, CoreServices.SKSearchGroupRef)

        lst = []

        @objc.callbackFor(CoreServices.SKSearchResultsCreateWithQuery)
        def callback(idx, doc, ctx):
            lst.append([idx, doc, ctx])
            return True

        ctx = 10

        orig_res = CoreServices.SKSearchResultsCreateWithQuery(
            grp, "copyright", CoreServices.kSKSearchRequiredRanked, 2, ctx, callback
        )
        self.assertIsInstance(orig_res, CoreServices.SKSearchResultsRef)

        res = CoreServices.SKSearchResultsCreateWithDocuments(
            grp, [doc], 10, ctx, callback
        )
        self.assertIsInstance(res, CoreServices.SKSearchResultsRef)
        self.assertGreaterEqual(len(lst), 2)
        self.assertEqual(lst[0][0], index)
        self.assertIsInstance(lst[0][1], CoreServices.SKDocumentRef)
        self.assertEqual(lst[0][2], ctx)

        cnt = CoreServices.SKSearchResultsGetCount(orig_res)
        self.assertIsInstance(cnt, int)

        if os_level_key(os_release()) < os_level_key("10.7"):
            # The API does not work on macOS 10.7 or later.
            # (Verified with an ObjC reproducer).
            # See issue #9
            self.assertGreater(cnt, 0)

        res = orig_res

        cnt = CoreServices.SKSearchResultsGetCount(res)
        self.assertIsInstance(cnt, int)
        self.assertGreater(cnt, 0)

        v, o1, o2, o3 = CoreServices.SKSearchResultsGetInfoInRange(
            res, CoreServices.CFRange(0, cnt), None, None, None
        )
        self.assertIsInstance(v, int)
        self.assertIsInstance(o1, tuple)
        if o1:
            self.assertIsInstance(o1[0], CoreServices.SKDocumentRef)
        self.assertIsInstance(o2, tuple)
        if o2:
            self.assertIsInstance(o2[0], CoreServices.SKIndexRef)
        self.assertIsInstance(o3, tuple)
        if o3:
            self.assertIsInstance(o3[0], float)

        v = CoreServices.SKSearchResultsCopyMatchingTerms(res, 1)
        # self.assertIsInstance(v, CoreServices.CFArrayRef)

        src = CoreServices.SKSearchCreate(
            index, "copyright", CoreServices.kSKSearchOptionFindSimilar
        )
        self.assertIsInstance(src, CoreServices.SKSearchRef)

        v, o1, o2, o3 = CoreServices.SKSearchFindMatches(src, 10, None, None, 1.0, None)
        self.assertIsInstance(v, bool)
        self.assertIsInstance(o1, tuple)
        if o1:
            self.assertIsInstance(o1[0], int)
        self.assertIsInstance(o2, tuple)
        if o2:
            self.assertIsInstance(o2[0], float)
        self.assertIsInstance(o3, int)

        v1, v2 = CoreServices.SKIndexCopyInfoForDocumentIDs(index, o3, o1, None, None)
        if v1:
            self.assertIsInstance(v1[0], str)
        self.assertIsInstance(v2, tuple)
        if v2:
            self.assertIsInstance(v2[0], int)

        self.assertArgIsIn(CoreServices.SKIndexCopyDocumentRefsForDocumentIDs, 2)
        self.assertArgIsOut(CoreServices.SKIndexCopyDocumentRefsForDocumentIDs, 3)
        self.assertArgSizeInArg(
            CoreServices.SKIndexCopyDocumentRefsForDocumentIDs, 2, 1
        )
        self.assertArgSizeInArg(
            CoreServices.SKIndexCopyDocumentRefsForDocumentIDs, 3, 1
        )
        v = CoreServices.SKIndexCopyDocumentRefsForDocumentIDs(index, o3, o1, None)
        self.assertIsInstance(v, tuple)
        if v:
            self.assertIsInstance(v[0], CoreServices.SKDocumentRef)

        v = CoreServices.SKIndexCopyDocumentURLsForDocumentIDs(index, o3, o1, None)
        self.assertIsInstance(v, tuple)
        if v:
            self.assertIsInstance(v[0], CoreServices.CFURLRef)

        self.assertResultIsCFRetained(CoreServices.SKSearchGroupCopyIndexes)
        a = CoreServices.SKSearchGroupCopyIndexes(grp)
        self.assertIsInstance(a, CoreServices.CFArrayRef)

        CoreServices.SKSearchCancel(src)
