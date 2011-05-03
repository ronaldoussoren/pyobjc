
from PyObjCTools.TestSupport import *
from SearchKit import *
from Foundation import NSMutableData

class TestSKSearch (TestCase):
    def testTypes(self):
        self.assertIsInstance(SKSearchGroupRef, objc.objc_class)
        self.assertIsInstance(SKSearchResultsRef, objc.objc_class)
        self.assertIsInstance(SKSearchRef, objc.objc_class)

    def testConstants(self):
        self.assertEqual(kSKSearchRanked, 0)
        self.assertEqual(kSKSearchBooleanRanked, 1)
        self.assertEqual(kSKSearchRequiredRanked, 2)
        self.assertEqual(kSKSearchPrefixRanked, 3)

        self.assertEqual(kSKSearchOptionDefault, 0)
        self.assertEqual(kSKSearchOptionNoRelevanceScores, 1)
        self.assertEqual(kSKSearchOptionSpaceMeansOR, 2)
        self.assertEqual(kSKSearchOptionFindSimilar, 4)

    def testFunctions(self):
        self.assertIsInstance(SKSearchGroupGetTypeID(), (int, long))
        self.assertIsInstance(SKSearchResultsGetTypeID(), (int, long))
        self.assertIsInstance(SKSearchGetTypeID(), (int, long))

        data = NSMutableData.data()
        index = SKIndexCreateWithMutableData(
                data, "pyobjc.test", kSKIndexInverted, None)
        self.assertIsInstance(index, SKIndexRef)
        doc = SKDocumentCreateWithURL(
            CFURLCreateWithFileSystemPath(
            None, u"/Library/Documentation/Acknowledgements.rtf",
            kCFURLPOSIXPathStyle, False))
        doc2 = SKDocumentCreateWithURL(
            CFURLCreateWithFileSystemPath(
            None, u"/Library/Documentation/iPod/Acknowledgements.rtf",
            kCFURLPOSIXPathStyle, False))
        SKIndexAddDocumentWithText(index, doc, "copyright and licenses", True)
        SKIndexAddDocumentWithText(index, doc2, "copyright and licenses for iPod", True)
        SKIndexFlush(index)


        grp = SKSearchGroupCreate([index])
        self.assertIsInstance(grp, SKSearchGroupRef)


        l = []

        @objc.callbackFor(SKSearchResultsCreateWithQuery)
        def callback(idx, doc, ctx):
            l.append([idx, doc, ctx])
            return True

        ctx = 10

        res = SKSearchResultsCreateWithQuery(
                grp, u"apache", kSKSearchRequiredRanked, 2, ctx, callback)
        self.assertIsInstance(res, SKSearchResultsRef)

        res = SKSearchResultsCreateWithDocuments(
                grp, [doc], 10, ctx, callback)
        self.assertIsInstance(res, SKSearchResultsRef)
        self.assertEqual(len(l), 2)
        self.assertEqual(l[0][0], index)
        self.assertIsInstance(l[0][1], SKDocumentRef)
        self.assertEqual(l[0][2], ctx)

        cnt = SKSearchResultsGetCount(res)
        self.assertIsInstance(cnt, (int, long))
        self.failUnless(cnt > 0)


        v, o1, o2, o3 = SKSearchResultsGetInfoInRange(res, CFRange(0, cnt), None, None, None)
        self.assertIsInstance(v, int)
        self.assertIsInstance(o1, tuple)
        if o1:
            self.assertIsInstance(o1[0], SKDocumentRef)
        self.assertIsInstance(o2, tuple)
        if o2:
            self.assertIsInstance(o2[0], SKIndexRef)
        self.assertIsInstance(o3, tuple)
        if o3:
            self.assertIsInstance(o3[0], float)

        v = SKSearchResultsCopyMatchingTerms(res, 1)
        self.assertIsInstance(v, CFArrayRef)

        src = SKSearchCreate(index, "copyright", kSKSearchOptionFindSimilar)
        self.assertIsInstance(src, SKSearchRef)

        v, o1, o2, o3 = SKSearchFindMatches(src, 10, None, None, 1.0, None)
        self.assertIsInstance(v, bool)
        self.assertIsInstance(o1, tuple)
        if o1:
            self.assertIsInstance(o1[0], (int, long))
        self.assertIsInstance(o2, tuple)
        if o2:
            self.assertIsInstance(o2[0], float)
        self.assertIsInstance(o3, (int, long))

        v1, v2 = SKIndexCopyInfoForDocumentIDs(
                index, o3, o1, None, None)
        if v1:
            self.assertIsInstance(v1[0], unicode)
        self.assertIsInstance(v2, tuple)
        if v2:
            self.assertIsInstance(v2[0], (int, long))

        v = SKIndexCopyDocumentRefsForDocumentIDs(
            index, o3, o1, None)
        self.assertIsInstance(v, tuple)
        if v:
            self.assertIsInstance(v[0], SKDocumentRef)

        v = SKIndexCopyDocumentURLsForDocumentIDs(
                index, o3, o1, None)
        self.assertIsInstance(v, tuple)
        if v:
            self.assertIsInstance(v[0], CFURLRef)

        self.assertResultIsCFRetained(SKSearchGroupCopyIndexes)
        a = SKSearchGroupCopyIndexes(grp)
        self.assertIsInstance(a, CFArrayRef)

        SKSearchCancel(src)

if __name__ == "__main__":
    main()
