
from PyObjCTools.TestSupport import *
from SearchKit import *
from Foundation import NSMutableData

class TestSKSearch (TestCase):
    def testTypes(self):
        self.failUnlessIsInstance(SKSearchGroupRef, objc.objc_class)
        self.failUnlessIsInstance(SKSearchResultsRef, objc.objc_class)
        self.failUnlessIsInstance(SKSearchRef, objc.objc_class)

    def testConstants(self):
        self.failUnlessEqual(kSKSearchRanked, 0)
        self.failUnlessEqual(kSKSearchBooleanRanked, 1)
        self.failUnlessEqual(kSKSearchRequiredRanked, 2)
        self.failUnlessEqual(kSKSearchPrefixRanked, 3)

        self.failUnlessEqual(kSKSearchOptionDefault, 0)
        self.failUnlessEqual(kSKSearchOptionNoRelevanceScores, 1)
        self.failUnlessEqual(kSKSearchOptionSpaceMeansOR, 2)
        self.failUnlessEqual(kSKSearchOptionFindSimilar, 4)

    def testFunctions(self):
        self.failUnlessIsInstance(SKSearchGroupGetTypeID(), (int, long))
        self.failUnlessIsInstance(SKSearchResultsGetTypeID(), (int, long))
        self.failUnlessIsInstance(SKSearchGetTypeID(), (int, long))

        data = NSMutableData.data()
        index = SKIndexCreateWithMutableData(
                data, "pyobjc.test", kSKIndexInverted, None)
        self.failUnlessIsInstance(index, SKIndexRef)


        grp = SKSearchGroupCreate([index])
        self.failUnlessIsInstance(grp, SKSearchGroupRef)

        self.failUnlessResultIsCFRetained(SKSearchGroupCopyIndexes)
        a = SKSearchGroupCopyIndexes(grp)
        self.failUnlessIsInstance(a, CFArrayRef)

        l = []

        @objc.selectorFor(SKSearchResultsCreateWithQuery)
        def callback(idx, doc, ctx):
            l.append([idx, doc, ctx])

        ctx = 10
        res = SKSearchResultsCreateWithQuery(
                grp, "copyright", kSKSearchRanked, 10, ctx, callback)
        self.failUnlessIsInstance(res, SKSearchResultsRef)
        print l

        v = SKSearchResultsCreateWithDocuments(
                grp, [], 0, ctx, callback)
        self.failUnlessIsInstance(v, SKSearchResultsRef)
        print l

        v = SKSearchResultsGetCount(res)
        self.failUnlessIsInstance(v, (int, long))

        v, o1, o2, o3 = SKSearchResultsGetInfoInRange(res, CFRange(0, 10), None, None, None)
        self.failUnlessIsInstance(v, int)
        self.failUnlessIsInstance(o1, tuple)
        if o1:
            self.failUnlessIsInstance(o1[0], SKDocumentRef)
        self.failUnlessIsInstance(o2, tuple)
        if o2:
            self.failUnlessIsInstance(o2[0], SKIndexRef)
        self.failUnlessIsInstance(o3, tuple)
        if o3:
            self.failUnlessIsInstance(o3[0], float)

        v = SKSearchResultsCopyMatchingTerms(res, 0)
        self.failUnlessIsInstance(v, CFArrayRef)

        src = SKSearchCreate(index, "copyright", kSKSearchOptionFindSimilar)
        self.failUnlessIsInstance(src, SKSearchRef)

        v, o1, o2, o3 = SKSearchFindMatches(src, 10, None, None, 1.0, None)
        self.failUnlessEqual(v, bool)
        self.failUnlessEqual(o1, tuple)
        if o1:
            self.failUnlesssInstance(o1[0], (int, long))
        self.failUnlessEqual(o2, tuple)
        if o2:
            self.failUnlesssInstance(o2[0], (int, long))
        self.failUnlessEqual(o3, float)

        v1, v2 = SKIndexCopyInfoForDocumentIDs(
                index, o3, o1, None, None)
        if v1:
            self.failUnlesssInstance(v1[0], unicode)
        self.failUnlessEqual(v2, tuple)
        if v2:
            self.failUnlesssInstance(v2[0], (int, long))

        v = SKIndexCopyDocumentRefsForDocumentIDs(
            index,
            o3, o1, None)
        self.failUnlessIsInstance(v, tuple)
        if v:
            self.failUnlessIsInstance(v[0], SKDocumentRef)

        v = SKIndexCopyDocumentURLsForDocumentIDs(
                index, o3, o1, None)
        self.failUnlessIsInstance(v, tuple)
        if v:
            self.failUnlessIsInstance(v[0], CFURLRef)

        SKSearchCancel(src)

if __name__ == "__main__":
    main()
