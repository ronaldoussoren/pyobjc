
from PyObjCTools.TestSupport import *
from LatentSemanticMapping import *
import os

class TestLatentSemanticMapping (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kLSMMapOutOfState, -6640)
        self.failUnlessEqual(kLSMMapNoSuchCategory, -6641)
        self.failUnlessEqual(kLSMMapWriteError, -6642)
        self.failUnlessEqual(kLSMMapBadPath, -6643)
        self.failUnlessEqual(kLSMMapBadCluster, -6644)

        self.failUnlessEqual(kLSMMapPairs, 1)
        self.failUnlessEqual(kLSMMapTriplets, 2)
        self.failUnlessEqual(kLSMMapHashText, 256)

        self.failUnlessEqual(kLSMAlgorithmKey, "LSMAlgorithm")
        self.failUnlessEqual(kLSMAlgorithmDense, "LSMAlgorithmDense")
        self.failUnlessEqual(kLSMAlgorithmSparse, "LSMAlgorithmSparse")
        self.failUnlessEqual(kLSMPrecisionKey, "LSMPrecision")
        self.failUnlessEqual(kLSMPrecisionFloat, "LSMPrecisionFloat")
        self.failUnlessEqual(kLSMPrecisionDouble, "LSMPrecisionDouble")
        self.failUnlessEqual(kLSMDimensionKey, "LSMDimension")
        self.failUnlessEqual(kLSMIterationsKey, "LSMIterations")
        self.failUnlessEqual(kLSMSweepAgeKey, "LSMSweepAge")
        self.failUnlessEqual(kLSMSweepCutoffKey, "LSMSweepCutoff")

        self.failUnlessEqual(kLSMClusterCategories, 0)
        self.failUnlessEqual(kLSMClusterWords, 1)
        self.failUnlessEqual(kLSMClusterTokens, 2)
        self.failUnlessEqual(kLSMClusterKMeans, 0)
        self.failUnlessEqual(kLSMClusterAgglomerative, 4)

        self.failUnlessEqual(kLSMResultBestWords, 1)

        self.failUnlessEqual(kLSMMapDiscardCounts, 1)
        self.failUnlessEqual(kLSMMapLoadMutable,  2)

        self.failUnlessEqual(kLSMTextPreserveCase, 1)
        self.failUnlessEqual(kLSMTextPreserveAcronyms, 2)
        self.failUnlessEqual(kLSMTextApplySpamHeuristics, 4)






    def testTypes(self):
        self.failUnlessIsInstance(LSMMapRef, objc.objc_class)
        self.failUnlessIsInstance(LSMTextRef, objc.objc_class)
        self.failUnlessIsInstance(LSMResultRef, objc.objc_class)

    def testFunctions(self):
        self.failUnlessIsInstance(LSMMapGetTypeID(), (int, long))
        self.failUnlessIsInstance(LSMTextGetTypeID(), (int, long))
        self.failUnlessIsInstance(LSMResultGetTypeID(), (int, long))

        self.failUnlessResultIsCFRetained(LSMMapCreate)
        map = LSMMapCreate(None, kLSMMapPairs)
        self.failUnlessIsInstance(map, LSMMapRef)

        v = LSMMapGetProperties(map)
        self.failUnlessIsInstance(v, CFDictionaryRef)

        LSMMapSetProperties(map, {u"key": u"value"})
        v = LSMMapGetProperties(map)
        self.failUnlessIsInstance(v, CFDictionaryRef)

        v = LSMMapStartTraining(map)
        self.failUnlessIsInstance(v, (int, long))

        cat = LSMMapAddCategory(map)
        self.failUnlessIsInstance(cat, (int, long))

        cat2 = LSMMapAddCategory(map)
        self.failUnlessIsInstance(cat2, (int, long))

        v = LSMMapGetCategoryCount(map)
        self.failUnlessIsInstance(v, (int, long))

        text = LSMTextCreate(None, map)
        self.failUnlessIsInstance(text, LSMTextRef)
        text2 = LSMTextCreate(None, map)
        self.failUnlessIsInstance(text2, LSMTextRef)
        words = LSMTextCreate(None, map)
        self.failUnlessIsInstance(words, LSMTextRef)

        v = LSMTextAddWord(words, "hello")
        self.failUnlessIsInstance(v, (int, long))
        v = LSMTextAddWord(words, "world")
        self.failUnlessIsInstance(v, (int, long))

        v = LSMTextAddWords(text, "the world goes on and on",
                CFLocaleCopyCurrent(), 0)
        self.failUnlessIsInstance(v, (int, long))
        v = LSMTextAddWords(text2, "on a bright and sunny morning",
                CFLocaleCopyCurrent(), 0)
        self.failUnlessIsInstance(v, (int, long))

        v = LSMMapSetStopWords(map, words)
        self.failUnlessIsInstance(v, (int, long))

        v = LSMMapAddText(map, text, cat)
        self.failUnlessIsInstance(v, (int, long))

        v = LSMMapAddTextWithWeight(map, text2, cat2, 2.0)
        self.failUnlessIsInstance(v, (int, long))

        v = LSMMapCompile(map)
        self.failUnlessIsInstance(v, (int, long))

        text3 = LSMTextCreate(None, map)
        self.failUnlessIsInstance(text2, LSMTextRef)
        v = LSMTextAddWords(text3, "foo the bar and worlds away",
                CFLocaleCopyCurrent(), 0)

        v = LSMMapCreateClusters(None, map, None, 2, 0)
        self.failUnlessIsInstance(v, CFArrayRef)

        v = LSMMapApplyClusters(map, v);
        self.failUnlessIsInstance(v, (int, long))

        mytext = LSMTextCreate(None, map)
        v = LSMTextAddWords(text, "the world goes on and on",
                                CFLocaleCopyCurrent(), 0)
        self.failUnlessIsInstance(v, (int, long))

        res = LSMResultCreate(None, map, mytext, 2, 0)
        self.failUnlessIsInstance(res, LSMResultRef)

        v = LSMResultGetCount(res);
        self.failUnlessIsInstance(v, (int, long))
        self.failUnless(v)

        v = LSMResultGetCategory(res, 0)
        self.failUnlessIsInstance(v, (int, long))

        v = LSMResultGetScore(res, 0)
        self.failUnlessIsInstance(v, float)

        v = LSMResultCopyWord(res, 0)
        self.failUnlessIsInstance(v, unicode)

        v = LSMResultCopyToken(res, 0)
        self.failUnlessIsInstance(v, CFDataRef)

        v = LSMTextAddToken(text, v)
        self.failUnlessIsInstance(v, (int, long))

        v = LSMResultCopyWordCluster(res, 0)
        self.failUnlessIsInstance(v, CFArrayRef)

        v = LSMResultCopyTokenCluster(res, 0)
        self.failUnlessIsInstance(v, CFArrayRef)

        fn = '/tmp/pyobjc.test'
        url = CFURLCreateWithFileSystemPath(None, fn, kCFURLPOSIXPathStyle, False)
        self.failUnlessIsInstance(url, CFURLRef)
        v = LSMMapWriteToURL(map, url, 0)
        self.failUnlessIsInstance(v, (int, long))

        map2 = LSMMapCreateFromURL(None, url, 0)
        self.failUnlessIsInstance(map2, LSMMapRef)

        if os.path.exists(fn):
            os.unlink(fn)

        fp = CFWriteStreamCreateWithAllocatedBuffers(None, None)
        self.failUnlessIsInstance(fp, CFWriteStreamRef)
        CFWriteStreamOpen(fp)

        v = LSMMapWriteToStream(map, text, fp, 0)
        sel.failUnlessIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
