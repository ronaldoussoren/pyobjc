
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
        self.failUnlessIsInstance(grp, SKSearchGroupRef)


        l = []

        @objc.callbackFor(SKSearchResultsCreateWithQuery)
        def callback(idx, doc, ctx):
            l.append([idx, doc, ctx])
            return True

        ctx = 10

        res = SKSearchResultsCreateWithQuery(
                grp, u"apache", kSKSearchRequiredRanked, 2, ctx, callback)
        self.failUnlessIsInstance(res, SKSearchResultsRef)

        res = SKSearchResultsCreateWithDocuments(
                grp, [doc], 10, ctx, callback)
        self.failUnlessIsInstance(res, SKSearchResultsRef)
        self.failUnlessEqual(len(l), 2)
        self.failUnlessEqual(l[0][0], index)
        self.failUnlessIsInstance(l[0][1], SKDocumentRef)
        self.failUnlessEqual(l[0][2], ctx)

        cnt = SKSearchResultsGetCount(res)
        self.failUnlessIsInstance(cnt, (int, long))
        self.failUnless(cnt > 0)


        v, o1, o2, o3 = SKSearchResultsGetInfoInRange(res, CFRange(0, cnt), None, None, None)
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

        v = SKSearchResultsCopyMatchingTerms(res, 1)
        self.failUnlessIsInstance(v, CFArrayRef)

        src = SKSearchCreate(index, "copyright", kSKSearchOptionFindSimilar)
        self.failUnlessIsInstance(src, SKSearchRef)

        v, o1, o2, o3 = SKSearchFindMatches(src, 10, None, None, 1.0, None)
        self.failUnlessIsInstance(v, bool)
        self.failUnlessIsInstance(o1, tuple)
        if o1:
            self.failUnlessIsInstance(o1[0], (int, long))
        self.failUnlessIsInstance(o2, tuple)
        if o2:
            self.failUnlessIsInstance(o2[0], float)
        self.failUnlessIsInstance(o3, (int, long))

        v1, v2 = SKIndexCopyInfoForDocumentIDs(
                index, o3, o1, None, None)
        if v1:
            self.failUnlessIsInstance(v1[0], unicode)
        self.failUnlessIsInstance(v2, tuple)
        if v2:
            self.failUnlessIsInstance(v2[0], (int, long))

        v = SKIndexCopyDocumentRefsForDocumentIDs(
            index, o3, o1, None)
        self.failUnlessIsInstance(v, tuple)
        if v:
            self.failUnlessIsInstance(v[0], SKDocumentRef)

        v = SKIndexCopyDocumentURLsForDocumentIDs(
                index, o3, o1, None)
        self.failUnlessIsInstance(v, tuple)
        if v:
            self.failUnlessIsInstance(v[0], CFURLRef)

        self.failUnlessResultIsCFRetained(SKSearchGroupCopyIndexes)
        a = SKSearchGroupCopyIndexes(grp)
        self.failUnlessIsInstance(a, CFArrayRef)

        SKSearchCancel(src)

if __name__ == "__main__":
    main()
