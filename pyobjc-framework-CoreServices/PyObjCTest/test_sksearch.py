
from PyObjCTools.TestSupport import *
import CoreServices

class TestSKSearch (TestCase):
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
        self.assertIsInstance(CoreServices.SKSearchGroupGetTypeID(), (int, long))
        self.assertIsInstance(CoreServices.SKSearchResultsGetTypeID(), (int, long))
        self.assertIsInstance(CoreServices.SKSearchGetTypeID(), (int, long))

        data = CoreServices.NSMutableData.data()
        index = CoreServices.SKIndexCreateWithMutableData(
                data, "pyobjc.test", CoreServices.kSKIndexInverted, None)
        self.assertIsInstance(index, CoreServices.SKIndexRef)
        doc = CoreServices.SKDocumentCreateWithURL(
            CoreServices.CFURLCreateWithFileSystemPath(
            None, b"/Library/Documentation/Acknowledgements.rtf".decode('latin1'),
            CoreServices.kCFURLPOSIXPathStyle, False))
        doc2 = CoreServices.SKDocumentCreateWithURL(
            CoreServices.CFURLCreateWithFileSystemPath(
            None, b"/Library/Documentation/iPod/Acknowledgements.rtf".decode('latin1'),
            CoreServices.kCFURLPOSIXPathStyle, False))
        CoreServices.SKIndexAddDocumentWithText(index, doc, "copyright and licenses", True)
        CoreServices.SKIndexAddDocumentWithText(index, doc2, "copyright and licenses for iPod", True)
        CoreServices.SKIndexFlush(index)


        grp = CoreServices.SKSearchGroupCreate([index])
        self.assertIsInstance(grp, CoreServices.SKSearchGroupRef)


        l = []

        @objc.callbackFor(CoreServices.SKSearchResultsCreateWithQuery)
        def callback(idx, doc, ctx):
            l.append([idx, doc, ctx])
            return True


        ctx = 10

        res = CoreServices.SKSearchResultsCreateWithQuery(
                grp, b"copyright".decode('latin1'), CoreServices.kSKSearchRequiredRanked, 2, ctx, callback)
        self.assertIsInstance(res, CoreServices.SKSearchResultsRef)

        res = CoreServices.SKSearchResultsCreateWithDocuments(
                grp, [doc], 10, ctx, callback)
        self.assertIsInstance(res, CoreServices.SKSearchResultsRef)
        self.assertGreaterEqual(len(l), 2)
        self.assertEqual(l[0][0], index)
        self.assertIsInstance(l[0][1], CoreServices.SKDocumentRef)
        self.assertEqual(l[0][2], ctx)

        cnt = CoreServices.SKSearchResultsGetCount(res)
        self.assertIsInstance(cnt, (int, long))

        if cnt == 0:
            # XXX: For some reason this doesn't work on OSX 10.7,
            # reason is unclear for now.
            pass
            return


        self.failUnless(cnt > 0)


        v, o1, o2, o3 = CoreServices.SKSearchResultsGetInfoInRange(res, CFRange(0, cnt), None, None, None)
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
        self.assertIsInstance(v, CoreServices.CFArrayRef)

        src = CoreServices.SKSearchCreate(index, "copyright", kSKSearchOptionFindSimilar)
        self.assertIsInstance(src, CoreServices.SKSearchRef)

        v, o1, o2, o3 = CoreServices.SKSearchFindMatches(src, 10, None, None, 1.0, None)
        self.assertIsInstance(v, bool)
        self.assertIsInstance(o1, tuple)
        if o1:
            self.assertIsInstance(o1[0], (int, long))
        self.assertIsInstance(o2, tuple)
        if o2:
            self.assertIsInstance(o2[0], float)
        self.assertIsInstance(o3, (int, long))

        v1, v2 = CoreServices.SKIndexCopyInfoForDocumentIDs(
                index, o3, o1, None, None)
        if v1:
            self.assertIsInstance(v1[0], unicode)
        self.assertIsInstance(v2, tuple)
        if v2:
            self.assertIsInstance(v2[0], (int, long))

        v = CoreServices.SKIndexCopyDocumentRefsForDocumentIDs(
            index, o3, o1, None)
        self.assertIsInstance(v, tuple)
        if v:
            self.assertIsInstance(v[0], CoreServices.SKDocumentRef)

        v = CoreServices.SKIndexCopyDocumentURLsForDocumentIDs(
                index, o3, o1, None)
        self.assertIsInstance(v, tuple)
        if v:
            self.assertIsInstance(v[0], CoreServices.CFURLRef)

        self.assertResultIsCFRetained(CoreServices.SKSearchGroupCopyIndexes)
        a = CoreServices.SKSearchGroupCopyIndexes(grp)
        self.assertIsInstance(a, CoreServices.CFArrayRef)

        CoreServices.SKSearchCancel(src)

if __name__ == "__main__":
    main()
