
from PyObjCTools.TestSupport import *
from LatentSemanticMapping import *
import os

try:
    long
except NameError:
    long = int

try:
    unicode
except NameError:
    unicode = str

class TestLatentSemanticMapping (TestCase):
    def testConstants(self):
        self.assertEqual(kLSMMapOutOfState, -6640)
        self.assertEqual(kLSMMapNoSuchCategory, -6641)
        self.assertEqual(kLSMMapWriteError, -6642)
        self.assertEqual(kLSMMapBadPath, -6643)
        self.assertEqual(kLSMMapBadCluster, -6644)

        self.assertEqual(kLSMMapPairs, 1)
        self.assertEqual(kLSMMapTriplets, 2)
        self.assertEqual(kLSMMapHashText, 256)

        self.assertEqual(kLSMAlgorithmKey, "LSMAlgorithm")
        self.assertEqual(kLSMAlgorithmDense, "LSMAlgorithmDense")
        self.assertEqual(kLSMAlgorithmSparse, "LSMAlgorithmSparse")
        self.assertEqual(kLSMPrecisionKey, "LSMPrecision")
        self.assertEqual(kLSMPrecisionFloat, "LSMPrecisionFloat")
        self.assertEqual(kLSMPrecisionDouble, "LSMPrecisionDouble")
        self.assertEqual(kLSMDimensionKey, "LSMDimension")
        self.assertEqual(kLSMIterationsKey, "LSMIterations")
        self.assertEqual(kLSMSweepAgeKey, "LSMSweepAge")
        self.assertEqual(kLSMSweepCutoffKey, "LSMSweepCutoff")

        self.assertEqual(kLSMClusterCategories, 0)
        self.assertEqual(kLSMClusterWords, 1)
        self.assertEqual(kLSMClusterTokens, 2)
        self.assertEqual(kLSMClusterKMeans, 0)
        self.assertEqual(kLSMClusterAgglomerative, 4)

        self.assertEqual(kLSMResultBestWords, 1)

        self.assertEqual(kLSMMapDiscardCounts, 1)
        self.assertEqual(kLSMMapLoadMutable,  2)

        self.assertEqual(kLSMTextPreserveCase, 1)
        self.assertEqual(kLSMTextPreserveAcronyms, 2)
        self.assertEqual(kLSMTextApplySpamHeuristics, 4)






    def testTypes(self):
        self.assertIsInstance(LSMMapRef, objc.objc_class)
        self.assertIsInstance(LSMTextRef, objc.objc_class)
        self.assertIsInstance(LSMResultRef, objc.objc_class)

    def testFunctions(self):
        self.assertIsInstance(LSMMapGetTypeID(), (int, long))
        self.assertIsInstance(LSMTextGetTypeID(), (int, long))
        self.assertIsInstance(LSMResultGetTypeID(), (int, long))

        self.assertResultIsCFRetained(LSMMapCreate)
        map = LSMMapCreate(None, kLSMMapPairs)
        self.assertIsInstance(map, LSMMapRef)

        v = LSMMapGetProperties(map)
        self.assertIsInstance(v, CFDictionaryRef)

        LSMMapSetProperties(map, {b"key".decode('latin1'): b"value".decode('latin1')})
        v = LSMMapGetProperties(map)
        self.assertIsInstance(v, CFDictionaryRef)

        v = LSMMapStartTraining(map)
        self.assertIsInstance(v, (int, long))

        cat = LSMMapAddCategory(map)
        self.assertIsInstance(cat, (int, long))

        cat2 = LSMMapAddCategory(map)
        self.assertIsInstance(cat2, (int, long))

        v = LSMMapGetCategoryCount(map)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(LSMTextCreate)
        text = LSMTextCreate(None, map)
        self.assertIsInstance(text, LSMTextRef)
        text2 = LSMTextCreate(None, map)
        self.assertIsInstance(text2, LSMTextRef)
        words = LSMTextCreate(None, map)
        self.assertIsInstance(words, LSMTextRef)

        v = LSMTextAddWord(words, "the")
        self.assertIsInstance(v, (int, long))
        v = LSMTextAddWord(words, "and")
        self.assertIsInstance(v, (int, long))

        v = LSMTextAddWords(text, "the world goes on and on",
                CFLocaleCopyCurrent(), 0)
        self.assertIsInstance(v, (int, long))
        v = LSMTextAddWords(text2, "on a bright and sunny morning",
                CFLocaleCopyCurrent(), 0)
        self.assertIsInstance(v, (int, long))

        v = LSMMapSetStopWords(map, words)
        self.assertIsInstance(v, (int, long))

        v = LSMMapAddText(map, text, cat)
        self.assertIsInstance(v, (int, long))

        fn = __file__
        fn = os.path.splitext(fn)[0] + ".py"
        for line in open(fn, 'r'):
            t = LSMTextCreate(None, map)
            LSMTextAddWords(t, line, CFLocaleCopyCurrent(), 0)
            LSMMapAddText(map, t, cat)


        v = LSMMapAddTextWithWeight(map, text2, cat2, 2.0)
        self.assertIsInstance(v, (int, long))

        v = LSMMapCompile(map)
        self.assertIsInstance(v, (int, long))

        text3 = LSMTextCreate(None, map)
        self.assertIsInstance(text2, LSMTextRef)
        v = LSMTextAddWords(text3, "foo the bar and worlds away",
                CFLocaleCopyCurrent(), 0)

        if 0:
            self.assertResultIsCFRetained(LSMMapCreateClusters)
            clusters = LSMMapCreateClusters(None, map, None, 3,  0)
            self.assertIsInstance(clusters, CFArrayRef)

            v = LSMMapApplyClusters(map, clusters);
            self.assertIsInstance(clusters, (int, long))

        v = LSMMapStartTraining(map)

        mytext = LSMTextCreate(None, map)
        v = LSMTextAddWords(mytext, "the world goes on and on",
                                CFLocaleCopyCurrent(), 0)
        self.assertIsInstance(v, (int, long))

        v = LSMMapCompile(map)

        # FIXME: Tests crash, probably due to misuse of the
        # APIs. I haven't found usable API docs for this
        # framework :-(
        return

        self.assertResultIsCFRetained(LSMResultCreate)
        res = LSMResultCreate(None, map, mytext, 2, 0)
        self.assertIsInstance(res, LSMResultRef)

        v = LSMResultGetCount(res);
        self.assertIsInstance(v, (int, long))
        self.assertTrue(v)


        v = LSMResultGetCategory(res, 0)
        self.assertIsInstance(v, (int, long))

        v = LSMResultGetScore(res, 0)
        self.assertIsInstance(v, float)


        self.assertResultIsCFRetained(LSMResultCopyWord)
        v = LSMResultCopyWord(res, 0)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(LSMResultCopyToken)
        v = LSMResultCopyToken(res, 0)
        self.assertIsInstance(v, CFDataRef)

        v = LSMMapStartTraining(map)
        mytext = LSMTextCreate(None, map)



        v = LSMTextAddToken(mytext, v)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(LSMResultCopyWordCluster)
        v = LSMResultCopyWordCluster(res, 0)
        self.assertIsInstance(v, CFArrayRef)

        self.assertResultIsCFRetained(LSMResultCopyTokenCluster)
        v = LSMResultCopyTokenCluster(res, 0)
        self.assertIsInstance(v, CFArrayRef)

        fn = '/tmp/pyobjc.test'
        url = CFURLCreateWithFileSystemPath(None, fn, kCFURLPOSIXPathStyle, False)
        self.assertIsInstance(url, CFURLRef)
        v = LSMMapWriteToURL(map, url, 0)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(LSMMapCreateFromURL)
        map2 = LSMMapCreateFromURL(None, url, 0)
        self.assertIsInstance(map2, LSMMapRef)

        if os.path.exists(fn):
            os.unlink(fn)

        fp = CFWriteStreamCreateWithAllocatedBuffers(None, None)
        self.assertIsInstance(fp, CFWriteStreamRef)
        CFWriteStreamOpen(fp)

        v = LSMMapWriteToStream(map, text, fp, 0)
        sel.assertIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
